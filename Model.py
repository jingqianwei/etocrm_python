#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/5 16:09
# @Author  : Chinwe
# @File    : Model.py
# 参考地址：https://www.cnblogs.com/itdyb/p/5700614.html
# 使用pip install mysqlclient命令安装mysqlclient失败方法 https://blog.csdn.net/cn_1937/article/details/81533544

# import MySQLdb
#
# # host：ip地址， port：端口，user：用户名，passwd：密码，db：指定数据库，charset：数据库编码
# db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='mysqlkoa', charset='utf8')
#
# # 使用cursor()方法获取操作游标
# cursor = db.cursor()
#
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 创建的sql语句
# sql = """
#         create table if not EXISTS user (
#           user_id int(11) PRIMARY KEY,
#           username VARCHAR(20)
#         )
# """
# # 用于执行一个数据库的查询命令
# cursor.execute(sql)
# for i in range(1, 10):
#     cursor.execute("insert into user(user_id, username) values('%d', '%s')" % (int(i), 'name' + str(i)))
#
# # 提交当前事物
# db.commit()
#
# # 关闭游标
# cursor.close()
#
# # 关闭数据库连接
# db.close()
