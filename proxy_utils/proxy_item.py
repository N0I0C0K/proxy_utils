from .proxy_type import *


class ProxyItem:
    def __init__(self, ip: IpType, port: Port, method: Method, reply_time: ReplyTime = 100) -> None:
        self.ip = ip
        self.port = port
        self.method = method
        self.reply_time = reply_time
        self.address = f'{self.ip}:{self.port}'

    def __repr__(self) -> str:
        return f'\n{self.address} | {self.reply_time}'
