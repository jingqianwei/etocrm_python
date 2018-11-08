#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/6 14:26
# @Author  : Chinwe
# @File    : DbHelper.py

import MySQLdb
# 引入类, from 后面为文件名, import 后面为类名
from Logger import Logger


class DB:
    # host：ip地址， port：端口，user：用户名，passwd：密码，db：指定数据库，charset：数据库编码
    def __init__(self, host, port, user, passwd, db):
        self._logger = Logger('logs')
        self._host = host
        self._port = port
        self._user = user
        self._passwd = passwd
        self._db = db
        self._conn = self.connectMysql()
        if self._conn:
            self._cursor = self._conn.cursor()

    # 连接
    def connectMysql(self):
        try:
            conn = MySQLdb.connect(host=self._host, port=self._port, user=self._user, passwd=self._passwd, db=self._db,
                                   charset='utf8')
        except Exception as e:
            conn = False
            self._logger.error('连接失败，错误信息为，%s' % e)
        else:
            self._logger.info('数据库连接成功')

        return conn

    # 创建
    def create(self, sql):
        res = False
        if self._conn:
            try:
                self._cursor.execute(sql)
                res = True
            except Exception as e:
                self._logger.error('创建失败，错误信息为，%s' % e)
            else:
                self._logger.info('数据表创建成功')
                self.close()

        return res

    # 查询
    def query(self, sql):
        res = ''
        if self._conn:
            try:
                self._cursor.execute(sql)
                if self._cursor.rowcount > 1:  # 执行execute()方法后影响的行数
                    res = self._cursor.fetchall()
                else:
                    res = self._cursor.fetchone()
            except Exception as e:
                self._logger.error('查询失败，错误信息为，%s' % e)
            else:
                self._logger.info('查询成功，结果为，%s' % res)
                self.close()

        return res

    # 更新, 插入, 删除
    def update(self, sql):
        flag = False
        if self._conn:
            try:
                self._cursor.execute(sql)
                self._conn.commit()
                flag = True
            except Exception as e:
                self._conn.rollback()
                self._logger.error('更新失败，错误信息为，%s' % e)
            else:
                self._logger.info('更新或插入或删除成功')
                self.close()

        return flag

    # 关闭
    def close(self):
        if self._conn:
            try:
                if type(self._cursor) == 'object':
                    self._cursor.close()

                if type(self._conn) == 'object':
                    self._conn.close()
            except Exception as e:
                self._logger.error('关闭失败，错误信息为，%s,%s,%s' % (e, type(self._cursor), type(self._conn)))
            else:
                self._logger.info('关闭成功')


if __name__ == '__main__':
    # 测试方法
    model = DB('localhost', 3306, 'root', 'root', 'mysqlkoa')
