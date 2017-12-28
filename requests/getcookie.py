#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import random
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


m = PyMouse()
k = PyKeyboard()
#profile = webdriver.FirefoxProfile('/root/.mozilla/firefox/s8uj541j.default')

#打开本机火狐浏览器，输入登录地址
profile = webdriver.FirefoxProfile('/home/android/.mozilla/firefox/1lhpjrv7.default')
driver = webdriver.Firefox(profile)
time.sleep(random.randint(2, 5))
driver.get('https://login.taobao.com/member/login.jhtml?style=minisimple&from=alimama&disableQuickLogin=true')
time.sleep(random.randint(2, 5))

#输入用户名：
#driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/span[1]/input').click()
#driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/span[1]/input').clear()
#driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/span[1]/input').send_keys('聚跑团')


#输入密码
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/span[1]/input').click()
time.sleep(random.randint(2, 5))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/span[1]/input').send_keys('Nosecret521')
time.sleep(random.randint(2, 5))
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/span[1]/input').send_keys(Keys.RETURN)
time.sleep(random.randint(15, 35))


currurl=driver.current_url
if currurl=='https://www.alimama.com/index.htm':
    print 'login success'
    cookies = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookies)
    #f=file("/root/weixin.11tn.com/mp/almmck.txt","w+")
    f = file("/data/tbk/requests/almmck.txt", "w+")
    f.writelines(cookiestr)
    f.close()
    time.sleep(random.randint(60, 80))
    driver.quit()
else:
    #登录失败，需要模拟拖动滑块验证
    print 'login fail'
    time.sleep(random.randint(7, 15))
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/span[1]/input').click()
    time.sleep(random.randint(2, 5))
    #driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/span[1]/input').send_keys('Nosecret521')
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/span[1]/input').send_keys('Nosecret521')
    time.sleep(random.randint(2, 5))
    #place of huakuaier
    m.move(494,296)
    time.sleep(random.randint(2, 5))
    m.drag(710,296)
    time.sleep(random.randint(7, 15))
    m.release(710,296,1)
    time.sleep(random.randint(7, 15))
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/form/div[2]/span[1]/input').send_keys(Keys.RETURN)
    time.sleep(random.randint(7, 15))
    cookies = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookies)
    #f=file("/root/weixin.11tn.com/mp/almmck.txt","w+")
    f = file("/data/tbk/requests/almmck.txt", "w+")
    f.writelines(cookiestr)
    #print currurl
    f.close()
    #driver.save_screenshot("3.png")
    time.sleep(random.randint(10, 60))
    driver.quit()