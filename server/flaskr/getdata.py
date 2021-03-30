#!/RPVdb/server/flaskr/getdata.py
# -*- conding: utf-8 -*-
# 蓝图文件'getdata',为前端获取数据提供接口

import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,current_app
    )
from flaskr.db import get_db
from flask import Flask, jsonify

bp = Blueprint('getdata', __name__, url_prefix='/getdata')
#全局辅助变量
datalist = {}

@bp.route('/list',methods=['GET','POST'])
def getlist():
    '''获取数据目录'''
    response_list = {'status':'defeat'}
    if request.method == 'POST':
        datastyle = request.get_json()
        datalist['style'] =  datastyle.get('style')
        if   datalist['style'] == 1 :
            #请求类型1，返回球形顶盖算例数据目录{'ID':'','CaseID':''}
            db = get_db()
            cursor = db.cursor()
            error = None
            caselist = cursor.execute('SELECT CaseID,ID FROM tbCasesStruc1').fetchall()
            datalist['caselist'] = tup2dic(caselist,cursor.description)
            cursor.close()
        elif datalist['style'] == 2 :
            #请求类型2，返回内带平台球形顶盖算例数据目录{'ID':'','CaseID':''}
            pass
        elif datalist['style'] == 3 :
            #请求类型3，返回平顶盖算例数据目录{'ID':'','caseID':''}
            pass
        elif datalist['style'] == 4 :
            #请求类型4，返回SG-系列结构尺寸数据目录{'ID':'','caseID':''}
            pass
        elif datalist['style'] == 5 :
            #请求类型5，返回SG-D-系列结构尺寸数据目录{'ID':'','caseID':''}
            pass
        elif datalist['style'] == 6 :
            #请求类型6，返回其他结构尺寸数据目录{'ID':'','caseID':''}
            pass
        elif datalist['style'] == 7 :
            #请求类型7，返回材料库数据目录{'ID':'','caseID':''}
            pass
        elif datalist['style'] == 8 :
            #请求类型8，返回加载工况库数据目录{'ID':'','caseID':''}
            pass
    else:
        response_list = datalist
        pass

    def composelist(list):
        outlist = []
        for li in list:
            outlist = outlist + li 
        return outlist

    return jsonify(response_list)



@bp.route('/case',methods=['GET','POST'])
def get_case():
    '''获取算例数据'''
    db = get_db()
    cursor = db.cursor()
    error = None
    case_value = cursor.execute('SELECT * FROM tbCasesStruc1 WHERE ID=13').fetchone()
    dict = composedict(cursor.description,case_value)
    cursor.close()
    return jsonify(dict)

def composedict(des,value):
    dict = {}
    for index,tup in enumerate(des):
        dict[tup[0]] = value[index]
    return dict

def tup2dic(tup,des):
    '''输入元组，输出对象'''
    outlist = []
    for t in tup:
        outlist.append(composedict(des,t))
    return outlist