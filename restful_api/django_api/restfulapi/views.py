from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser, JSONParser

from .models import Music
from .serializers import MusicSerializer
from django_filters import rest_framework as filters
from utils.CustomViewBase import *

# 欢迎关注公众号：AirPython


# class MusicViewSet(viewsets.ModelViewSet):
class MusicViewSet(CustomViewBase):
    """
    CRUD 
    """
    authentication_classes = []
    permission_classes = []

    # 解析方式
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    queryset = Music.objects.all()
    serializer_class = MusicSerializer

    # 过滤
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = MusicFilter


    def create(self, request, *args, **kwargs):
        """新建一条音乐"""
        pass

    def list(self, request, *args, **kwargs):
        """全部音乐数据"""
        pass

    def retrieve(self, request, *args, **kwargs):
        """查询一条数据"""
        pass

    def update(self, request, *args, **kwargs):
        """更新一条音乐数据"""
        pass

    def destroy(self, request, *args, **kwargs):
        """删除一条数据"""
        pass


# GET 请求（查询）
# curl --location --request GET 'http://127.0.0.1:8000/music/'

# 过滤查询
# curl --location --request GET 'http://127.0.0.1:8000/music/?song=%E4%B8%83%E9%87%8C%E9%A6%991'


# POST 请求（创建）
# curl --location --request POST 'http://127.0.0.1:8000/music/' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "song":"我是中国人",
#     "singer":"刘德华"
# }'


# PUT 请求（更新）
# curl --location --request PUT 'http://127.0.0.1:8000/music/1/' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "song":"七里香1",
#     "singer":"周杰伦1"
# }'

# DELETE 请求（删除）
# curl --location --request DELETE 'http://127.0.0.1:8000/music/3/'


def index(request):
    return render(request, 'index.html')
