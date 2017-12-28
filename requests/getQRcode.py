#coding:utf-8
import requests
import re
import json
import MySQLdb
import time
import random

import top.api


import sys
reload(sys)
sys.setdefaultencoding("utf-8")





str1 =  "宁美国度官方旗舰店"


# get clickurl


db=MySQLdb.connect(host="127.0.0.1",user="root",passwd="Aa123456",db="tbk",charset="utf8")
cursor = db.cursor()




sql1 = "select orimemberid from ShopClickUrl where shoptitle = '%s'" % (str1)



cursor.execute(sql1)

results = cursor.fetchall()

orimemberid =  results[0][0]

#get clickurl

sql2 = "select clickurl from temp where orimemberid = '%s'" % (orimemberid)
cursor.execute(sql2)
results = cursor.fetchall()

clickurl = results[0][0]

print clickurl


#clickurl = "https://s.click.taobao.com/t?e=m%3D2%26s%3Ds1NlGAGqXSMcQipKwQzePDAVflQIoZepK7Vc7tFgwiFRAdhuF14FMX5ZAdEbDQilxq3IhSJN6GSit1vIFTntupRCEODG4lLh4oIuQQHrCak1MsId7xyTi4mbOeFA9oWQcSpj5qSCmbA%3D"
#get QRcode

req = top.api.TbkTpwdCreateRequest()

req.set_app_info(top.appinfo("23497210", "ff184386a02de8767f761910f18df4b8"))

#req.user_id = "123"
req.text = str1
req.url = clickurl
#req.logo = "https://uland.taobao.com/"
#req.ext = "{}"
try:
    resp = req.getResponse()

    #print resp

    print resp['tbk_tpwd_create_response']['data']['model']


except Exception, e:
    print(e)

