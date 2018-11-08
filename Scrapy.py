#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/7 13:27
# @Author  : Chinwe
# @File    : Scrapy.py

import json
import os
import pymongo
import requests
from urllib.parse import urlencode
from urllib.request import urlretrieve

class Scrapy:
    def __init__(self):
        self._mongo = pymongo.MongoClient(host='localhost', port=27017)
        # 指定数据库为picture
        self._db = self._mongo['picture']
        # 指定集合为beauty
        self._collect = self._db['beauty']

    def start(self):
        path = 'C:/image/'
        # 是否有这个路径
        if not os.path.exists(path):
            # 创建路径
            os.makedirs(path)
        data = {'ch': 'photogtaphy', 'listtype': 'new'}
        base_url = 'https://image.so.com/zj?0'
        for page in range(1, 50 + 1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params
            response = requests.get(url)
            wbData = json.loads(response.text)
            if wbData.get('list'):
                for image in wbData.get('list'):
                    imageid = image.get('imageid')
                    title = image.get('group_title')
                    url = image.get('qhimg_url')
                    thumb = image.get('qhimg_thumb_url')
                    file_name = url.split('/')[-1]
                    filename = path + file_name
                    print(filename)
                    # 下载网上图片保存到本地
                    urlretrieve(url, filename=filename)
                    print(imageid, title, url, thumb)
                    data = {
                        'imageid': imageid,
                        'title': title,
                        'img_url': url,
                        'thumb': thumb,
                        'create_at': '2018-11-07 13:34:24'
                    }
                    # 插入一行数据
                    self._collect.insert_one(data)
                    # 查询所有数据
                for i in self._collect.find():
                    print(i)


    @staticmethod
    def boss():
        url = 'https://www.zhipin.com/mobile/jobs.json?city=101020100&query=PHP'
        response = requests.get(url)
        print(response)
        wbData = json.loads(response.text)
        print(wbData)


if __name__ == '__main__':
    res = Scrapy()
    res.boss()






