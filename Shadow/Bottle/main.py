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
sys.path.append('../CSDN')

import MYSQL.sql as sql
from CSDN import analyse
from CSDN import website
from CSDN import keyword
from AI import get_grade    # ai预测模块

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
    # ...这个等待和前端的接口搭建完使用，或者可以开始着手进行博文的机器学习的算法训练集的搭建
    # 这里可以考虑我们的网页的feature数据不存入数据库，但是可以将数据传递给我们的get_grade的AI模块去得到对应的预测值
    # feature = analyse.crawl_sample( , , 0)
    # get_grade <= feature
    # ...
    force = None
    return force    


# 用户信息数据获取响应

# 用户登录路由
def check_login(username , passwd):
    print(username , passwd)
    save = sql.main(1 , **{'name' : username})
    if save[1] == passwd : return True
    else : return False

@route('/user/login' , method = 'POST')
def get_signup():
    username = request.forms.get('username')
    passwd = request.forms.get('passwd')
    if check_login(username , passwd):
        # This is the what we want to do
        # 用户的登录账号，在这里可以获取用户的model以进一步操作等等
        return '<p><b>Login successfullly!</b></p>'
    else:
        return '<p><b>Login Failed!</b></p>'

# 用户注销路由
@route('/user/delete' , method = 'POST')
def get_delete():
    username = request.forms.get('username')
    passwd = request.forms.get('passwd')
    if check_login(username , passwd):
        sql.main(9 , **{'name':username})
        return '<p><b>User has been deleted from database!</b></p>'
    else:
        return '<p><b>Password wrong or User wrong , delete user Failed!</p>'

# 用户注册
@route('/user/signup' , method = 'POST')
def get_signup():
    username = request.forms.get('username')
    passwd = request.forms.get('passwd')
    sql.main(2 , **{'name' : username , 'passwd' : passwd})
    return '<p><b>Create login successfully!</b></p>'

'''
爬虫定义数据接收路由
'''
# TODO:这里的记得要加入一个排序处理，排序处理的模块组件写在AI中，这里只是一个中间的处理过程
@route('/spider/website' , method = 'POST')
def get_website_spider():
    import json
    response.set_header('Access-Control-Allow-Origin','*')
    data = eval(request.body.readlines()[0].decode('utf8'))
    name = data['username']
    limit = int(data['limit'])
    # root_url , limit是传递给其他组件模块的参数
    domain = 'http://blog.csdn.net/'
    root_url = domain + name
    # 处理,信息返回
    return json.dumps(website.crawl(root_url , domain , limit) , indent = 4 , ensure_ascii=False , skipkeys = True)

@route('/spider/keyword' , method = 'POST')
def get_keyword_spider():
    import json
    # 这里因为跨域请求的问题，必须要加入该头信息
    response.set_header('Access-Control-Allow-Origin','*')
    data = eval(request.body.readlines()[0].decode('utf8'))
    limit = int(data['limit'])
    # print(data , type(data))
    root_url = 'http://so.csdn.net/so/search/s.do?q=%s&q=%s' % (data['keyword'] , data['keyword'])
    return json.dumps(keyword.crawl(root_url , limit) , indent = 4 , ensure_ascii = False , skipkeys = True)

'''
博文信息管理，删除，评价，博文打开
'''
@route('/blog/delete/<md5url>' , method = 'POST')
def blog_delete(md5url):
    '''
    删除博文，但是不删除对于博文的评价，评价是很重要的信息数据，不能随便的删除
    '''
    import json
    response.set_header('Access-Control-Allow-Origin','*')
    sql.main(10 , **{'md5url' : md5url})
    return json.dumps({'delete': True} , ensure_ascii = False , skipkeys = True)

@route('/blog/batch_delete/<grade:int>')
def blog_batch_delete(grade):
    '''
    批量删除博文接口
    '''
    sql.main(11 , **{'grade' : grade})
    return '<p><b>Batch delete successfully!</b></p>'

@route('/blog/comment' , method = 'POST')
def blog_comment():
    '''
    这里的comment的数据制定了我们对博文的评价成程度
    1,2,3,4,5几个等级
    '''
    import json
    response.set_header('Access-Control-Allow-Origin','*')
    data = eval(request.body.readlines()[0].decode('utf8'))
    sql.main(7 , **{'md5url' : data['md5url'] , 'grade' : data['grade']})
    return json.dumps({'done': True} , ensure_ascii = False , skipkeys = True)

@route('/blog/open/<md5url>')
def blog_open(md5url):
    '''
    该模块返回一个新的富文本博文给用户
    '''
    response.set_header('Access-Control-Allow-Origin','*')
    return sql.main(3 , **{'md5url' :md5url})[0][1].decode('utf8')

# 启动服务器
run(host = '127.0.0.8' , port = 8888)
