#coding:utf-8
import requests
import re
import json
import MySQLdb
import time
import random
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


#将cookies转换成字典形式，zhihu_cookie为保存的cookie文件，跟程序处在同一路径
def get_cookie():
    with open('/data/tbk/requests/almmck.txt','r') as f:
        cookies={}
        for line in f.read().split(';'):
            name,value=line.strip().split('=',1)  #1代表只分割一次
            cookies[name]=value
        return cookies

s = requests.Session()


#print results

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




url = 'https://pub.alimama.com/common/code/getShopCode.json?orimemberid=1014237390&adzoneid=65078952&siteid=18272447&_input_charset=utf-8'

#url = 'https://pub.alimama.com/common/code/getShopCode.json?orimemberid=2131383559&adzoneid=65078952&siteid=18272447&_input_charset=utf-8'

#2131383559
#url = 'http://pub.alimama.com/myunion.htm'

resp = s.get(url, headers = headers, cookies = get_cookie())
html = resp.content


print html

#a_json = json.loads(html)

#click_url = a_json['data']['clickUrl']

#print  a_json

#print  click_url
#sqla = "insert into shoplink(clickurl) values{} WHERE orimemberid = {}".format(clickurl,orimemberid)

