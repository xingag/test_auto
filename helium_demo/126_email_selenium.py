#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: 126_email_selenium.py 
@time: 2020-08-12 22:52 
@description：使用Selenium登录126邮箱
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# 账号信息
home_url = 'https://mail.126.com/'
username = 'AirPython'
password = '**'

# 实例化Driver
driver = webdriver.Chrome()
# 隐式等待10s
driver.implicitly_wait(10)
# 打开主页面
driver.get(home_url)

# 显示等待打开主页面
wait = WebDriverWait(driver, 10, 0.5)

# 切换到对应的iframe，否则无法操作内部元素
wait.until(
    EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath('//iframe[contains(@id,"x-URS-iframe")]')))

# 用户名输入框
element_input = wait.until(EC.visibility_of(driver.find_element_by_xpath('//input[@name="email"]')))
element_input.clear()
element_input.send_keys(username)

# 密码输入框
element_password = wait.until(EC.visibility_of(driver.find_element_by_xpath('//input[@name="password"]')))
element_password.clear()
element_password.send_keys(password)

# 登录按钮
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id="dologin"]'))).click()

# 找一个登录成功的页面元素
# 通过元素属性+元素值来唯一定位元素
result = True
try:
    element_recy_email = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="oz0" and contains(text(),"收 信")]')))
    if element_recy_email:
        result = True
    else:
        result = False
except Exception as e:
    result = False

print("邮箱登陆成功" if result else "邮箱登录失败")


# 退出
sleep(10)
driver.quit()