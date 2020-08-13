#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: xag
@license: Apache Licence
@contact: xinganguo@gmail.com
@site: https://www.jianshu.com/u/f3b476549169
@software: PyCharm
@file: element_util.py
@time: 2019-10-02 11:54
@description：元素工具类
"""

import re
import xml.etree.ElementTree as ET
from time import sleep

from utils.cmd_util import *


def save_ui_tree_to_local(dName):
    """
    获取当前Activity控件树，保存到本地
    文件名固定为：uidump.xml
    :param dName: 设备id
    :return:
    """
    
    exec_cmd("adb  -s %s shell uiautomator dump /data/local/tmp/%s.xml" % (dName, dName))

    sleep(2)

    exec_cmd("adb -s %s pull /data/local/tmp/%s.xml ./../" % (dName, dName))


def get_element_position(element_id, uidump_name):
    """
    通过元素的id，使用ElementTree，解析元素控件树，查找元素的坐标中心点
    :param element_id: 元素id，比如：
    :return: 元素坐标
    """

    # 解析XML
    tree = ET.parse('./../%s.xml' % uidump_name)
    root = tree.getroot()

    # 待查找的元素
    result_element = None

    # print('查找数目', len(root.findall('.//node')))

    # 遍历查找node元素
    # 通过元素id
    for node_element in root.findall('.//node'):
        if node_element.attrib['resource-id'] == element_id:
            result_element = node_element
            break

    # 如果找不到元素，直接返回空
    if result_element is None:
        print('抱歉！找不到元素！')
        return None

    # 解析数据
    coord = re.compile(r"\d+").findall(result_element.attrib['bounds'])

    # 中心点坐标
    position_center = int((int(coord[0]) + int(coord[2])) / 2), int((int(coord[1]) + int(coord[3])) / 2)

    return position_center
