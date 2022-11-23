from requests import get
from re import findall
from random import choice
from .proxy_type import *
from .proxy_item import ProxyItem


class ProxyCoreSync:
    def __init__(self, pages: int = 1) -> None:
        self.proxy_dict: dict[Method, list[ProxyItem]] = {
            'http': [], 'https': []}
        for page in range(1, pages+1):
            html_res = get(
                f'https://proxy.ip3366.net/free/?action=china&page={page}')
            reg_exp = r"<td data-title=\"IP\">(.*)<[\s\S]*?data-title=\"PORT\">(.*)<[\s\S]*?data-title=\"类型\">(.*)<[\s\S]*?data-title=\"响应速度\">([.,0-9]*)[\s\S]*?data-title=\"最后验证时间\">(.*)<"
            match_res: list[tuple[IpType, Port, Method, ReplyTime, str]] = findall(
                reg_exp, html_res.text)
            for ip, port, method, reply_time, update_time in match_res:
                method = method.lower()
                self.proxy_dict[method].append(
                    ProxyItem(ip, port, method, float(reply_time)))
        self.proxy_dict['http'].sort(key=lambda x: x.reply_time)
        self.proxy_dict['https'].sort(key=lambda x: x.reply_time)

    def get_proxy(self) -> ProxyDict:
        proxy: ProxyDict = {}
        proxy['http'] = self.proxy_dict['http'][0].address
        proxy['https'] = self.proxy_dict['https'][0].address
        return proxy


def test():
    # a = ProxyCoreSync(10)
    # print(a.proxy_dict)
    # proxy = a.get_proxy()
    proxy = {'http': '218.59.139.238:80', 'https': '36.137.208.16:7777'}
    print(proxy)
    try:
        res = get('http://httpbin.org/get', proxies=proxy)
        print(res.text)
    except:
        print('failed')
    else:
        print('success')
