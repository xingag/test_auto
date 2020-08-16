# !/usr/bin/env python
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: 公众号：AirPython
@software: PyCharm 
@file: 126_email_helium.py 
@time: 2020-08-12 22:53 
@description：使用Helium登录126邮箱
"""

import helium
from helium import *
from time import sleep

home_url = 'https://mail.126.com/'
username = 'AirPython'
password = '**'

# 打开主页
# 注意：返回一个driver，同样可以使用selenium的API
driver = start_chrome(home_url)

# 所有的属性及方法
print('helium所有属性及方法:\n', helium.__all__, '\n')

# 等待元素加载完成
wait_until(Text("你的专业电子邮局").exists)
print('首页加载完成！')

# 不需要切换iframe，直接输入
write(username,TextField('邮箱帐号或手机号码'))
write(password,TextField('输入密码'))

# 模拟点击Enter键登录
press(ENTER)

wait_until(Text('收 信').exists)

# 点击收件箱
click(Text('收 信'))

# 退出
sleep(10)

# 关闭浏览器
kill_browser()

