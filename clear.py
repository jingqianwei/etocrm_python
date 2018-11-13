#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/13 10:54
# @Author  : Chinwe
# @File    : clear.py

import os
import shutil

# 这里是你要整理的文件夹，可以根据需要赋予相应的路径
path_root = os.path.join(os.getcwd(), '\\Users\chinwe.jing\Desktop\资料')

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

def collect():
    """
    把文件根据文件扩展名自动新建相应的文件，
    并把对应的文件剪切进去
    """
    for f in os.listdir(path_root):
        file_old = os.path.join(path_root, f)

        if os.path.isfile(file_old):
            extension = f.split('.')[1]
            path_sub_folder = os.path.join(path_root, extension)
            file_new = os.path.join(path_sub_folder, f)

            create_folder(path_sub_folder)
            move_file(file_old, file_new)


def extract():
    """
    如果想回退文件整理操作，在下面的main函数里面，
    注释掉collect函数，使用extract函数
    """
    for root, dirs, files in os.walk(path_root):
        if dirs:
            for d in dirs:
                path_d = os.path.join(path_root, d)
                for f in os.listdir(path_d):
                    file_old = os.path.join(path_d, f)
                    file_new = os.path.join(path_root, f)

                    move_file(file_old, file_new)
                print(path_d)
                delete_folder(path_d)

def main():
    collect()
    # extract()

if __name__ == '__main__':
    main()