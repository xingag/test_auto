#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: proxy_simple.py 
@time: 2020-07-31 22:06 
@description：代理模式
"""

class RealObject(object):
    """
    实际对象
    """
    def __init__(self, arg):
        self.arg = arg

    def foo(self):
        print('参数值为:', self.arg)


class ProxyObject(object):
    """
    代理对象
    """
    def __init__(self, real_object):
        self.real_object = real_object

    def foo(self):
        # 实际对象调用
        self.real_object.foo()


if __name__ == '__main__':
    # 实例化代理对象
    proxy_object = ProxyObject(RealObject('AirPython'))
    proxy_object.foo()
