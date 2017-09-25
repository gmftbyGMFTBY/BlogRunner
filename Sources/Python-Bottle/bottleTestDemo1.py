from bottle import *
import requests
 
@get('/')
def homepage():
    r= requests.get("http://www.baidu.com") #抓取数据

    return r.text

#运行Web服务器
run(host='', port=8090)
