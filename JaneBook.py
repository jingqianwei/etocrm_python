#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @TIME    : 2018/11/8 10:38
# @Author  : Chinwe
# @File    : JaneBook.py
import pymongo
import xlwt
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

host = 'https://www.jianshu.com/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}

def get_urls():
    """从首页获取文章url"""
    content = requests.get(host, headers=headers).text
    soup = BeautifulSoup(content, 'lxml')
    for a in soup.find_all('a', class_='title'):
        yield urljoin(host, a.get('href'))

def get_info(url, flag=True):
    """获取文章的标题，作者，发布时间，以及正文内容"""
    content = requests.get(url, headers=headers).text
    soup = BeautifulSoup(content, 'lxml')
    title = soup.find('h1', class_='title').text
    author = soup.find('span', class_='name').text
    timestamp = soup.find('span', class_='publish-time').text.replace('*', '')
    body = soup.find('div', class_='show-content-free')
    p_list = []
    for p in body.find_all('p'):
        p_list.append(p.text)

    if flag:
        body_str = '\n'.join(p_list)
        return [url, title, author, timestamp, body_str]
    else:
        return {'url': url, 'title': title, 'author': author, 'timestamp': timestamp, 'body': p_list}
    # return {'url': url, 'title': title, 'author': author, 'timestamp': timestamp, 'body': body_str}

def save_as_xls(info_list):
    """将获取的文章信息储存到本地"""
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet1', cell_overwrite_ok=True)
    titles = ['链接', '标题', '作者', '发布时间', '正文']
    # keys = ['url', 'title', 'author', 'timestamp', 'body']
    for index, title in enumerate(titles):
        worksheet.write(0, index, title)
        for i, info in enumerate(info_list):
            for j, key in enumerate(info):
                # for j, key in enumerate(keys):
                worksheet.write(i+1, j, key)
    workbook.save('excel/info.xls')

def save_as_mongo(info_data):
    """将获取的文章信息储存到mongodb数据库"""
    mongo = pymongo.MongoClient(host='localhost', port=27017)
    # 指定数据库为picture
    db = mongo['janeBook']
    # 指定集合为beauty
    collect = db['info']
    # 插入数据
    collect.insert_many(info_data)

def save_as_txt(info_list):
    with open('file/jane_book.txt', 'w', encoding='utf-8') as f:
        for val in info_list:
            f.write('\n' . join(val))

def main():
    """main function"""
    info_list, info_data = [], []
    for url in get_urls():
        info_list.append(get_info(url))
        info_data.append(get_info(url, False))

    save_as_txt(info_list)
    save_as_mongo(info_data)
    save_as_xls(info_list)

if __name__ == '__main__':
    main()
