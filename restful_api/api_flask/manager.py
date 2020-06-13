#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: manager.py 
@time: 2020-06-07 09:38 
@description：数据库映射
"""

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from exts import db
from api_app import app
from models import Foo

# 显式写出要映射到数据库的模型



manager = Manager(app)
migrate=Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()



# 映射命令
# python3 manager.py db init
# python3 manager.py db migrate
# python3 manager.py db upgrade
