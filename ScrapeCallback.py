#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/12 17:38
# @Author  : Chinwe
# @File    : ScrapeCallback.py

import csv
import lxml.html
from Weather import link_crawler


# 使用回调类而非回调函数以保持csv中write属性的状态
class ScrapeCallback:
    def __init__(self):
        self.writer = csv.writer(open('weather.csv', 'w', newline=''))
        # 天气 最高温/最低温 风力
        self.fields = ('天气', '最高/低温', '风力')
        self.writer.writerow(self.fields)

    def __call__(self, url, html):
        # if re.search('/view/', url):
        tree = lxml.html.fromstring(html)
        td = tree.cssselect('p.wea')
        n = 0
        for wea in td:
            row = [tree.cssselect('p.wea')[n].text_content().strip(''),
                   tree.cssselect('p.tem')[n].text_content().strip(''),
                   tree.cssselect('p.win')[n].text_content().strip('')]
            n = n + 1
            self.writer.writerow(row)


if __name__ == '__main__':
        link_crawler('http://www.weather.com.cn/weather/101020100.shtml', '/(index|view)',
                     scrape_callback=ScrapeCallback())