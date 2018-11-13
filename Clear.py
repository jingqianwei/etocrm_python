#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/13 10:54
# @Author  : Chinwe
# @File    : Clear.py

import os
import shutil


# 创建文件夹
def create_folder(path_sub_folder):
    if not os.path.exists(path_sub_folder):
        os.mkdir(path_sub_folder)

# 移动文件
def move_file(old, new):
    if not os.path.exists(new):
        shutil.move(old, new)

# 删除文件夹
def delete_folder(path_d):
    if os.path.exists(path_d) and not os.listdir(path_d):
        os.rmdir(path_d)

# 判断目录下是否存在文件
def is_folder_file(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            return True
    return False

class Clear(object):
    def __init__(self, path):
        # 这里是你要整理的文件夹，可以根据需要赋予相应的路径
        self.path_root = os.path.join(os.getcwd(), path)

    def collect(self):
        """
        把文件根据文件扩展名自动新建相应的文件，
        并把对应的文件剪切进去
        """
        for f in os.listdir(self.path_root):
            file_old = os.path.join(self.path_root, f)

            if os.path.isfile(file_old):
                extension = f.split('.')[1]
                path_sub_folder = os.path.join(self.path_root, extension)
                file_new = os.path.join(path_sub_folder, f)

                create_folder(path_sub_folder)
                move_file(file_old, file_new)


    def extract(self):
        """
        回退文件上面整理操作
        """
        for root, dirs, files in os.walk(self.path_root):
            if dirs:
                for d in dirs:
                    path_d = os.path.join(self.path_root, d)
                    for f in os.listdir(path_d):
                        file_old = os.path.join(path_d, f)
                        file_new = os.path.join(self.path_root, f)

                        move_file(file_old, file_new)
                    delete_folder(path_d)

    def main(self):
        """
        统一入口
        """
        if is_folder_file(self.path_root):  # 存在文件，整理
            self.collect()
            print('整理成功')
        else:  # 不存在就后退
            self.extract()
            print('回退成功')

if __name__ == '__main__':
    clear = Clear('\\Users\chinwe.jing\Desktop\资料')
    clear.main()