#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/7 10:44
# @Author  : Chinwe
# @File    : DbReptile.py

import requests
import json
from DbHelper import DB

class DbReptile:
    def __init__(self):
        self._url = 'http://www.toutiao.com/api/pc/focus/'
        self._db = DB('localhost', 3306, 'root', 'root', 'mysqlkoa')

    def create(self):
        sql = """
            CREATE TABLE IF NOT EXISTS `data`(
               `id` INT UNSIGNED AUTO_INCREMENT,
               `title` VARCHAR(100) NOT NULL,
               `img_url` VARCHAR(200) NOT NULL,
               `media_url` VARCHAR(200) NOT NULL,
               `create_at` DATE,
               PRIMARY KEY ( `id` )
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """
        return self._db.create(sql)

    def getData(self):
        wbData = requests.get(self._url).text
        data = json.loads(wbData)  # json转array
        if data['message'] == 'success':
            news = data['data']['pc_feed_focus']
            if self.create():
                for val in news:
                    title = val['title']
                    img_url = val['image_url']
                    media_url = val['media_url']
                    print(title, img_url, media_url)
                    sql = "INSERT INTO `data` (`title`, `img_url`, `media_url`, `create_at`) VALUES \
                          ('{0}', '{1}', '{2}', '{3}');" .format(title, img_url, media_url, '2018-11-07 11:16:24')
                    self._db.update(sql)
        else:
            print('抓取数据出错')


if __name__ == '__main__':
    reptile = DbReptile()
    reptile.getData()
