#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/6 15:12
# @Author  : Chinwe
# @File    : Logger.py

import logging
import datetime
import os


class Logger:
    def __init__(self, dirs, file='python-' + datetime.datetime.now().strftime('%Y-%m-%d') + '.log',
                 Clevel=logging.DEBUG, Flevel=logging.DEBUG):
        path = dirs + '/' + file
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s [%(filename)s:%(lineno)s]', '%Y-%m-%d %H:%M:%S')
        # 设置控制台日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(Clevel)
        # 设置文件日志
        if not os.path.exists(dirs):  # 目录不存在就创建
            os.makedirs(dirs)
        fh = logging.FileHandler(path, encoding='utf-8')
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    logger = Logger('logs', 'logging-' + time + '.log', logging.ERROR, logging.DEBUG)
    logger.debug('一个debug信息')
    logger.info('一个info信息')
    logger.war('一个warning信息')
    logger.error('一个error信息')
    logger.cri('一个致命critical信息')
