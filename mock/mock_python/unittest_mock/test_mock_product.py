#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: test_mock_product.py 
@time: 2021-01-16 15:53 
@description：unittest中使用mock
"""

import unittest
from unittest import mock

from unittest_mock.product_impl import Product


class TestProduct(unittest.TestCase):

    def test_success(self):
        # 成功结果
        mock_success_value = {"id": 1, "name": "苹果", "num": 23}

        product = Product()

        product.get_product_status_by_id = mock.Mock(return_value=mock_success_value)

        # 调用实际函数
        assert product.buy_product(1).get("status") == 0

    def test_fail(self):
        # 失败结果
        mock_success_value = {"id": 1, "name": "苹果", "num": 0}

        product = Product()

        product.get_product_status_by_id = mock.Mock(return_value=mock_success_value)

        # 调用实际函数
        assert product.buy_product(1).get("status") == 1



if __name__ == "__main__":
    unittest.main()
