# author: Igor Kazak
"""Test task for python developer"""

import selectors
import socket

import sportparser

PORT = 4040


class SportInfoServer:
    MESSAGE_SIZE = 1000
    PRINT_FORMAT_STRING = "Спортсмен, нагрудный номер {:04d} прошёл отсечку {:2} в {:02d}:{:02d}:{:02d}.{:d}, группа: {:d}\n"

    def __init__(self, port: int, file_output: str):
        """
        constructor of sport TCP server
        :param port (int): port of server
        :param file_output (string): filename of log file
        """
        self.file_output_name = file_output
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("", port))
        self.socket.listen(100)
        self.socket.setblocking(False)
        self.selector = selectors.DefaultSelector()
        self.selector.register(self.socket, selectors.EVENT_READ, self.__handler_accept)

    def __handler_accept(self, sock, mask):
        conn, address = sock.accept()
        conn.setblocking(False)
        self.selector.register(conn, selectors.EVENT_READ, self.__handler_read)

    def __write_data(self, sportsmen):
        output_str = self.PRINT_FORMAT_STRING.format(
                sportsmen.number, sportsmen.channel, sportsmen.hours,
                sportsmen.minutes, sportsmen.seconds, sportsmen.milliseconds // 100, sportsmen.group)
        self.file_output.write(output_str)
        self.file_output.flush()
        if sportsmen.group == 0:
            print(output_str, end = '')

    def __handler_read(self, conn, mask):
        data = conn.recv(self.MESSAGE_SIZE)
        try:
            if data:
                sportsmen = sportparser.parse_sportsmen(data.decode("utf-8"))
                self.__write_data(sportsmen)
            else:
                self.selector.unregister(conn)
                conn.close()
        except sportparser.ParseException:
            self.selector.unregister(conn)
            conn.close()

    def start(self):
        """
        Just call this function for running server
        """
        with open(self.file_output_name, "w") as self.file_output:
            while True:
                events = self.selector.select()
                for key, mask in events:
                    callback = key.data
                    callback(key.fileobj, mask)


if __name__ == '__main__':
    server = SportInfoServer(PORT, "athletes.txt")
    server.start()
