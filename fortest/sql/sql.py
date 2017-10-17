#!/usr/bin/python3

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

if __name__ == "__main__" :
    # test for user read
    #    print(user_read(name = 'xuhengda'))
    # test for user write
    #    print(user_write(name = 'lantian',passwd = 'wanggeyuan' , model = "xuehngda"))
    # test for page read
    #    print(page_read('lantian'))
    # test for page write
    #    print(page_write(md5url = 'xuhengda'))
    # test for aifeature read
    #    print(aifeature_read('lantian'))
    # test for aifeature wrie
    #    print(aifeature_write('wanggeyuan' , size = 12 , number_like = 1))
