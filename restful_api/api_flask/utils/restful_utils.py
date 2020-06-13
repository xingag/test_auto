#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: restful_utils.py 
@time: 2020-06-07 15:28 
@description：TODO
"""

from flask import jsonify


class HttpCode(object):
    ok = 200
    un_auth_error = 401
    params_error = 400
    server_error = 500


def restful_result(code, message, data):
    return jsonify({"code": code, "message": message, "data": data or {}})


def success(message="", data=None):
    """
    正确返回
    :param message:
    :param data:
    :return:
    """
    return restful_result(code=HttpCode.ok, message=message, data=data)


def un_auth_error(message=""):
    return restful_result(code=HttpCode.un_auth_error, message=message, data=None)


def params_error(message=""):
    """
    参数错误
    :param message:
    :return:
    """
    return restful_result(code=HttpCode.params_error, message=message, data=None)


def server_error(message=""):
    """
    服务器内部错误
    :param message:
    :return:
    """
    return restful_result(code=HttpCode.server_error, message=message or '服务器内部错误', data=None)
