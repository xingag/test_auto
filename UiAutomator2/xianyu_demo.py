#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: xianyu_demo.py 
@time: 2020-08-17 23:13 
@description：TODO
"""

import uiautomator2 as u2

from uiautomator2_utils import *

PACKAGE_NAME = 'com.taobao.idlefish'

# device = u2.connect_usb('822QEDTL225T7')
device = u2.connect('192.168.0.102')

# 获取屏幕的宽、高度
width, height = device.window_size()

# 打开应用
device.app_start(PACKAGE_NAME, stop=True)

# 隐式等待主界面加载完全
device.implicitly_wait(20)

# 点击到搜索页面
device(resourceId="com.taobao.idlefish:id/search_bg_img_front",).click()

# 输入内容
device.send_keys("Python", clear=True)

# 点击搜索按钮
device(text="搜索").click()

for i in range(5):
    print('滑动一次')
    swipe_custom(device, 0.5, 0.8, 0.5, 0.2, 1.2)


# 停止App
device.app_stop(PACKAGE_NAME)

# 清除App数据
# device.app_clear(PACKAGE_NAME)