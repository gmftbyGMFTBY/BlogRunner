#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import sys
import urllib.request as ur
import hashlib
import time

def add_url(soup):
    url = []
    block = soup.find_all(class_ = 'result c-container ')
    for i in block:
        url.append(i.find(name = 'a')['href'])
    return url

def get_next_page(next_page):
    page = requests.get(next_page)
    page.encoding = 'utf8'
    return page

# 获取关键字 
# keyword = sys.argv[1]
keyword = 'python'

# 利用百度搜索引擎进行关键字检索
driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys(keyword)
driver.find_element_by_id('su').send_keys(Keys.ENTER)
url = driver.current_url
url = url.replace('https' , 'http')
print('URL :' , url)

page = requests.get(url)
page.encoding = 'utf8'


now_url = url
page_number = 10    # 最大抓取页数上限
page_sum_number = page_number

urls = []

while page_number:
    page_number -= 1
    soup = BeautifulSoup(page.text , 'lxml')
    urls.extend(add_url(soup))    # 扩展urls列表
    # 获取下一页链接，准备跳转,更新page
    # print('Href :' , soup.find_all(class_ = 'n')[0]['href'])
    next_page = ur.urljoin(url , soup.find_all(class_ = 'n')[0]['href'])
    page = get_next_page(next_page)    # 获取下一个页面,返回requests对象
    # print(urls , len(urls))
    print("page scanning ... %d / %d" % (page_number , page_sum_number))

# save the page to the folder at /home/lantian/fortest/baidu/raw
print('总计爬取网页 %d' % len(urls))
for j , i in enumerate(urls):
    md5 = hashlib.md5()
    md5.update(i.encode('utf8'))    # md5加密对url压缩存储
    try:
        content = md5.hexdigest()
        print('Downloading ' + content + ' ...' , j + 1)
        ur.urlretrieve(i , '/home/lantian/fortest/baidu/raw/' + content)
    except:
        print('百度服务器正在扫描爬虫，延时 10s 躲避')
        time.sleep(10)
print('End')
