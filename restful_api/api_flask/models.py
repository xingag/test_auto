#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: models.py 
@time: 2020-06-06 23:33 
@description：模型，对应表结构
"""

from exts import db


class Foo(db.Model):
    """
    模型，将映射到数据库表中
    """
    __tablename__ = 'foo'

    # 主键ID
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    # 名字
    name = db.Column(db.String(100), nullable=False)
    # 年龄
    age = db.Column(db.INTEGER)



