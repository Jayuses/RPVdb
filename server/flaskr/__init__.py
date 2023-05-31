import os
from flask import Flask
from flask import Flask, jsonify
from flask_cors import CORS

def create_app(test_config=None):
    #应用工厂
    app = Flask(__name__,instance_relative_config=True)
    #应用配置
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE1=os.path.join(app.instance_path,'RPV-Simulation.mdb'),
        DATABASE2=os.path.join(app.instance_path,'Users.mdb'),
        )

    #使用flask-CORS扩展，允许全局跨域
    cor=CORS(app)

    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #返回响应后关闭数据库
    from . import db
    db.init_app(app)

    #注册'getdata'蓝图
    from . import getdata
    app.register_blueprint(getdata.bp)

    #注册'login'蓝图
    from . import login
    app.register_blueprint(login.bp)

    #注册'search'蓝图
    from . import search
    app.register_blueprint(search.bp)

    #注册'create'蓝图
    from . import create
    app.register_blueprint(create.bp)

    #注册'change'蓝图
    from . import change
    app.register_blueprint(change.bp)

    from . import db
    db.init_app(app)

    return app