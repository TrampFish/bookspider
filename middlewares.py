# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

class RandomUserAgentMiddleware:
    def process_request(self,request,spider):
        ua = random.choice(spider.setting.get("USER_AGENTS_LIST"))
        request.headers["User-Agent"] = ua

class RandomProxyMiddleware:
    def process_request(self,request,spider):
        with open("E:\翻墙软件\proxychecker\Working1.txt", 'r', encoding="utf-8")as f:
            proxies = []
            http_str = f.read()
            http_list = http_str.split("\n")
            for http in http_list:
                proxiey = "http://" + http
                proxies.append(proxiey)
            proxy = random.choice(proxies[1:-2])
            request.meta["PROXY"] = proxy
