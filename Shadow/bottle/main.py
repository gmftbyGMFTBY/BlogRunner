#!/usr/bin/python3

'''
该模块执行对应的请求
前端发送的求情，在后端执行对应的语句或者返回对应的JSON格式数据
'''

# 库导入
from bottle import template , route , run , static_file
from bottle import request , response
import sys
sys.path.append('..')
import sql.sql as sql
from ai import ....    # ai预测模块

'''
该函数接收用户上传的URL，并且经过我们的ai预测返回一个可能的值作为预测的阅读量
'''
@route('/upload' , method = 'POST')
def get_upload():
    url = request.forms.get('url')    # 获取用户为文件定义的名字,一定要发布出去才可以使用
    import requests
    page = requests.get(url , headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    page.encoding = 'utf8'
    f = page.text
    force = ....
    return force    

# 启动服务器
run(host = '127.0.0.8' , port = 8888)
