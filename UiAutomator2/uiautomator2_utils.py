#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: uiautomator2_utils.py 
@time: 2020-08-17 23:32 
@description：工具类
"""

from time import sleep


def swipe_up(device):
    """
    向上滑动
    :param device:
    :return:
    """
    device.swipe_ext("up")


def swipe_down(device):
    """
    向下滑动
    :param device:
    :return:
    """
    device.swipe_ext("down")


def swipe_left(device):
    """
    往左滑动
    :param device:
    :return:
    """
    device.swipe_ext("left")


def swipe_right(device):
    """
    往右滑动
    :param device:
    :return:
    """
    device.swipe_ext("right")


def swipe_custom(device, start_x_percent, start_y_percent, end_x_percent, end_y_percent, during=1.0, interval=1):
    """
    自定义滑动，适配性更高
    :param device:
    :param start_x_percent:
    :param start_y_percent:
    :param end_x_percent:
    :param end_y_percent:
    :param during:
    :return:
    """
    # 获取屏幕的宽、高度
    width, height = device.window_size()
    device.swipe(start_x_percent * width, start_y_percent * height, end_x_percent * width, end_y_percent * height,
                 during)

    if interval > 0:
        sleep(interval)

