from typing import Literal

IpType = str
Port = str
Address = str
ReplyTime = float
Method = Literal['HTTP', 'HTTPS']

ProxyDict = dict[Method, Address]
