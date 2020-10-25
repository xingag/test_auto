#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: https://github.com/xingag 
@software: PyCharm 
@file: demo.py 
@time: 2020/10/20 19:25 
@description：使用xlrd、xlwt处理Excel文件
"""

import xlwt
import xlrd
from xlutils.copy import copy


# 依赖
# pip3 install xlrd
# pip3 install xlwt
# pip3 install xlutils


class ExcelF(object):

    def __init__(self):
        # 标题栏
        self.titles = ["姓名", "年龄"]
        # 值
        self.values = [["xag", 23], ["xinag", 18], ["星安果", 19], ["张三", 30], ["李四", 40]]

        self.file_path = './output.xls'

    def start(self):
        # 1、将数据写入到一个Excel中
        # self.write_to_excel_file(self.file_path)

        # 2、读取Excel文件数据
        # self.read_from_excel_file(self.file_path)

        # 3、修改Excel文件数据
        # self.modify_excel_file(self.file_path)

        # 4、进阶用法
        self.advance_use(self.file_path)

    def write_to_excel_file(self, filepath):
        """
        使用xlwt依赖，将数据写入到Excel文件中
        :return:
        """
        sheetname = '第一个Sheet'

        # 创建一个工作簿对象
        wb = xlwt.Workbook()

        # 添加Sheet，通过sheet名称
        sheet = wb.add_sheet(sheetname)

        # 将数据写入到Sheet中
        # 3个参数分别是：行索引（从0开始）、列索引（从0开始）、单元格的值
        # 第一行第一列，写入一个数据
        # 写入标题
        for index, title in enumerate(self.titles):
            sheet.write(0, index, title)

        # 写入值
        for index_row, row_values in enumerate(self.values):
            for index_column, column_value in enumerate(row_values):
                sheet.write(index_row + 1, index_column, column_value)

        # 保存文件
        # 最后保存文件即可
        wb.save(filepath)

    def read_from_excel_file(self, file_path):
        """
        使用xlrd读取本地Excel文档
        :return:
        """
        # 打开文件，返回一个工作簿对象
        wb = xlrd.open_workbook(file_path)

        # 统计sheet数量
        sheets_num, sheets_names = wb.nsheets, wb.sheet_names()
        print('sheet数量一共有:', sheets_num)
        print('sheet名称分别为:', sheets_names)

        # 获取某一个sheet
        # 通过名称或者索引获取
        sheet = wb.sheet_by_index(0)
        # sheet = wb.sheet_by_name('第一个Sheet')
        print(sheet)

        # 获取某一个sheet中，包含的行数量、列数量
        sheet_name, sheet_row_count, sheet_column_count = sheet.name, sheet.nrows, sheet.ncols
        print('当前sheet名称为:', sheet_name, ",一共有：", sheet_row_count, "行；有：", sheet_column_count, "列")

        # 单独获取某一行数据，索引从0开始
        # 比如：获取第2行数据
        row_datas = sheet.row_values(1)
        print('第2行数据为：', row_datas)

        # 单独获取某一列数据，索引从0开始
        # 比如：获取第二列数据
        column_datas = sheet.col_values(1)
        print('第2列数据为：', column_datas)

        # 获取某一个单元格的数据
        # 比如：获取第2行第1列的单元格的数据
        one_cell = sheet.cell(1, 0)
        # 值
        cell_value = one_cell.value
        print("单元格的值为:", cell_value)
        # 单元格数据类型
        cell_type = one_cell.ctype
        print("单元格数据类型为:", cell_type)

        # 数据类型参考
        # 0	empty	空
        # 1	string	字符串
        # 2	number	数字
        # 3	date	日期
        # 4	boolean	布尔值
        # 5	error	错误

        # 获取所有单元格的值
        print('表格中所有数据如下：')
        for r in range(sheet.nrows):
            for i in range(sheet.ncols):
                print(sheet.cell(r, i).value)

    def modify_excel_file(self, file_path):
        """
        使用xlutils修改Excel文件数据
        :param file_path:
        :return:
        """
        # 打开文件
        wb = xlrd.open_workbook(file_path)

        # 复制一份
        wb_copy = copy(wb)

        # 选择一个待修改的sheet
        sheet = wb_copy.get_sheet(0)

        # 直接通过行索引、列索引，往单元格中写入数据
        # 比如：修改第2行第1列的数据为AirPython
        sheet.write(1, 0, 'AirPython1')

        # 保存并覆盖
        wb_copy.save(file_path)

        print('修改成功！')

    def advance_use(self, file_path):
        """
        进阶用法
        :return:
        """
        # 注意：必须设置formatting_info=True，才能正常获取属性
        wb = xlrd.open_workbook(file_path, formatting_info=True)
        sheet = wb.sheet_by_index(0)

        # 1、获取所有可看见的sheet
        sheet_visiable = self.get_all_visiable_sheets(wb)
        print('所有可见的sheet包含：', sheet_visiable)

        # 2、获取单元格的字体颜色及背景颜色
        cell_property = self.get_cell_bg_color(wb, sheet, 0, 0)
        print(cell_property)

        # 3、获取某一个sheet中，可见的行和列
        row_visiable = self.get_all_visiable_rows(sheet)
        column_visiable = self.get_all_visiable_columns(sheet)
        print('所以看见的行包含：', row_visiable)
        print('所以看见的列包含：', column_visiable)

    def get_all_visiable_rows(self, sheet):
        """
        获取某一个sheet中，可见的行
        :param sheet:
        :return:
        """
        result = [index for index in range(sheet.nrows) if sheet.rowinfo_map[index].hidden == 0]
        return result

    def get_all_visiable_columns(self, sheet):
        """
        获取某一个sheet中，可见的列
        :param sheet:
        :return:
        """
        result = [index for index in range(sheet.ncols) if sheet.colinfo_map[index].hidden == 0]
        return result

    def get_all_visiable_sheets(self, wb):
        """
        获取所有可见的sheet
        :param wb:
        :return:
        """
        return list(filter(lambda item: item.visibility == 0, wb.sheets()))

    def get_cell_bg_color(self, wb, sheet, row_index, col_index):
        """
        获取某一个单元格的背景颜色
        :param wb:
        :param sheet:
        :param row_index:
        :param col_index:
        :return:
        """
        xfx = sheet.cell_xf_index(row_index, col_index)
        xf = wb.xf_list[xfx]

        # 字体颜色
        font_color = wb.font_list[xf.font_index].colour_index
        # 背景颜色
        bg_color = xf.background.pattern_colour_index

        return font_color, bg_color


if __name__ == '__main__':
    excelF = ExcelF()
    excelF.start()
