from requests import get
from re import findall
from random import choice
from .proxy_type import *


class ProxyCoreSync:
    def __init__(self, pages: int = 1) -> None:
        self.proxy_dict: dict[Method, list[str]] = {'HTTP': [], 'HTTPS': []}
        for page in range(1, pages+1):
            html_res = get(
                f'https://proxy.ip3366.net/free/?action=china&page={page}')
            reg_exp = r"<td data-title=\"IP\">(.*)<[\s\S]*?data-title=\"PORT\">(.*)<[\s\S]*?data-title=\"类型\">(.*)<[\s\S]*?data-title=\"响应速度\">([.,0-9]*)[\s\S]*?data-title=\"最后验证时间\">(.*)<"
            match_res: list[tuple[IpType, Port, Method, ReplyTime, str]] = findall(
                reg_exp, html_res.text)
            for ip, port, method, reply_time, update_time in match_res:
                self.proxy_dict[method].append(f'http://{ip}:{port}')

    def get_proxy(self) -> ProxyDict:
        proxy: ProxyDict = {}
        proxy['HTTP'] = choice(self.proxy_dict['HTTP'])
        proxy['HTTPS'] = choice(self.proxy_dict['HTTPS'])
        return proxy


def test():
    a = ProxyCoreSync(1)
    print(a.proxy_dict)
    proxy = a.get_proxy()
    print(proxy)
    res = get('https://www.baidu.com', proxies=proxy)
    print(res.text)
