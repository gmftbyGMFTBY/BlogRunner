#!/usr/bin/python3

# TODO : 添加修改模块，必要的
import pymysql

# 建立连接
conn = pymysql.connect(host = '127.0.0.1' , port = 3306 , user = 'root' , passwd = 'lt970106' , db = 'fortest' , charset = 'utf8')

# 建立游标
cur = conn.cursor()

def user_read(name = None):
    answer = 'select * from user where '
    if name != None : answer += 'name = "%s"' % name
    else : print('Please input the name for searching')
    cur.execute(answer)
    return cur.fetchone()

def user_write(name = 'NULL' , passwd = 'NULL' , photo = 'NULL' , model = 'NULL'):
    try :
        if name == 'NULL' or passwd == 'NULL' : 
            raise Exception('ERROR for no name or no passwd')
        else:
            answer = 'insert into user(name , passwd , photo , model) values("%s","%s","%s","%s")' % (name , passwd , photo , model)
            cur.execute(answer)
            conn.commit()
    except Exception as e:
        print(e)

def page_read(md5url = None , content = None):
    if md5url == None : print('Please input the url for searching')
    else :
        answer = 'select * from page where '
        answer += 'md5url = "%s"' % md5url
        cur.execute(answer)
        return cur.fetchone()

def page_write(md5url = 'NULL' , content = 'NULL'):
    try :
        if md5url == 'NULL':
            raise Exception('ERROR for no url')
        else:
            answer = 'insert into page(md5url , content) values("%s" , "%s")' % (md5url , content)
            cur.execute(answer)
            conn.commit()
    except Exception as e:
        print(e)

def aifeature_read(md5url = None):
    if md5url == None : print('Please input the url for searching')
    else:
        answer = 'select * from aifeature where md5url = "%s"' % md5url
        cur.execute(answer)
        return cur.fetchone()
        
def aifeature_write(md5url = 'NULL' , size = 0 , number_comment = 0 , number_reader = 0 , grade = 0.0 , analyse_grade = 0.0 , number_like = 0 , number_hate = 0):
    try :
        if md5url == 'NULL' : 
            raise Exception('ERROR for no md5url')
        else:
            answer = 'insert into aifeature(md5url , size , number_comment , number_reader , grade , analyse_grade , number_like , number_hate) values("%s" , %d , %d , %d , %f , %f , %d, %d)' % (md5url, size , number_comment , number_reader , grade , analyse_grade , number_like , number_hate)
            cur.execute(answer)
            conn.commit()
    except Exception as e:
        print(e)

# 该函数提供对数据库操作的统一接口
def main(type_  , **argv):
    '''
    1 - user_read
    2 - user_write
    3 - page_read
    4 - page_write
    5 - aifeature_read
    6 - aifeature_write
    '''
    # 建立连接
    conn = pymysql.connect(host = '127.0.0.1' , port = 3306 , user = 'root' \
            , passwd = 'lt970106' , db = 'fortest' , charset = 'utf8')
    cur = conn.cursor()
    print("数据库和游标建立成功")
    if type_ == 1 : user_read(**argv)
    elif type_ == 2 : user_write(**argv)
    elif type_ == 3 : page_read(**argv)
    elif type_ == 4 : page_write(**argv)
    elif type_ == 5 : aifeature_read(**argv)
    elif type_ == 6 : aifeature_write(**argv)
    cur.close()
    conn.close()
    print("数据库顺利关闭，数据读写成功")

