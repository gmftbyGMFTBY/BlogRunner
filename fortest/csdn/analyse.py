#!/usr/bin/python3

'''利用BeautifulSoup进行富文本过滤'''

import sys
from bs4 import BeautifulSoup
sys.path.append('../')
from sql import sql

def crawl_sample(filename , ans):
    soup = BeautifulSoup(ans , 'lxml')
    # 提取正文，富文本化
    main = soup.article
    # 提取样本
    feature = {}
    feature['md5url'] = filename
    feature['size'] = len(main.get_text())
    feature['number_like'] = int(soup.find(class_ = 'left_fixed').find(class_ = 'txt').string)
    feature['number_reader'] = int(soup.find(class_ = 'btn-noborder').find(class_ = 'txt').string)
    # feature['number_comment'] = int(soup.find(class_ = 'load_comment').span.string)
    feature['number_hate'] = 0    # 新版本的CSDN好像默认是没有踩的数目的
    # 之后的 grade and analyse_grade 都是用户的添加和我们的自然语言文本分析的结果
    # feaure 存储进入数据库
    sql.main(6 , **feature)
    print('样本入数据库结束')
    noise = main.find_all(class_ = 'article_bar clearfix')[0]
    noise.decompose()    # 删除标签
    ans = '<html><head><meta charset="utf8"></head><body>' + main.prettify() + '</body></html>'
    pages = {'md5url' : filename , 'content' : ans}
    sql.main(4 , **pages)
    print('文本入数据库结束')
