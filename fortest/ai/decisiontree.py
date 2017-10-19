#!/usr/bin/python3

import sys
sys.path.append('..')
import sql.sql as sql    # 导入数据库存储模块

def load_data():
    '''
    该函数从数据库中抽取所有的样本空间数据，将信息规整病返还给监督学习组件去学习
    '''
    save = sql.main(5)    # 获取全部的样本信息
    label = [i[4] for i in save]     # label
    # data
    data = []
    for i in save:
        p = i[0:4] + i[5:]
        data.append(p)
    return data , label

def calShannoneEnt():
    pass

if __name__ == "__main__":
    load_data()



