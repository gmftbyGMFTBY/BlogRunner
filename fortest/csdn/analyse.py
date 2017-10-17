#!/usr/bin/python3

'''利用BeautifulSoup进行富文本过滤'''

import sys
from bs4 import BeautifulSoup
# filename = sys.argv[1:]
filename = sys.argv[1]

with open('/home/lantian/fortest/raw/' + filename) as f:
    ans = f.read()

soup = BeautifulSoup(ans , 'lxml')
main = soup.article
noise = main.find_all(class_ = 'article_bar clearfix')[0]
noise.decompose()    # 删除标签
'''
for i in main.stripped_strings:
    print(i)
'''

ans = '<html><head><meta charset="utf8"></head><body>' + main.prettify() + '</body></html>'
with open('./content/filename' + '.html' , 'w') as f:
    f.write(ans)


