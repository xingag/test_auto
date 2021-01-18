#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: test_pytest.py 
@time: 2021-01-16 10:39 
@description：pytest中使用mock
"""

import pytest

from pytest_mock_.product_impl import Product


def test_buy_product_success(mocker):
    """
    购买成功Mock
    :param mocker:
    :return:
    """
    # 实例化一个产品对象
    product = Product()

    # 对Product中的方法的返回值进行Mock
    mock_value = {"id": 1, "name": "苹果", "num": 23}

    # Mock方法
    # 注意：需要指定方法的完整路径
    # mocker.patch 的第一个参数必须是模拟对象的完整路径，第二个参数用来指定返回值
    product.get_product_status_by_id = mocker.patch("product_impl.Product.get_product_status_by_id",
                                                    return_value=mock_value)

    # 调用购买产品的方法
    result = product.buy_product(1)

    assert result.get("status") == 0


def test_buy_product_fail(mocker):
    """
    购买失败Mock
    :param mocker:
    :return:
    """
    product = Product()

    mock_value = {"id": 2, "name": "香蕉", "num": 0}

    product.get_product_status_by_id = mocker.patch("product_impl.Product.get_product_status_by_id",
                                                    return_value=mock_value)

    result = product.buy_product(1)

    assert result.get("status") == 0, result.get("msg")


if __name__ == '__main__':
    pytest.main()
