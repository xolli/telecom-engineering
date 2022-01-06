# author: Igor Kazak
"""Module to parse data of athletes"""

from dataclasses import dataclass
from parse import *

FORMAT_STRING = "{sportsmen:4d} {channel_id:2w} {hours:2d}:{minutes:2d}:{seconds:2d}.{milliseconds:3d} {group:2d}\r\n"


class ParseException(Exception):
    def __init__(self, request_string: str):
        """
        :param request_string: body of wrong request
        """
        self.request_string = request_string
        self.message = "Parse exception of request: " + request_string
        super().__init__("Parse exception of request: " + request_string)


@dataclass
class Sportsmen:
    number: int
    channel: str
    hours: int
    minutes: int
    seconds: int
    milliseconds: int
    group: int


def parse_sportsmen(sport_string: str) -> Sportsmen:
    """
    Parse info string about sportsmen

    :param sport_string: string with information about sportsmen
    :return (Sportsmen): information about input sportsmen
    """
    parse_result = parse(FORMAT_STRING, sport_string)
    if parse_result == None:
        raise ParseException(sport_string)
    return Sportsmen(
        number=parse_result["sportsmen"],
        channel=parse_result["channel_id"],
        hours=parse_result["hours"],
        minutes=parse_result["minutes"],
        seconds=parse_result["seconds"],
        milliseconds=parse_result["milliseconds"],
        group=parse_result["group"],
    )
