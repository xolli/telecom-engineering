# Test task "TCP-server"

This TCP server reads data in the specified format and displays it in the console and file.

- Name of output file: athletes.txt
- Binding port: 4040 

## Input fomat
Format input line: "BBBB NN HH:MM:SS.zhqxGG\r\n"

BBBB: number of athlet

NN: channel id

HH: Hours

MM: minutes

SS: seconds

zhq: milliseconds

GG: group number

Example: 0008 C2 11:12:01.764 00

# Requirements
Python version above 3.7

# Running server
```bash
pip3 install -r requirements.txt
python3 sportinfoserver.py
```

# Example input data
```bash
$ telnet 127.0.0.1 4040

0004 C1 01:13:02.877 00
0002 C1 01:13:32.957 20
0001 C1 01:14:01.543 02
0004 C1 01:14:15.134 99
```

