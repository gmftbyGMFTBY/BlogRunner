#!/usr/bin/python3

'''
该模块构建response响应类，实现我们响应的封装
'''

class response:
    def __init__(self , class_ , content , type_ , status , headers , spider_type , url):
        self.class_ = class_
        self.content = content
        self.type_ = type_
        self.status = status
        self.headers = headers
        self.spider_type = spider_type
        self.url = url
