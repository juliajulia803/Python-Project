# -*- coding: utf-8 -*-
from selenium import webdriver
import time

username="a1073352"
password="12345678"

path="./driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://aca.nuk.edu.tw/Student2/login.asp")
time.sleep(0.5)
email_in = driver.find_element_by_xpath('//*[@name="Account"]')
email_in.send_keys(username)
time.sleep(0.5)
password_in = driver.find_element_by_xpath('//*[@name="Password"]')
password_in.send_keys(password)
time.sleep(0.5)
login_btn = driver.find_element_by_xpath('//*[@value="登　　入"]')
login_btn.click()
time.sleep(3)
print(driver.page_source)
# driver.get("https://m.facebook.com")
# for i in range(5):
#     time.sleep(1.5)
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')#一次滑一頁
# time.sleep(20)