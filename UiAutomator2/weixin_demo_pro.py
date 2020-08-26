#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: weixin_demo.py 
@time: 2020-08-18 21:57 
@description：微信
"""

import uiautomator2 as u2
from loguru import logger

from uiautomator2_utils import *

# 微信App的包名
PACKAGE_NAME = 'com.tencent.mm'


class WeiXin(object):

    def __init__(self):
        # 通过设备ip地址，连接设备
        self.device = u2.connect('192.168.0.101')

        # 获取屏幕的宽、高度
        self.width, self.height = self.device.window_size()

        # 每一条消息的高度
        self.msg_height = 0

    def run(self):
        # 打开应用
        self.__start()

        # 等待主页面完全加载
        self.__wait_home_appear()

        # 处理未读信息
        self.__handle_msg()

    def __start(self):
        """
        打开应用
        :return:
        """
        # 利用应用包名打开App
        self.device.app_start(PACKAGE_NAME, stop=True)

    def __has_unread_msg(self):
        """
        是否有未读的消息
        :return:
        """
        try:
            number_unread_msg = self.device(resourceId='com.tencent.mm:id/gik')
            return number_unread_msg.get_text() != ""
        except Exception:
            return False

    def __is_number(self, str):
        """
        判断是否为整数
        :param str:
        :return:
        """
        try:
            x = int(str)
            return isinstance(x, int)
        except ValueError:
            return False

    def __wait_home_appear(self):
        """
        等待主页加载完成
        :return:
        """
        self.device(resourceId='com.tencent.mm:id/cns', text='微信').wait(timeout=20)
        self.device(resourceId='com.tencent.mm:id/cns', text='通讯录').wait(timeout=20)
        self.device(resourceId='com.tencent.mm:id/cns', text='发现').wait(timeout=20)
        self.device(resourceId='com.tencent.mm:id/cns', text='发现').wait(timeout=20)
        print('首页加载完成')

    def __is_home_page(self):
        """主页"""
        element_tab1 = self.device(resourceId='com.tencent.mm:id/cns', text='微信')
        element_tab2 = self.device(resourceId='com.tencent.mm:id/cns', text='通讯录')
        element_tab3 = self.device(resourceId='com.tencent.mm:id/cns', text='发现')
        element_tab4 = self.device(resourceId='com.tencent.mm:id/cns', text='发现')

        return element_tab1.exists and element_tab2.exists and element_tab3.exists and element_tab4.exists

    def __handle_msg(self):
        """
        处理消息，模拟查看消息
        :return:
        """
        while True:
            if self.__has_unread_msg():
                # 定位到要处理的消息
                element = self.device(resourceId='com.tencent.mm:id/gik')
                click_twice_quickly(self.device, element)

                # 对界面要处理的元素进行处理
                # 如果存在，就执行点击操作
                # instance=0：获取第一个控件
                element = self.device(resourceId='com.tencent.mm:id/ga3', instance=0)

                if element.exists and self.__is_number(element.get_text()):
                    logger.debug(element.get_text())
                    element.click()
                    if not self.__is_home_page():
                        # 返回到主页面
                        self.device.press('back')
            else:
                logger.debug('没有可读的消息了，退出！')
                break


if __name__ == '__main__':
    wx = WeiXin()
    wx.run()
