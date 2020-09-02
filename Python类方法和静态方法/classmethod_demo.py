#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: classmethod_demo.py 
@time: 2020-08-30 09:17 
@description：classmethod使用
"""


class Web(object):
    # 静态变量（类变量）
    name = "Python_Web"

    def __init__(self):
        self.desc = "实例属性，不共享"

    def norm_method(self):
        """普通方法"""
        print('普通方法被调用！')
        Web.foo_staticmethod()

    # 静态方法
    @staticmethod
    def foo_staticmethod():
        print('静态方法被调用！')

    # 其他类方法
    @classmethod
    def foo_classmethod_other(cls):
        print('另外一个类方法被调用！')

    # 类方法，第一个参数为cls，代表类本身
    @classmethod
    def foo_classmethod(cls):
        # 打印cls的值查看类型
        # <class '__main__.Web'>
        print(cls)

        # 调用静态变量1（cls.静态变量）
        print(cls.name)

        # 调用静态变量2（类名.静态变量）
        print(Web.name)

        # 调用其他类方法
        cls.foo_classmethod_other()

        # 调用静态方法
        cls.foo_staticmethod()

        # 如果要调用实例属性，必须使用cls实例化一个对象，然后再去引用
        print(cls().desc)

        # 如果要调用普通方法，必须使用cls实例化一个对象，然后再去引用
        cls().norm_method()


class Django(Web):
    """子类"""
    pass


if __name__ == '__main__':
    # 1、使用类名去调用类方法
    # Web.foo_classmethod()

    # 也可以实例化是调用，但是不建议！！！
    # Web().foo_classmethod()

    # ==================================

    # 2、子类去调用类方法
    # Django.foo_classmethod()

    # 也可以实例化是调用，但是不建议！！！
    #
    Django().foo_classmethod()
