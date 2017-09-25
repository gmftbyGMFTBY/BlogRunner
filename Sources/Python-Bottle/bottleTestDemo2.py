from bottle import *
import requests
 
@get('/')
def homepage():
    r= requests.get("http://www.baidu.com")

    return template("<br><H1 style='color:red;text-align:center;'>" #演示②
    +"抓取到的数据是:</H1><br><b>{{text}}</b>",text=r.text)
    
#运行Web服务器
run(host='', port=8080)
