#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: main.py 
@time: 2020-07-18 21:47 
@description：被测代码
"""


def get_level(cource):
    """
    自定义的方法
    :param cource:成绩
    :return:
    """
    if cource >= 90:
        return "优秀"
    elif cource >= 80:
        return "良好"
    elif cource >= 60:
        return "合格"
    elif cource >= 40:
        return "不合格"
    else:
        return "差"
