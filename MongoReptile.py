#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/7 11:19
# @Author  : Chinwe
# @File    : MongoReptile.py

import pymongo, requests, json


class MongoReptile:
    def __init__(self):
        self._url = 'http://www.toutiao.com/api/pc/focus/'
        self._mongo = pymongo.MongoClient(host='localhost', port=27017)
        # 指定数据库为toutiao
        self._db = self._mongo['toutiao']
        # 指定集合为news
        self._collect = self._db['news']

    def getData(self):
        wbData = requests.get(self._url).text
        data = json.loads(wbData)
        if data['message'] == 'success':
            news = data['data']['pc_feed_focus']
            for val in news:
                title = val['title']
                img_url = val['image_url']
                media_url = val['media_url']
                print(title, img_url, media_url)
                data = {
                    'title': title,
                    'img_url': img_url,
                    'media_url': media_url,
                    'create_at': '2018-11-07 11:34:24'
                }
                # 插入一行数据
                self._collect.insert_one(data)
                # 查询所有数据
            for i in self._collect.find():
                print(i)
        else:
            print('抓取数据出错')


if __name__ == '__main__':
    mongo = MongoReptile()
    mongo.getData()

