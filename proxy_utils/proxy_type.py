from typing import Literal

IpType = str
Port = str
Address = str
ReplyTime = float
Method = Literal['http', 'https']

ProxyDict = dict[Method, Address]
