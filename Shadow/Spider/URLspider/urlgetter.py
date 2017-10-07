#!/usr/bin/python3

import requests
import chardet

def getter(url):
    '''
    Input :
        string : url
    Output :
        a long UTF8 string of the result HTML
    '''
    try :
        user_agent = {'User_Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        f = requests.get( url , user_agent)
        f.encoding = chardet.detect(f.content)['encoding']
        return f.text
    except Exception as e:
        print('There is something wrong!')
        print(e)

if __name__ == "__main__":
    # this is code is only for the test
    # next two code try to solve the problem of the coding with the utf8
    # the print function has the wrong coding , change it into utf8 will be OK
    print(getter('http://www.baidu.com'))
