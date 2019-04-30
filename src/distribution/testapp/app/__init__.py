"""sanic默认的app构造组件.

组件名字会被改为项目名.

注册模块组件使用`xxx.init_app(app)`;

使用数据库组件放在hooks模块中在启动项目时挂载
"""
from sanic import Sanic
from .api import restapi



def main():
    app = Sanic()
    restapi.init_app(app)
    app.run()
