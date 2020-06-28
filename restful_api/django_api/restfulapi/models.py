from django.db import models


# ORM，对象关系映射，将模型映射到数据库中

class Music(models.Model):
    song = models.CharField(max_length=100,default='')
    singer = models.CharField(max_length=100,default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'music'


# python3 manage.py makemigrations  --empty  restfulapi
# python3 manage.py migrate