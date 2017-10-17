#!/usr/bin/python3

import pymysql

conn = pymysql.connect(host = '127.0.0.1' , port = 3306 ,\
        user = 'root' , passwd = 'lt970106' , db = 'shadow'\
        , charset = 'utf8')

cur = conn.cursor()



