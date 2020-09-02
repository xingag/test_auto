#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: staticmethod_demo.py 
@time: 2020-08-30 08:42 
@description：staticmethod使用
"""

class Web(object):
    # 静态变量（类变量）
    name = "Python_Web"

    def __init__(self):
        self.desc = "实例属性，不共享"

    def norm_method(self):
        """普通方法"""
        print('普通方法被调用！')

    # 类方法
    @classmethod
    def foo_classmethod_other(cls):
        print('类方法被调用！')

    # 另外一个静态方法
    @staticmethod
    def foo_staticmethod_other():
        print('另外一个静态方法被调用！')

    @staticmethod
    def foo_staticmethod(arg1, arg2):
        print(arg1, arg2)

        # 调用静态变量
        print(Web.name)

        # 调用其他静态方法
        Web.foo_staticmethod_other()

        # 调用类方法
        Web.foo_classmethod_other()

        # 获取实例属性
        print(Web().desc)

        # 调用普通方法
        Web().norm_method()


class Django(Web):
    """子类，继承于Web"""
    pass


if __name__ == '__main__':
    # 1、使用类名去调用静态方法
    Web.foo_staticmethod("Hello", ",AirPython")

    # 不建议使用实例对象去调用静态方法
    # Web().foo_staticmethod("Hello", ",AirPython")

    # 2、子类
    # Django.foo_staticmethod("Hello", ",AirPython")

    # 不建议使用实例对象去调用静态方法
    # Django().foo_staticmethod("Hello", ",AirPython")
