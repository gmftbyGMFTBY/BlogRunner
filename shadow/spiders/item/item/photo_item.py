#!/usr/bin/python3

'''
该模块是构建的图片item对象
'''

class photo_item:
    def __init__(self , photo_url , type_ , photo_content , page_url):
        self.photo_url = photo_url
        self.type_ = type_
        self.photo_content = photo_content
        self.page_url = page_url
    def set_photo_url(self , url):
        self.photo_url = url
    def set_content(self , content):
        self.content = content
    def set_page_url(self , url):
        self.page_url = url
