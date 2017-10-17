#!/usr/bin/python3

import spider
from bs4 import BeautifulSoup
import urllib.request as ur
import urllib.parse as up
import sys
sys.path.append('..')
import request.request

class websitespider(spider.spider):
    def __init__(self , ruler):
        self.ruler = ruler    # 明确ruler对象
    def parse(self , res):
        '''解析模块，输入是response,输出是item和request的列表'''
        for_item = []
        for_request = []
        if res.class_ == 0 :    # 页面是搜索页面
            soup = BeautifulSoup(res.content , 'lxml')
            elem = soup.find(self.ruler.content)
            request = elem.find_all(href = True)
            for i in request:
                for_request.append(request(1 , 5 , up.urljoin(res.url , request) , 1 , 2))
            return for_request
        else :     # 页面是资源页面
            if res.type == 0 :    # 页面是HTML页面
                
            else :    # 页面是图片页面
                pass
    def create_start_request(self , domain , name):
        '''
        提供域名和用户，在博文网站站点爬取对应的博主的博文
        '''
        return request(0 , 5 , domain + name , 1 , 2)
        
        
