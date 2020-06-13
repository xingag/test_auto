#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: exts.py 
@time: 2020-06-07 09:36 
@description：第三方中间模块，解决模型和App主程序双向循环导入的问题
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
