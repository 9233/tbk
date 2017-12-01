#coding:utf-8
import requests
import re
import json
import MySQLdb
import time




#连接Mysql
conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="Aa123456",db="tbk",charset="utf8")
cursor = conn.cursor()

#写入
sql = "insert into shoplink(shoptitle,clickurl,commanrate) values(%s,%s,%s)"
param = ("三只松鼠旗舰店","http://taobao.com","15")
n = cursor.execute(sql,param)

# 关闭
cursor.close()
conn.close()

