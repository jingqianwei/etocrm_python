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

# 保存说明文档
def save_as_txt(path, deal_file, info_list):
    file_name = os.path.join(path, deal_file)
    with open(file_name, 'w', encoding='utf-8') as f:
        for val in info_list:
            f.write(val + '\n')

# 读取说明文档
def read_as_txt(path, deal_file):
    file_name = os.path.join(path, deal_file)
    with open(file_name, 'r', encoding='utf-8') as f:
        contents = f.read().split('\n')  # 字符串转化为数组
        contents.pop()  # 删除最后一个空元素
        return contents

class Clear(object):
    def __init__(self, path, deal_file):
        # 这里是你要整理的文件夹，可以根据需要赋予相应的路径
        self.path_root = os.path.join(os.getcwd(), path)
        self.deal_file = deal_file
        self.new_create_folder = []

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
                # 记录哪些文件夹是新创建的
                if path_sub_folder not in self.new_create_folder:
                    self.new_create_folder.append(path_sub_folder)
        # 写入说明文件中
        save_as_txt(self.path_root, self.deal_file, self.new_create_folder)

    def extract(self):
        """
        回退文件上面整理操作
        """
        # # 粗暴型回退，不满足回退到跟整理之前的一样
        # for root, dirs, files in os.walk(self.path_root):
        #     if dirs:
        #         for d in dirs:
        #             path_d = os.path.join(self.path_root, d)
        #             for f in os.listdir(path_d):
        #                 file_old = os.path.join(path_d, f)
        #                 file_new = os.path.join(self.path_root, f)
        #
        #                 move_file(file_old, file_new)
        #             delete_folder(path_d)
        # os.remove(os.path.join(self.path_root, self.deal_file))  # 删除整理文件

        # 优雅型回退，满足回退到跟整理之前的一样
        if len(read_as_txt(self.path_root, self.deal_file)) > 0:  # 存在新创建的文件夹
            for path_d in read_as_txt(self.path_root, self.deal_file):
                for f in os.listdir(path_d):
                    file_old = os.path.join(path_d, f)
                    file_new = os.path.join(self.path_root, f)

                    move_file(file_old, file_new)
                delete_folder(path_d)
            os.remove(os.path.join(self.path_root, self.deal_file))  # 删除整理文件

    def main(self):
        """
        统一入口
        """
        if not os.path.isfile(os.path.join(self.path_root, self.deal_file)):  # 不存在整理文件
            self.collect()
            print('整理成功')
        else:  # 不存在就后退
            self.extract()
            print('回退成功')

if __name__ == '__main__':
    clear = Clear('\\Users\\chinwe.jing\\Desktop\\资料', '整理说明文档.txt')
    clear.main()