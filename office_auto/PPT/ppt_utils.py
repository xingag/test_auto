#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: ppt_utils.py 
@time: 2020-11-14 15:15 
@description：PPT工具类
"""

import math
import os
import random

from PIL import Image
from moviepy.editor import VideoFileClip
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN
from pptx.parts.image import Image
from pptx.shapes.picture import Movie
from pptx.util import Inches, Cm
from pptx.util import Pt


def add_slide(presentation, slide_style_index):
    """
    在PPT文档中，以内置的版式添加幻灯片
    :param presentation:文档对象
    :param slide_style_index:版式索引
    :return:
    """
    # PPT版式样式
    # 内置有11种版式样式
    # 0：Title Slide 标题幻灯片
    # 1：Title and Content  标题和内容
    # 2：Section Header   节标题
    # 3：Two Content   两栏内容
    # 4：Comparison  比较
    # 5：Title Only  仅标题
    # 6：Blank  空白
    # 7：Content with Caption   内容和标题
    # 8：Picture with Caption   图片和标题
    # 9：Title and Vertical Text  标题和竖排内容
    # 10：Vertical Title and Text  竖排标题和文本
    slide_layout = presentation.slide_layouts[slide_style_index]

    # 通过样式Layout，新增一张幻灯片
    slide = presentation.slides.add_slide(slide_layout)

    return slide


def get_slides(presentation):
    """
    获取所有的幻灯片
    :param presentation:
    :return:
    """
    # 所有幻灯片
    slides = presentation.slides

    # 幻灯片数目
    slide_num = len(slides)

    return slides, slide_num


def get_slide(presentation, slide_index):
    """
    根据索引，获取某一个幻灯片
    :param presentation:
    :param slide_index:页面索引，从0开始
    :return:
    """
    slides, slide_num = get_slides(presentation=presentation)

    return slides[slide_index]


def del_slide(presentation, slide_index=0):
    """
    删除某一张幻灯片
    :param presentation:
    :param slide_index: 索引
    :return:
    """
    # 所有幻灯片的列表
    slides = list(presentation.slides._sldIdLst)

    # 根据索引，删除某一张幻灯片
    presentation.slides._sldIdLst.remove(slides[slide_index])


def insert_textbox(slide, left, top, width, height, unit=Inches):
    """
    幻灯片中添加文本框
    :param unit: 单元，默认设置为Inches
    :param slide: 幻灯片对象
    :param left: 左边距
    :param top:  上边距
    :param width: 宽度
    :param height: 高度
    :return:
    """
    # 文本框
    textbox = slide.shapes.add_textbox(left=unit(left),
                                       top=unit(top),
                                       width=unit(width),
                                       height=unit(height))
    # 文本框形状
    tf = textbox.text_frame

    return textbox, tf


def set_widget_bg(widget, bg_rgb_color=None):
    """
    设置【文本框textbox/单元格/形状】的背景颜色
    :param widget:文本框textbox、单元格、形状
    :param bg_rgb_color:背景颜色值
    :return:
    """
    if bg_rgb_color and len(bg_rgb_color) == 3:
        # 1、将形状填充类型设置为纯色
        widget.fill.solid()
        # 2、设置文本框的背景颜色
        widget.fill.fore_color.rgb = RGBColor(bg_rgb_color[0], bg_rgb_color[1], bg_rgb_color[2])


def set_widget_frame(widget, frame_rgb_color=None, frame_width=-1, unit=Cm):
    """
    设置【文本框textbox/单元格/形状】边框样式
    包含：边框颜色、宽度
    :param unit: 默认单位是厘米
    :param widget:文本框textbox/单元格/形状
    :param frame_rgb_color:
    :param frame_width:
    :return:
    """
    if frame_rgb_color and len(frame_rgb_color) == 3:
        widget.line.color.rgb = RGBColor(frame_rgb_color[0], frame_rgb_color[1], frame_rgb_color[2])
    if frame_width > 0:
        widget.line.width = unit(frame_width)


def set_font_style(font, font_name=None, font_color=None, font_size=-1, font_bold=False, font_italic=False):
    """
    设置字体样式
    :param font:
    :param font_name:
    :param font_color:
    :param font_size:
    :param font_bold:
    :param font_italic:
    :return:
    """
    # 字体名称
    if font_name:
        font.name = font_name

    # 字体颜色
    if font_color and len(font_color) == 3:
        font.color.rgb = RGBColor(font_color[0], font_color[1], font_color[2])

    # 字体大小
    if font_size != -1:
        font.size = Pt(font_size)

    # 是否加粗，默认不加粗
    font.bold = font_bold

    # 是否倾斜，默认不倾斜
    font.italic = font_italic


def set_parg_font_style(paragraph, font_name=None, font_color=None, font_size=-1, font_bold=False, font_italic=False,
                        paragraph_alignment=PP_ALIGN.CENTER):
    """
    设置段落中文本的样式，包含：字体名称、颜色、大小、是否加粗、是否斜体
    :param paragraph_alignment: 段落对齐方式
    :param paragraph:
    :param font_name:
    :param font_color:
    :param font_size:
    :param font_bold:
    :param font_italic:
    :return:
    """

    # 对齐方式
    # 注意：对齐方式是针对段落的
    paragraph.alignment = paragraph_alignment

    # 获取段落中字体对象
    font = paragraph.font

    # 设置字体样式
    set_font_style(font, font_name, font_color, font_size, font_bold, font_italic)

    return font
