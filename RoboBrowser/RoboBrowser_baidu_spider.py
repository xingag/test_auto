#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: baidu_spider.py 
@time: 2021/3/6 下午11:34 
@description：TODO
"""
from time import sleep

from robobrowser import RoboBrowser

home_url = 'https://baidu.com'

#  parser: 解析器，HTML parser; used by BeautifulSoup
#  官方推荐：lxml
rb = RoboBrowser(history=True, parser='lxml')

# 打开目标网站
rb.open(home_url)

sleep(1)

# 找到form表单
bd_form = rb.get_form()

print(bd_form)

bd_form['wd'].value = "AirPython"

# 提交表单，模拟一次搜索
rb.submit_form(bd_form)

sleep(1)


# 查看结果
result_elements = rb.select(".result")

# 搜索结果
search_result = []

# 第一项的链接地址
first_href = ''

for index, element in enumerate(result_elements):
    title = element.find("a").text
    href = element.find("a")['href']
    search_result.append(title)

    if index == 0:
        first_href = element.find("a")
        print('第一项地址为:', href)

print(search_result)

# 跳转到第一个链接
rb.follow_link(first_href)

# 获取历史
print(rb.url)
