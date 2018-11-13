#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/13 11:37
# @Author  : Chinwe
# @File    : Monitor.py

import threading
import MySQLdb
from datetime import datetime
from time import sleep
import smtplib
from email.mime.text import MIMEText
from Logger import Logger

# 实例日志类
Logger = Logger('logs')

def get_con():
    host = '127.0.0.1'
    port = 3306
    db = 'logs'
    user = 'root'
    passwd = 'root'
    conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd, db=db,
                           charset='utf8')

    return conn

def calculate_time():
    now = datetime.now()
    now_min = now.minute

    if now_min < 2:
        now_min += 60 - 2
    else:
        now_min -= 2

    return now.replace(minute=now_min).strftime("%Y-%m-%d %H:%M:%S")

def get_data():
    select_time = calculate_time()
    Logger.info('select_time: ' + select_time)
    sql = "select file_name, message from logs.app_logs_record " \
            "where log_time > " + "'"+select_time+"'" \
            "and level = " + "'ERROR'" \
            "order by log_time desc"
    conn = get_con()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result

def send_email(content):
    sender = '1007123591@qq.com'
    receiver = ['jqw01@qq.com', 'jqw02@qq.com']
    host = 'smtp.163.com'
    port = 465
    msg = MIMEText(content)
    msg['From'] = '1007123591@qq.com'
    msg['To'] = 'jqw01@qq.com,jqw02@qq.com'
    msg['Subject'] = 'system error warning'

    try:
        smtp = smtplib.SMTP_SSL(host, port)
        smtp.login(sender, '123456')
        smtp.send_message(sender, receiver, msg.as_string())
        Logger.info('send email success')
    except Exception as e:
        Logger.error(e)

# 单线程独立跑
def task():
    while True:
        Logger.info('monitor running')
        result = get_data()
        if result is not None and len(result) > 5:
            content = 'recharge error: '
            Logger.info('a lot of error, so send mail')
            for r in result:
                content += r[1] + '\n'
            send_email(content)
        sleep(2*60)

def run_monitor():
    monitor = threading.Thread(target=task())
    monitor.start()

if __name__ == '__main__':
    run_monitor()
