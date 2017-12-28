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

clickurl = 'http://taobao.com'

sql = """
INSERT INTO shoplink (clickurl)   
SELECT @clickurl FROM shoplink 
    WHERE NOT EXISTS(  
        SELECT orimemberid   
        FROM shoplink   
        WHERE clickurl=@clickurl)
        """

#user_id = "http://taobao.com"
#password = "31536383"

#cursor.execute("INSERT INTO shoplink(clickurl) VALUES('http://taobao.com') WHERE orimemberid = '880734502'")

#cursor.execute('insert into shoplink(clickurl) values("%s") WHERE orimemberid = "%s"'% (user_id,password))


#sqla = "insert into shoplink(clickurl) values ('http://taobao.com') where orimemberid = '31536383'"



#results = cursor.fetchall()

cursor.execute(sql)
db.commit()


time.sleep(random.randint(20, 50))

# param = (clickurl,orimemberid)

# cursor.execute(sql,param)


# 关闭
cursor.close()



db.close()