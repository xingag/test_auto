#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: urls.py 
@time: 2020-06-05 14:23 
@description：对应App的路由文件
"""

from django.urls import path

from restfulapi import api
from .views import index

urlpatterns = [
    path('', index),
]
