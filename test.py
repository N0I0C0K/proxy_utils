# from proxy_utils.proxy_sync import test

# test()
from requests import session, get
import re

sess = session()
sess.verify = False
sess.headers = {'User-Agent': 'cdasdasdasdas'}
r = sess.get('https://www.zdaye.com/dayProxy.html')

r.encoding = 'utf-8'
urls = re.findall(r"class=\"thread_title\"><a href=\"([\s\S]*?)\"", r.text)

r = sess.get(f'https://www.zdaye.com{urls[0]}')

r.encoding = 'utf-8'
ips = re.findall(r"\"/ip/CheckHttp/([0-9,\.,:]*)\"[\s\S]*?(HTTPS?)", r.text)
print(ips)
