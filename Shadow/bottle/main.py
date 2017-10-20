#!/usr/bin/python3

'''
该模块执行对应的请求
前端发送的求情，在后端执行对应的语句或者返回对应的JSON格式数据
'''

# 库导入
from bottle import template , route , run , static_file
from bottle import request , response

@route('')


