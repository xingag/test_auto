#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top
@software: PyCharm 
@file: exec_api.py 
@time: 2020-07-17 11:20 
@description：Coverage 调用API
"""

import coverage
import unittest

# 公众号：AirPython

# 实例化一个对象
cov = coverage.coverage()
cov.start()

# 测试套件
suite = unittest.defaultTestLoader.discover("./", "test_get_level.py")
unittest.TextTestRunner().run(suite)


# 结束分析
cov.stop()

# 结果保存
cov.save()

# 命令行模式展示结果
cov.report()

# 生成HTML覆盖率报告
cov.html_report(directory='result_html')
