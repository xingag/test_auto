#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: step.py 
@time: 2020-06-03 12:47 
@description：测试用例
"""
from time import sleep
from selenium.webdriver.common.keys import Keys
from behave import *

# 欢迎关注公众号：AirPython


@given(u'搜索框输入一个关键字 {keyword}')
def step_impl(context, keyword):
    element_input = context.driver.find_element_by_name('q')
    element_input.clear()
    print("准备输入")
    element_input.send_keys(keyword)


@when(u'点击搜索按钮')
def step_impl(context):
    # 模拟Enter键
    context.driver.find_element_by_name("q").send_keys(Keys.ENTER)

    sleep(1)


@then(u'页面标题应该为 {title}')
def step_impl(context, title):
    assert context.driver.title == title


# 运行
# behave --lang=zh-CN
# behave --lang=zh-CN -f json.pretty -o './test_report.json'