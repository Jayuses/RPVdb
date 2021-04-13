#!/RPVdb/server/flaskr/getdata.py
# -*- conding: utf-8 -*-
# 蓝图文件'login',处理前端登录请求
from flask import (Blueprint, request)
from flask import Flask, jsonify

#用户信息明示，后续应建立数据库并加密
userlist = [
    {'username':'admin','password':'123321'}
    ]

#辅助状态变量
statusdata = {}

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/',methods=['GET','POST'])
def login():
    response_status = {}
    if request.method == 'POST':
        loginForm = request.get_json()
        username = loginForm.get('username')
        password = loginForm.get('password')
        statusdata['status'] = -1
        for user in userlist:
            if user['username'] == username:
                if user['password'] == password:
                    statusdata['status'] = 1  #登录成功
                else:
                    statusdata['status'] = 0  #密码错误
        if statusdata['status'] == -1:
            statusdata['status'] = 2  #用户名不存在
        response_status = statusdata
    else:
        response_status = statusdata
    return jsonify(response_status)
