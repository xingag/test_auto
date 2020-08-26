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


def swipe_up_special(device, distance):
    """
    向上滑动固定的距离
    :return:
    """
    # 获取屏幕的宽、高度
    width, height = device.window_size()
    device.swipe(width / 2, 1400, width / 2, 1600 - distance, 1000)


def get_widget_height(device, id):
    """
    获取控件的高度
    :param device:
    :param id:
    :return:
    """
    element = device(resourceId=id, instance=0)
    bounds = element.bounds()
    # print(bounds)
    # 高度
    height = bounds[3] - bounds[1]
    return height


def get_widget_center_position(device, id):
    """
    获取控件的中心点坐标
    :param device:
    :param id:
    :return:
    """
    element = device(resourceId=id, instance=0)
    bounds = element.bounds()

    return (bounds[2] - bounds[0] / 2, bounds[3] - bounds[1] / 2)


def click_twice_quickly(device, element):
    """
    快读点击两下
    :param device:
    :param id: 控件ID
    :return:
    """
    bounds = element.bounds()

    center_x, center_y = ((bounds[2] + bounds[0]) / 2, ((bounds[3] + bounds[1]) / 2))
    print(center_x,center_y)
    device.double_click(center_x, center_y, 0.05)
