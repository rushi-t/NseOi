import random

import requests


class ProxyRequests:
    proxy_list = [

    ]

    proxy_list_http = [

    ]


    headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,mr-IN;q=0.8,mr;q=0.7'
    }

    def __init__(self):
        self.session = requests.Session()

    def get(self, url):
        proxy_index = random.randint(0, len(self.proxy_list_http) - 1)
        proxies = {"https": self.proxy_list_http[proxy_index]}
        return self.session.get(url, headers=self.headers, proxies=proxies)
