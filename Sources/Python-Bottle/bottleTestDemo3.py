from bottle import *
import requests
 
@get('/')
def homepage():
    return static_file("index.html",root=".")

#演示③：使用vue和elementUI的前端页面+request.query.uname

@route('/testPython')
def testpython():
    r = requests.get("http://www.baidu.com")
    return r.text

#根据前端页面的结构返回所请求的文件
@get('/static/css/<filename>')
def css(filename):
    return static_file(filename,root='static/css/')
@get('/static/js/<filename>')
def js(filename):
    return static_file(filename,root='static/js/')
@get('/static/img/<filename>')
def img(filename):
    return static_file(filename,root='static/img/')
@get('/static/fonts/<filename>')
def fonts(filename):
    return static_file(filename,root='static/fonts/')

#运行Web服务器
run(host='', port=8080)
