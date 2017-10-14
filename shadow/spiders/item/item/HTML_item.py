#!/usr/bin/python3

'''
该模块定义HTML的数据对象item
'''

class HTML_item:
    def __init__(self , url , number_photo , content , photos):
        self.url = url
        self.number = number_photo
        self.content = content
        # photos 是HTML网页所包含的图片的URL
        try:
            if isinstance(photos , list):
                self.photos = photos.copy()
            else:
                raise Exception('传入给HTML_item对象的图片对象不是列表类型')
        except:
            print("创建HTML_item对象错误")
        finally:
            self.photos = []
