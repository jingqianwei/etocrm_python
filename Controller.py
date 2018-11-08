#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/6 18:03
# @Author  : Chinwe
# @File    : Controller.py

from DbHelper import DB


class Controller:
    def __init__(self):
        self._db = DB('localhost', 3306, 'root', 'root', 'mysqlkoa')

    # 创建数据表
    def create(self):
        sql = """
            CREATE TABLE IF NOT EXISTS `article`(
               `article_id` INT UNSIGNED AUTO_INCREMENT,
               `article_title` VARCHAR(100) NOT NULL,
               `article_author` VARCHAR(40) NOT NULL,
               `create_at` DATE,
               PRIMARY KEY ( `article_id` )
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;
        """
        res = self._db.create(sql)
        if res:
            self._db._logger.info('创建数据表成功')

    # 查询数据
    def select(self):
        sql = 'SELECT * FROM `user` WHERE `user_id` = 1'
        res = self._db.query(sql)
        self._db._logger.info(res)

    # 更新数据
    def update(self):
        sql = 'UPDATE `user` SET `username` = "name0" WHERE `user_id` = 1'
        res = self._db.update(sql)
        if res:
            self._db._logger.info('更新成功')

    # 插入数据
    def insert(self):
        sql = """
            INSERT INTO `article` (`article_title`, `article_author`, `create_at`) VALUES 
            ('今日头条', '张一鸣', '2018-11-07 12:01:11'), ('腾讯新闻', '马化腾', '2018-11-08 12:01:11'), 
            ('搜狐新闻', '张朝阳', '2018-11-09 12:01:11'), ('网易新闻', '丁磊', '2018-11-10 12:01:11')
        """
        res = self._db.update(sql)
        print(res)

    # 删除数据
    def delete(self):
        sql = 'DELETE FROM `article` WHERE `article_id` = 1'
        res = self._db.update(sql)
        print(res)



# 测试结果
if __name__ == '__main__':
    handle = Controller()
    handle.delete()
