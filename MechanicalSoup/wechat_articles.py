#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: 126.py 
@time: 2021/3/7 下午12:59 
@description：TODO
"""

import mechanicalsoup
from faker import Factory

home_url = 'https://weixin.sogou.com/'

# 实例化一个浏览器对象
# user_agent：指定UA
f = Factory.create()
ua = f.user_agent()
# print(ua)
browser = mechanicalsoup.StatefulBrowser(user_agent=ua)

result = browser.open(home_url)

# 获取表单元素
browser.select_form()

# 打印表单摘要
# browser.form.print_summary()

# 根据name属性，填充内容
browser["query"] = "Python"

# 提交
response = browser.submit_selected()

# 调试一下
# 判断是否已经到了搜索结果页面
# browser.launch_browser()


search_results = browser.get_current_page().select('.news-list li .txt-box')

print('搜索结果为:', len(search_results))

# 网页数据爬取
for result in search_results:
    # a标签
    element_a = result.select('a')[0]

    # 获取href值
    # 注意：这里的地址经过调转才是真实的文章地址
    href = "https://mp.weixin.qq.com" + element_a.attrs['href']

    text = element_a.text

    print("标题：", text)
    print("地址:", href)

# 关闭浏览器对象
browser.close()
