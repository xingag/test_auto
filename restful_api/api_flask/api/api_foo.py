#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: FooResource.py 
@time: 2020-06-07 11:18 
@description：来源公众号：AirPython，欢迎关注
"""

from flask_restful import Resource, fields, marshal_with, request

from exts import db
from models import Foo
from utils.restful_utils import *

class FooListApi(Resource):
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'age': fields.String
    }

    @marshal_with(resource_fields)
    def get(self):
        """
        返回所有记录
        :return:
        """
        foos = db.session.query(Foo).all()
        return foos


# RESTful API
class FooApi(Resource):
    # 输出字段定义
    resource_fields = {
        'id': fields.Integer,
        'name': fields.String,
        'age': fields.String
    }

    @marshal_with(resource_fields)
    def get(self, id):
        """获取用户信息
    ---
    schemes:
      - http
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        default: 1
        description: 用户id

    responses:
      200:
        description: 返回用户信息
        examples:
                {
                    "id": 1,
                    "name": "xag",
                    "age":"18"
                }
    """
        foo = db.session.query(Foo).get(id)
        return foo
        
    def post(self):
        """
        创建一条记录
        :return:
        """
        # 参数
        params = request.get_json()
        name = params.get("name")
        age = params.get("age")
        # 构建一个模型
        foo = Foo(name=name, age=age)

        # 加入到数据库
        db.session.add(foo)
        db.session.commit()

        return success("新增一条记录成功！")

    def put(self, id):
        """
        更新一条记录
        :return:
        """
        params = request.get_json()
        name = params.get("name")
        age = params.get("age")

        # 查询数据是否存在
        foo = db.session.query(Foo).get(id)
        if foo:
            if name:
                foo.name = name
            if age:
                foo.age = age
            db.session.commit()
            return success("更新成功！")
        else:
            return params_error("更新失败！不存在这条记录！")

    def delete(self, id):
        """
        删除某条记录
        :return:
        """
        foo = db.session.query(Foo).get(id)
        if foo:
            db.session.delete(foo)
            db.session.commit()
            return success("删除成功！")
        else:
            return params_error("删除失败！不存在这条记录！")
