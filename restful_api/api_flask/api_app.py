from flask import Flask
import config
from flask_restful import Api
from api.api_foo import *
from flasgger import Swagger

app = Flask(__name__)
# 配置文件
app.config.from_object(config)

# 绑定数据库
db.init_app(app)
api = Api(app)

# API可视化管理
swagger_config = Swagger.DEFAULT_CONFIG

# 标题
swagger_config['title'] = config.SWAGGER_TITLE
# 描述信息
swagger_config['description'] = config.SWAGGER_DESC
# Host
swagger_config['host'] = config.SWAGGER_HOST

# 实例化
swagger = Swagger(app,config=swagger_config)

# swagger = Swagger(app)


# 某一条记录
api.add_resource(FooApi, '/api/v1/foo','/api/v1/foo/<int:id>')
# 所有记录
api.add_resource(FooListApi, '/api/v1/foos')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)


#=========================================
# 公众号：AirPython

# 访问Doc地址
# http://localhost:5000/apidocs/


# 在线编辑文件（swagger编写格式）
# http://editor.swagger.io/#/