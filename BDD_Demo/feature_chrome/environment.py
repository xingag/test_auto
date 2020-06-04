#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: environment.py 
@time: 2020-06-03 12:47 
@description：配置环境文件
"""

from selenium import webdriver
import behave2cucumber
import json

# environment.py文件定义了一些当测试脚本在run的过程中之前和之后完成的任务


def before_all(context):
    pass


def before_feature(context, feature):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.google.com/")


def after_feature(context, feature):
    context.driver.quit()


def after_all(context):
    """
    所有测试完成之后执行
    注意：behave1.2.6生成的json没法正常转换为cucumber兼容的json报告，建议降级为：1.2.5
    :param context:
    :return:
    """

    # 转换
    with open('./test_report.json',encoding='utf-8') as behave_json:
        # 格式转换
        cucumberJson = behave2cucumber.convert(json.load(behave_json))

    jsonStr = json.dumps(cucumberJson)

    # 写入
    jsonReport = open(r'./report/jsonReport.json', 'w',encoding='utf-8')
    jsonReport.write(jsonStr)
    jsonReport.close()


if __name__ == '__main__':
    after_all(None)