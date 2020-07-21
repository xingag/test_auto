#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: test_get_level.py 
@time: 2020-07-18 21:57 
@description：单元测试
"""

import unittest

from main import *


class GetLevel(unittest.TestCase):

    def test_get_level1(self):
        self.assertEquals(get_level(90), "优秀")

    def test_get_level2(self):
        self.assertEquals(get_level(80), "良好")


if __name__ == '__main__':
    unittest.main(verbosity=2)
