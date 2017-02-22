import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

yourId = input("准考证号： ")
yourName = input("姓名： ")
print("waiting...")

driver = webdriver.PhantomJS(executable_path='/home/xu/a-project/python/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
driver.get("http://www.chsi.com.cn/cet/query")

zkzh = driver.find_element(By.NAME, "zkzh")
zkzh.clear()
zkzh.send_keys(yourId)
xm = driver.find_element(By.NAME, "xm")
xm.clear()
xm.send_keys(yourName)

driver.find_element(By.ID, "submitCET").click()
time.sleep(2)

print(driver.find_element(By.CLASS_NAME, "m_cnt_m").text)

driver.close()
