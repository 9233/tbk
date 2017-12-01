#coding:utf-8
import requests
import re
import json
import MySQLdb
import time
import random


#将cookies转换成字典形式，zhihu_cookie为保存的cookie文件，跟程序处在同一路径
def get_cookie():
    with open('/data/tbk/requests/almmck.txt','r') as f:
        cookies={}
        for line in f.read().split(';'):
            name,value=line.strip().split('=',1)  #1代表只分割一次
            cookies[name]=value
        return cookies

s = requests.Session()
url = 'http://pub.alimama.com/shopsearch/shopList.json?q=%E6%97%97%E8%88%B0%E5%BA%97&toPage=1&perPagesize=100&_input_charset=utf-8'
headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.5',

    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'pub.alimama.com',
    'Referer': 'http://pub.alimama.com/myunion.htm',

    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'X-Requested-With': 'XMLHttpRequest'
    }

resp = s.get(url, headers = headers, cookies = get_cookie())
html = resp.content

print html

time.sleep(random.randint(2, 5))

#连接Mysql
conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="Aa123456",db="tbk",charset="utf8")
cursor = conn.cursor()

#写入
sql = "insert into shoplink(shtoptitle,clickurl,commanrate) values(%s,%s,%s)"
param = ("三只松鼠旗舰店","http://taobao.com","15.00")
n = cursor.execute(sql,param)

# 关闭
cursor.close()
conn.close()