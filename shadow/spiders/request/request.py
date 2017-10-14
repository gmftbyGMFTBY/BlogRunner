#!/usr/bin/python3

'''
该模块构建request请求类，实现我们的的请求的封装
'''

class request:
    def __init__(self , class_ , depth , url , type_ , spider_type):
        '''
        类的初始化函数:
        self , class_ , depth , url , type_ , spider_type
        初始化构建request请求
        '''
        self.class_ = class_
        self.depth_ = depth_
        self.url = url
        self.type_ = type_
        self.spider_type = spider_type
    
