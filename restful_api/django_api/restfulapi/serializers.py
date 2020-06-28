#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: music_serializers.py 
@time: 2020-06-06 10:52 
@description：Serializer序列化
"""

from rest_framework import serializers
from .models import Music



class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        
        fields = '__all__'
        # 序列化的字段（部分）
        # fields = ('id','song','singer','last_modify_date','created')
    