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
@time: 2020/10/23 17:17 
@description：使用xlsxwriter处理Excel
"""

# 依赖：pip3 install xlsxwriter

# 注意：xlsxwriter只能写入到新的Excel文件，不能读取或者修改已有的Excel文件

import xlsxwriter
from utils.xlsxwriter_util import *


class ExcelF(object):

    def __init__(self):
        # 单元格字体样式
        self.title_style = {'bold': True, 'bg_color': '#B0C4DE', 'font_size': 10,
                            'font_name': 'Microsoft yahei'}
        self.wb = None
        self.current_sheet = None

    def start(self):
        # 1、创建工作簿和sheet
        self.wb, sheets = create_workbook_and_worksheet('./output.xlsx', ["第一个Sheet", "第二个Sheet"])
        self.current_sheet = sheets[0]

        # 2、往单元格中写入数据
        # self.write_value()

        # 3、插入图片
        # self.insert_images()

        # 4、设置行高和列宽
        self.set_row_height_and_column_width()

        # 5、插入数据
        self.insert_datas()

        # 7、插入图表
        # 比如：面积图、条形图、柱状图、折线图、饼图、圆环图、散射图、股价图、雷达图
        self.insert_charts()

        # 保存数据到文件中，并关闭文件
        self.teardown()

    def write_value(self):
        """
        往单元格中写入数据
        :return:
        """
        # 创建标题字体样式
        title_font_style = create_format_styles(self.wb, self.title_style)

        # 往worksheet中写入数据
        # 第一行
        write_to_cell(self.current_sheet, 1, 1, "姓名", title_font_style)
        write_to_cell(self.current_sheet, 1, 2, "年龄", title_font_style)
        # 第二行
        write_to_cell(self.current_sheet, 2, 1, 'xingag')
        write_to_cell(self.current_sheet, 2, 2, 23)

        # 写入第3行-第5行
        # 定义待写入的数据
        datas = [
            ['张三', 18],
            ['李四', 19],
            ['王五', 20]
        ]
        for row_index, people in enumerate(datas):
            for column_index, data in enumerate(people):
                write_to_cell(self.current_sheet, row_index + 3, column_index + 1, data)

    def set_row_height_and_column_width(self):
        """
        设置行高和列宽
        :return:
        """
        # 设置列宽度
        # 设置第1列到第3列的宽度为：100
        set_column_width(self.current_sheet, 1, 3, 100)

        # 设置行高
        set_row_height(self.current_sheet, 1, 50)
        set_row_height(self.current_sheet, 2, 100)

    def insert_images(self):
        """
        插入图片和表格
        :return:
        """
        # 1、插入图片
        # insert_image(row, col, image[, options])
        # row(int) - 单元格所在的行（索引从0开始计数）
        # col(int) - 单元格所在的列（索引从0开始计数）
        # image(string) - 图片文件名（如有需要含路径）
        # options(dict) - 可选参数，包含：图片位置，缩放，url参数

        # 1.1 加载本地图片
        # 定义一个图片展示可选参数
        image_options = create_image_options(x_scale=0.5, y_scale=0.5, url='https://www.jianshu.com/u/f3b476549169')
        insert_local_image(self.current_sheet, 1, 1, '1.png', image_options)

        # 1.2 加载网络图片
        url = 'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1469158657,3820880868&fm=26&gp=0.jpg'
        # image_options2 = create_image_options(x_scale=0.2, y_scale=0.2, url='https://www.jianshu.com/u/f3b476549169')
        # image_options3 = create_image_options(url='https://www.jianshu.com/u/f3b476549169')
        image_options4 = create_image_options(x_scale=0.5, y_scale=0.5, url='https://www.jianshu.com/u/f3b476549169')
        insert_network_image(self.current_sheet, 1, 1, url, '1.png', image_options4)

    def insert_datas(self):
        """
        插入数据
        :return:
        """
        # 表头（第一行）
        titles = ['', '篮球', '排球', '足球', '受访总人数']

        # 数据（一共3行数据）
        export_data = [
            ['男', 11, 21, 31, 63],
            ['女', 12, 22, 32, 66],
            ['受访总人数', 23, 43, 63, 129]
        ]

        # 标题单元格文字样式
        column_title_format = create_format_styles(self.wb, {
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'color': '#FF0000',
            'font_size': 12
        })

        # 数据单元格文字样式
        data_format = create_format_styles(self.wb, {
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'font_size': 12
        })

        # 写入标题
        column_index = 0
        titles = [{'name': item, 'width': 20} for item in titles]

        for t in titles:
            # 写入数据
            self.current_sheet.write(0, column_index, t['name'], column_title_format)
            # 设置列宽
            self.current_sheet.set_column(column_index, column_index, t['width'])
            column_index += 1

        # 写入数据
        start_row = 1  # 起始行
        for item in export_data:
            for index, value in enumerate(item):
                # 写入数据，第一列设置为标题样式；其余设置为内容样式
                self.current_sheet.write(start_row, index, value, column_title_format if index == 0 else data_format)
            start_row += 1

    def insert_charts(self):
        """
        插入图表
        area：面积图
        bar：条形图
        column：柱状图
        line：折线图
        pie：饼图
        doughnut：圆环图
        scatter：散点图
        stock：股价图
        radar：雷达图
        :return:
        """
        # 自定义样式，加粗
        bold = self.wb.add_format({'bold': 1})

        # 标题栏（3列）
        headings = ['Number', 'testA', 'testB']
        # 数据
        data = [
            ['2017-9-1', '2017-9-2', '2017-9-3', '2017-9-4', '2017-9-5', '2017-9-6'],
            [10, 40, 50, 20, 10, 50],
            [30, 60, 70, 50, 40, 30],
        ]

        # 写入表头
        self.current_sheet.write_row('A1', headings, bold)

        # 写入数据
        self.current_sheet.write_column('A2', data[0])
        self.current_sheet.write_column('B2', data[1])
        self.current_sheet.write_column('C2', data[2])

        # --------2、生成图表并插入到excel---------------
        # 创建一个柱状图(line chart)
        chart_col = self.wb.add_chart({'type': 'line'})

        # 配置第一个系列数据（第一条折线）
        chart_col.add_series({
            # 如果我们新建sheet时设置了sheet名，这里就要设置成相应的值
            'name': '=第一个Sheet!$B$1',
            'categories': '=第一个Sheet!$A$2:$A$7',
            'values': '=第一个Sheet!$B$2:$B$7',
            'line': {'color': 'red'},
        })

        # 配置第二个系列数据（第二个折线）
        chart_col.add_series({
            'name': '=第一个Sheet!$C$1',
            'categories': '=第一个Sheet!$A$2:$A$7',
            'values': '=第一个Sheet!$C$2:$C$7',
            'line': {'color': 'yellow'},
        })

        # 配置第二个系列数据(用了另一种语法)
        # chart_col.add_series({
        #     'name': ['Sheet1', 0, 2],
        #     'categories': ['Sheet1', 1, 0, 6, 0],
        #     'values': ['Sheet1', 1, 2, 6, 2],
        #     'line': {'color': 'yellow'},
        # })

        # 设置图表的title 和 x，y轴信息
        chart_col.set_title({'name': 'The xxx site Bug Analysis'})
        chart_col.set_x_axis({'name': 'Test number'})
        chart_col.set_y_axis({'name': 'Sample length (mm)'})

        # 设置图表的风格
        chart_col.set_style(1)

        # 把图表插入到worksheet并设置偏移
        self.current_sheet.insert_chart('A10', chart_col, {'x_offset': 25, 'y_offset': 10})

    def teardown(self):
        # 写入文件，并关闭文件
        self.wb.close()


if __name__ == '__main__':
    excelF = ExcelF()
    excelF.start()
