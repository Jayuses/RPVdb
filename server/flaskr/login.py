#!/RPVdb/server/flaskr/getdata.py
# -*- conding: utf-8 -*-
# 蓝图文件'login',处理前端登录请求
from flask import (Blueprint, request)
from flask import Flask, jsonify
from flaskr.db import get_users
from werkzeug.security import check_password_hash, generate_password_hash

#辅助状态变量
statusdata = {'status':'','class':-1}

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
        user = cursor.execute(
            "SELECT * FROM tbUser WHERE NAME = ?",(username,)).fetchone()
        if user is None:
            statusdata['status'] = 2  #用户名不存在
        else:
            if user[2] == 'user':
                user_class = 1
            elif user[2] == 'administrator':
                user_class = 0       
            
            if not check_password_hash(user[1], password):
                statusdata['status'] = 0  #密码错误
            else:
                statusdata['status'] = 1  #登录成功

        statusdata['class'] = user_class
        cursor.close()
    else:
        response = statusdata
    return jsonify(response)

@bp.route('/change',methods=['POST','GET'])
def change():
    response = {}
    if request.method == 'POST':
        change_quest = request.get_json()
        del_data = change_quest.get('delData')
        mod = change_quest.get('mod')
        users = get_users()
        cursor = users.cursor()

        for item in del_data:
            cursor.execute('DELETE FROM tbUser WHERE NAME=?',(item['name'],))
        
        for item in mod:
            user = cursor.execute("SELECT * FROM tbUser WHERE NAME = ?",(item['name'],)).fetchone()
            if user:
                if item['password'] == '******' or item['password'] == '':
                    sql = 'UPDATE tbUser SET [LEVEL]=? WHERE NAME=?'
                    cursor.execute(sql,(item['level'],item['name']))
                else:
                    sql = 'UPDATE tbUser SET PASSWORD=?,[LEVEL]=? WHERE NAME=?'
                    cursor.execute(sql,(generate_password_hash(item['password']),item['level'],item['name']))
            else:
                sql = 'INSERT INTO tbUser (NAME,PASSWORD,[LEVEL]) VALUES (?,?,?)'
                cursor.execute(sql,(item['name'],generate_password_hash(item['password']),item['level']))
        
        cursor.commit()
        cursor.close()
        statusdata['status'] = 1
    else:
        response = statusdata['status']
    return jsonify(response)
