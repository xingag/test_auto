#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: https://github.com/xingag 
@software: PyCharm 
@file: Font.py 
@time: 2020/11/5 20:20 
@description：字体样式，包含：大小、字体名称、是否粗体、斜体、下划线、颜色等
"""
from docx.text.paragraph import Paragraph
from docx.text.run import Run
from docx.shared import Pt
from docx.shared import RGBColor


class FontRun():

    def __init__(self, paragraph, content):
        self.paragraph = paragraph
        self.run = paragraph.add_run(content)

    def set_font_name(self, font_name):
        """
        设置字体名称
        :param font_name: 'Times New Roman'
        :return:
        """
        self.run.font.name = font_name
        return self

    def set_font_color(self, font_color_array):
        """
        字体颜色
        :param font_color_array: 比如：[0xff,0x00,0x00]
        :return:
        """
        self.run.font.color.rgb = RGBColor(font_color_array[0], font_color_array[1], font_color_array[2])
        return self

    def set_font_size(self, font_size):
        """
        设置字体大小
        """
        self.run.font.size = Pt(font_size)
        return self

    def set_italic(self, italic):
        """
        是否斜体
        :param italic:
        :return:
        """
        self.run.italic = italic
        return self

    def set_bold(self, bold):
        """
        是否加粗
        :param bold:
        :return:
        """
        self.run.bold = bold
        return self

    def set_underline(self, underline):
        """
        是否带有下滑线
        :param underline:
        :return:
        """
        self.run.underline = underline
        return self
