# -*- coding: utf-8 -*-
"""
cron: 15 15 * * *
new Env('141hongkong');
"""

from unittest import result
import requests

from notify_mtr import send
from utils import get_data

class HONGKONG141:
    def __init__(self, check_items):
        self.check_items = check_items
    
    @staticmethod
    def generate_headers(cookie):
        headers = {
            "Host": "api.sfacg.com",
            "authority": "141hongkong.com",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,ja;q=0.5,th;q=0.4,vi;q=0.3,zh-HK;q=0.2,en-GB;q=0.1,en-NZ;q=0.1",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "accept": "*/*",
            "referer": "https://141hongkong.com/home.php?mod=space&do=notice",
            "cookie": cookie,
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }
        return headers

    def check_cookie(self, cookie):
        headers = self.generate_headers(cookie)
        req = requests.get("https://141hongkong.com/plugin.php?id=dsu_amupper:pper&ppersubmit=true&formhash=56607f37&infloat=yes&handlekey=dsu_amupper&inajax=1&ajaxtarget=fwin_content_dsu_amupper", headers=headers)
        result = req.content.decode("utf-8")
        print(result)
        return result

    def main(self):
        for check_item in self.check_items:
            cookie = check_item.get("cookie")
            info = self.check_cookie(cookie)
        return info


if __name__ == "__main__":
    data = get_data()
    _check_items = data.get("141hongkong", [])
    res = HONGKONG141(check_items=_check_items).main()
    send("141hongkong", res)
