#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: https://github.com/xingag 
@software: PyCharm 
@file: xlsxwriter_util.py 
@time: 2020/10/24 12:28 
@description：xlsxwriter工具类
"""
from urllib.request import urlopen

import xlsxwriter
from io import BytesIO
import ssl


def create_workbook_and_worksheet(filename, worksheet_names):
    """
    创建工作簿和Sheet
    :param filename: 文件名称
    :param worksheet_names: sheet名称列表
    :return:
    """
    wb = xlsxwriter.Workbook(filename)

    sheets = []

    # 新增sheet
    for worksheet_name in worksheet_names:
        sheets.append(wb.add_worksheet(worksheet_name))

    return wb, sheets


def write_to_cell(sheet, row_index, column_index, value, format_styles=None):
    """
    往单元格中写入数据
    :param row_index: 行索引，1：第一行
    :param column_index: 列索引，1：第一列
    :param format_styles 字体样式
    :return:
    """
    if row_index < 1 or column_index < 1:
        print('参数输入不正确，写入失败！')
    else:
        # 注意：默认xlsxwriter的行索引、列索引从0开始
        sheet.write(row_index - 1, column_index - 1, value, format_styles)


def create_format_styles(wb, format_stuyles):
    """
    创建一个样式，包含：字体大小、字体、颜色、背景、是否加粗等
    :param wb:
    :param format_stuyles:
    :return:
    """
    return wb.add_format(format_stuyles)


def set_column_width(sheet, index_start, index_end, width):
    """
    设置列宽
    :param sheet:
    :param index_start: 开始位置，从1开始
    :param index_end: 结束位置
    :param width: 宽度
    :return:
    """
    # 方式二选一
    # self.current_sheet.set_column('A:C', width)

    # 默认0代表第一列
    sheet.set_column(index_start - 1, index_end - 1, width)


def set_row_height(sheet, row_index, height):
    """
    设置行高
    :param sheet:
    :param row_index: 行索引，从1开始
    :param height:
    :return:
    """
    sheet.set_row(row_index - 1, height)


def create_image_options(x_offset=0, y_offset=0, x_scale=1, y_scale=1, url=None, tip=None, image_data=None,
                         positioning=None):
    """
    插入图片的参数配置
    包含：偏移量、缩放比、网络图片链接、超链接、悬停提示灯
    :param x_offset:
    :param y_offset:
    :param x_scale:
    :param y_scale:
    :param url:
    :param tip:
    :param image_data:
    :param positioning:
    :return:
    """
    image_options = {
        'x_offset': x_offset,
        'y_offset': y_offset,
        'x_scale': x_scale,
        'y_scale': y_scale,
        'url': url,
        'tip': tip,
        'image_data': image_data,
        'positioning': positioning,
    }
    return image_options


def get_image_data_from_network(url):
    """
    获取网络图片字节流
    :param url: 图片地址
    :return:
    """
    ssl._create_default_https_context = ssl._create_unverified_context
    # 获取网络图片的字节流
    image_data = BytesIO(urlopen(url).read())
    return image_data


def insert_local_image(sheet, row_index, column_index, filepath, image_options=None):
    """
    单元格中插入图片
    :param sheet:
    :param row_index: 行索引，从1开始
    :param column_index: 列索引，从1开始
    :param filepath:
    :param image_options:
    :return:
    """
    if row_index < 1 or column_index < 1:
        return "参数输入有误，插入失败！"

    # 二选一
    # self.current_sheet.insert_image('B2', '1.png')
    # self.current_sheet.insert_image('M2', '1.png', image_options)

    # 插入图片
    sheet.insert_image(row_index - 1, column_index - 1, filepath, image_options)


def insert_network_image(sheet, row_index, column_index, url, filepath, image_options=None):
    """
    插入网络图片
    :param sheet:
    :param row_index:
    :param column_index:
    :param url:
    :param filepath:
    :param image_options:
    :return:
    """
    if row_index < 1 or column_index < 1:
        return "参数输入有误，插入失败！"

    # 获取图片字节流
    image_data = get_image_data_from_network(url)

    if image_options:
        image_options['image_data'] = image_data
    print(image_options)

    sheet.insert_image(row_index - 1, column_index - 1, filepath, image_options)
