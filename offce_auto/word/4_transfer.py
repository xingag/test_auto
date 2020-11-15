#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: https://github.com/xingag 
@software: PyCharm 
@file: transfer.py 
@time: 2020/11/10 15:45 
@description：doc转为docx（批量）
"""

# doc转为docx分Win和Mac/Linxu
# win：使用win32com模块
# mac/linux:LibreOffice软件

# 以mac为例，下载LibreOffice软件；安装完全软件目录：/Applications/LibreOffice.app/Contents/MacOS
# 转换命令（可以转为docx、txt、pdf等格式）：./soffice --headless --convert-to docx 111.doc --outdir /output/path/
# 配置环境变量PATH，并重启pycharm
# #doc转为docx
# export PATH=$PATH:/Applications/LibreOffice.app/Contents/MacOS


import os

# from win32com import client
#
#
# def doc_to_docx_in_win(path_raw, path_output):
#     """
#     doc转为docx（win）
#     :param path_original:
#     :param path_final:
#     :return:
#     """
#     # 获取文件的格式后缀
#     file_suffix = os.path.splitext(path_raw)[1]
#     if file_suffix == ".doc":
#         word = client.Dispatch('Word.Application')
#         # 源文件
#         doc = word.Documents.Open(path_raw)
#         # 生成的新文件
#         doc.SaveAs(path_output, 16)
#         doc.Close()
#         word.Quit()
#     elif file_suffix == ".docx":
#         shutil.copy(path_raw, path_output)



source = "./doc/"
dest = "./docx/"
g = os.walk(source)

# 遍历目录
for root, dirs, files in g:
    for file in files:

        # 源文件目录
        file_path_raw = os.path.join(root, file)

        # 使用soffice命令进行转换
        os.system("soffice --headless --convert-to docx {} --outdir {}".format(file_path_raw, dest))
