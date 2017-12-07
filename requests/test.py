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

#连接Mysql
db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="Aa123456",db="tbk",charset="utf8")
cursor = db.cursor()

sql = "select orimemberid from shoplink"
cursor.execute(sql)

results = cursor.fetchall()
print results



for orimemberid2 in results:
    orimemberid =  orimemberid2[0]
    #row_list.append(orimemberid.replace("u'", "").replace("'", ""))
    #orimemberid2 = orimemberid.replace("u'", "'", 1)
    url = 'https://pub.alimama.com/common/code/getShopCode.json?orimemberid={}&adzoneid=65078952&siteid=18272447&_input_charset=utf-8'.format(orimemberid)

    print url



# 关闭
cursor.close()


db.close()