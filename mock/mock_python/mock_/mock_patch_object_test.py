#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: mock_test.py 
@time: 2021-01-16 12:40 
@description：@patch.object
"""

from mock import patch

from mock_.product_impl import Product

# 安装依赖
# pip3 install mock


# Mock一个方法
# @patch.object：对象、方法名
@patch.object(Product, 'get_product_status_by_id')
def test_succuse(mock_get_product_status_by_id):
    # Mock方法，指定一个返回值
    mock_get_product_status_by_id.return_value = {"id": 1, "name": "苹果", "num": 23}

    product = Product()

    assert product.buy_product(1).get("status") == 0


@patch.object(Product, 'get_product_status_by_id')
def test_fail(mock_get_product_status_by_id):
    # Mock方法，指定一个返回值
    mock_get_product_status_by_id.return_value = {"id": 2, "name": "香蕉", "num": 0}

    product = Product()

    assert product.buy_product(1).get("status") == 1
