#!/RPVdb/server/flaskr/getdata.py
# -*- conding: utf-8 -*-
# 蓝图文件'login',处理前端登录请求
from flask import (Blueprint, request)
from flask import Flask, jsonify
from flaskr.db import get_users
from werkzeug.security import check_password_hash

#辅助状态变量
statusdata = {}

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/',methods=['GET','POST'])
def login():
    response = {}
    if request.method == 'POST':
        loginForm = request.get_json()
        username = loginForm.get('username')
        password = loginForm.get('password')
        users = get_users()
        cursor = users.cursor()
        statusdata['status'] = -1
        user_class = -1  #用户等级
        admin = cursor.execute(
            "SELECT * FROM administrator WHERE USERNAME = ?",(username,)).fetchone()
        if admin is None:
            user = cursor.execute(
                "SELECT * FROM users WHERE USERNAME = ?",(username,)).fetchone()
            if user is None:
                statusdata['status'] = 2  #用户名不存在
            else:
                user_class = 1
                if not check_password_hash(user[2], password):
                    statusdata['status'] = 0  #密码错误
                else:
                    statusdata['status'] = 1  #登录成功
        else:
            user_class = 0
            if not check_password_hash(admin[2], password):
                statusdata['status'] = 0  #密码错误
            else:
                statusdata['status'] = 1  #登录成功

        statusdata['class'] = user_class
        cursor.close()
    else:
        response = statusdata
    return jsonify(response)
