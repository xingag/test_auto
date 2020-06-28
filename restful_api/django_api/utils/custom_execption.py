#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: custom_exception_handler.py 
@time: 2020-06-25 12:58 
@description：异常处理
"""

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        print(response.data)
        response.data.clear()
        response.data['code'] = response.status_code
        response.data['data'] = []

        if response.status_code == 404:
            try:
                response.data['message'] = response.data.pop('detail')
                response.data['message'] = "Not found"
            except KeyError:
                response.data['message'] = "Not found"

        if response.status_code == 400:
            response.data['message'] = 'Input error'

        elif response.status_code == 401:
            response.data['message'] = "Auth failed"

        elif response.status_code >= 500:
            response.data['message'] = "Internal service errors"

        elif response.status_code == 403:
            response.data['message'] = "Access denied"

        elif response.status_code == 405:
            response.data['message'] = 'Request method error'
    return response

