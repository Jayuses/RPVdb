#!/RPVdb/server/flaskr/getdata.py
# -*- conding: utf-8 -*-
# 蓝图文件'getdata',为前端获取数据提供接口

import functools
from flask import (
    Blueprint, request
    )
from flaskr.db import get_db
from flask import Flask, jsonify

bp = Blueprint('getdata', __name__, url_prefix='/getdata')
#全局辅助变量
datalist = {}
casedata = {}
detaildata = {}
#连接数据库

@bp.route('/list',methods=['GET','POST'])
def getlist():
    '''获取数据目录'''
    response_list = {'status':'defeat'}
    if request.method == 'POST':
        datastyle = request.get_json()
        datalist['style'] =  datastyle.get('style')
        db = get_db()
        cursor = db.cursor()
        error = None
        if   datalist['style'] == 1 :
            #请求类型1，返回球形顶盖算例数据目录{'ID':'','CaseID':''}
            caselist = cursor.execute('SELECT CaseID,ID FROM tbCasesStruc1').fetchall()
            datalist['caselist'] = tup2dic(caselist,cursor.description)
            cursor.close()
        elif datalist['style'] == 2 :
            #请求类型2，返回内带平台球形顶盖算例数据目录{'ID':'','CaseID':''}
            caselist = cursor.execute('SELECT CaseID,ID FROM tbCasesStruc2').fetchall()
            datalist['caselist'] = tup2dic(caselist,cursor.description)
            cursor.close()
        elif datalist['style'] == 3 :
            #请求类型3，返回平顶盖算例数据目录{'ID':'','caseID':''}
            caselist = cursor.execute('SELECT CaseID,ID FROM tbCasesStruc3').fetchall()
            datalist['caselist'] = tup2dic(caselist,cursor.description)
            cursor.close()
        elif datalist['style'] == 4 :
            #请求类型4，返回SG-系列结构尺寸数据目录{'ID':'','caseID':''}
            caselist = cursor.execute('SELECT SG_ID,ID FROM tbCasesStruc1').fetchall()
            datalist['caselist'] = tup2dic(caselist,cursor.description)
            cursor.close()
    else:
        response_list = datalist

    return jsonify(response_list)

@bp.route('/case',methods=['GET','POST'])
def get_case():
    '''获取算例数据'''
    response_data = {'status':'defeat'}
    if request.method == 'POST':
        index = request.get_json()
        style = index.get('style')
        idIndex = index.get('index')
        db = get_db()
        cursor = db.cursor()
        error = None
        if style == 1:
            case = cursor.execute(
                "SELECT * FROM tbCasesStruc1 WHERE CaseID = '%s'" %(idIndex)).fetchone()
            casedata['case'] = composedict(cursor.description,case)
            cursor.close()
        elif style == 2:
            case = cursor.execute(
                "SELECT * FROM tbCasesStruc2 WHERE CaseID = '%s'" %(idIndex)).fetchone()
            casedata['case'] = composedict(cursor.description,case)
            cursor.close()
        elif style == 3:
            case = cursor.execute(
                "SELECT * FROM tbCasesStruc3 WHERE CaseID = '%s'" %(idIndex)).fetchone()
            casedata['case'] = composedict(cursor.description,case)
            cursor.close()
        else:
            pass
    else:
        response_data = casedata
    return jsonify(response_data)

@bp.route('/geom',methods=['GET','POST'])
def get_gemo():
    '''获取结构参数'''
    response_data = {'status':'defeat'}
    if request.method == 'POST':
        index = request.get_json().get('index')
        style = request.get_json().get('style')
        db = get_db()
        cursor = db.cursor()
        if style == 1:
            geom = cursor.execute(
                "SELECT * FROM tbStrucGeom1 WHERE SG_ID = '%s'" %(index)).fetchone()
            detaildata['geom'] = composedict(cursor.description,geom)
            cursor.close()
        elif style == 2:
            geom = cursor.execute(
                "SELECT * FROM tbStrucGeom2 WHERE SG_ID = '%s'" %(index)).fetchone()
            detaildata['geom'] = composedict(cursor.description,geom)
            cursor.close()
        elif style == 3:
            geom = cursor.execute(
                "SELECT * FROM tbStrucGeom3 WHERE SG_ID = '%s'" %(index)).fetchone()
            detaildata['geom'] = composedict(cursor.description,geom)
            cursor.close()
    else:
        response_data = detaildata['geom']
    return jsonify(response_data)

@bp.route('/mater',methods=['GET','POST'])
def get_mater():
    '''获取材料参数'''
    response_data = {'status':'defeat'}
    if request.method == 'POST':
        index = request.get_json().get('index')
        db = get_db()
        cursor = db.cursor()
        #比热容
        capacity = cursor.execute(
                "SELECT Temperature,Variable FROM tbCapacity WHERE MaterID = '%s'" %(index)).fetchall()
        #热导率
        conductivity = cursor.execute(
                "SELECT Temperature,Variable FROM tbConductivity WHERE MaterID = '%s'" %(index)).fetchall()
        #热膨胀系数
        CTE = cursor.execute(
                "SELECT Temperature,Variable FROM tbCTE WHERE MaterID = '%s'" %(index)).fetchall()
        #密度
        density = cursor.execute(
                "SELECT Temperature,Variable*1E+10 FROM tbDensity WHERE MaterID = '%s'" %(index)).fetchall()
        #弹性模量
        elastic = cursor.execute(
                "SELECT Temperature,Variable FROM tbElastic WHERE MaterID = '%s'" %(index)).fetchall()
        #泊松比
        possion = cursor.execute(
                "SELECT Temperature,Variable FROM tbPossion WHERE MaterID = '%s'" %(index)).fetchall()
        #切线模量
        tangent = cursor.execute(
                "SELECT Temperature,Variable FROM tbTangent WHERE MaterID = '%s'" %(index)).fetchall()
        #屈服强度
        yie = cursor.execute(
                "SELECT Temperature,Variable FROM tbYield WHERE MaterID = '%s'" %(index)).fetchall()
        des = cursor.description
        detaildata['mater'] = {
            'capacity':capacity,
            'conductivity':conductivity,
            'CTE':CTE,
            'density':density,
            'elastic':elastic,
            'possion':possion,
            'tangent':tangent,
            'yie':yie,
            }
        cursor.close()
    else:
        response_data = detaildata['mater']
    return jsonify(response_data)

@bp.route('/load',methods=['GET','POST'])
def get_load():
    '''获取三种顶盖的工况参数'''
    response_data = {'status':'defeat'}
    if request.method == 'POST':
        loadIndex = request.get_json()
        style = loadIndex.get('style')
        index = loadIndex.get('index')
        db = get_db()
        cursor = db.cursor()
        if style == 1:
            loadcondition = cursor.execute(
                    "SELECT * FROM tbLoadCon1 WHERE LC_ID = '%s'" %(index)).fetchone()
            loadcon = composedict(cursor.description,loadcondition)
            loadtp = cursor.execute(
                    "SELECT Time,Temperature,Pressure FROM tbLoadTP1 WHERE LC_ID = '%s'" %(index)).fetchall()
            #输出载荷条件和温度压力
            detaildata['load'] = {
                'loadCon':loadcon,
                'loadTP':loadtp
                }
            cursor.close()
        elif style == 2:
            loadcondition = cursor.execute(
                    "SELECT * FROM tbLoadCon2 WHERE LC_ID = '%s'" %(index)).fetchone()
            loadcon = composedict(cursor.description,loadcondition)
            loadtp = cursor.execute(
                    "SELECT Time,Temperature,Pressure FROM tbLoadTP2 WHERE LC_ID = '%s'" %(index)).fetchall()
            detaildata['load'] = {
                'loadCon':loadcon,
                'loadTP':tup2dic(loadtp,cursor.description)
                }
            cursor.close()
        elif style == 3:
            loadcondition = cursor.execute(
                    "SELECT * FROM tbLoadCon3 WHERE LC_ID = '%s'" %(index)).fetchone()
            loadcon = composedict(cursor.description,loadcondition)
            loadtp = cursor.execute(
                    "SELECT Time,Temperature,Pressure FROM tbLoadTP3 WHERE LC_ID = '%s'" %(index)).fetchall()
            detaildata['load'] = {
                'loadCon':loadcon,
                'loadTP':tup2dic(loadtp,cursor.description)
                }
            cursor.close()
        else:
            pass
    else:
        response_data = detaildata['load']
    return jsonify(response_data)

@bp.route('/result',methods=['GET','POST'])
def get_result():
    '''获取结构参数'''
    response_data = {'status':'defeat'}
    if request.method == 'POST':
        resultIndex = request.get_json()
        style = resultIndex.get('style')
        index = resultIndex.get('index')
        db = get_db()
        cursor = db.cursor()
        detaildata['result'] = getResult(cursor,style)
        cursor.close()
    else:
        response_data = detaildata['result']
    return jsonify(response_data)

def composedict(des,value):
    '''将键值匹配为字典'''
    dict = {}
    for index,tup in enumerate(des):
        dict[tup[0]] = value[index]
    return dict

def tup2dic(tup,des):
    '''输入元组，输出对象列表'''
    outlist = []
    for t in tup:
        outlist.append(composedict(des,t))
    return outlist

def list2dic(tup,des):
    '''输入元组，输出列表对象'''
    list1 = []
    list2 = []
    for t in tup:
        list1.append(t[0])
        list2.append(t[1])
    outlist = [list1,list2]
    return composedict(des,outlist)

def getResult(cursor,type):
    '''获取分类完好的算例结果'''
    table = 'tbResultsStruc'+str(type)
    JX_IN1 = cursor.execute(
             "SELECT Time,JX_IN FROM '%s' WHERE CaseID = '%s' AND Time<=2" %(table,index)).fetchall()
    JX_IN2 = cursor.execute(
             "SELECT Time,JX_IN FROM '%s' WHERE CaseID = '%s' AND Time>=2" %(table,index)).fetchall()
    ZX_IN1 = cursor.execute(
             "SELECT Time,ZX_IN FROM '%s' WHERE CaseID = '%s' AND Time<=2" %(table,index)).fetchall()
    ZX_IN2 = cursor.execute(
             "SELECT Time,ZX_IN FROM '%s' WHERE CaseID = '%s' AND Time>=2" %(table,index)).fetchall()
    ZX_OUT1 = cursor.execute(
             "SELECT Time,ZX_OUT FROM '%s' WHERE CaseID = '%s' AND Time<=2" %(table,index)).fetchall()
    ZX_OUT2 = cursor.execute(
             "SELECT Time,ZX_OUT FROM '%s' WHERE CaseID = '%s' AND Time>=2" %(table,index)).fetchall()
    JX_OUT1 = cursor.execute(
             "SELECT Time,JX_OUT FROM '%s' WHERE CaseID = '%s' AND Time<=2" %(table,index)).fetchall()
    JX_OUT2 = cursor.execute(
             "SELECT Time,JX_OUT FROM '%s' WHERE CaseID = '%s' AND Time>=2" %(table,index)).fetchall()
    ZJ_U1 = cursor.execute(
             "SELECT Time,ZJ_U FROM '%s' WHERE CaseID = '%s' AND Time<=2" %(table,index)).fetchall()
    ZJ_U2 = cursor.execute(
             "SELECT Time,ZJ_U FROM '%s' WHERE CaseID = '%s' AND Time>=2" %(table,index)).fetchall()
    ZJ_D1 = cursor.execute(
             "SELECT Time,ZJ_D FROM '%s' WHERE CaseID = '%s' AND Time<=2" %(table,index)).fetchall()
    ZJ_D2 = cursor.execute(
             "SELECT Time,ZJ_D FROM '%s' WHERE CaseID = '%s' AND Time>=2" %(table,index)).fetchall()
    FL_JXWYL1 = cursor.execute(
             "SELECT Time,FL_JXWYL FROM '%s' WHERE CaseID = '%s' AND Time<=2" %(table,index)).fetchall()
    FL_JXWYL2 = cursor.execute(
             "SELECT Time,FL_JXWYL FROM '%s' WHERE CaseID = '%s' AND Time>=2" %(table,index)).fetchall()
    FL_ZKL1 = cursor.execute(
             "SELECT Time,FL_ZKL FROM '%s' WHERE CaseID = '%s' AND Time<=2" %(table,index)).fetchall()
    FL_ZKL2 = cursor.execute(
             "SELECT Time,FL_ZKL FROM '%s' WHERE CaseID = '%s' AND Time>=2" %(table,index)).fetchall()
    LS_YJL1 = cursor.execute(
             "SELECT Time,LS_YJL FROM '%s' WHERE CaseID = '%s' AND Time<=2" %(table,index)).fetchall()
    LS_YJL2 = cursor.execute(
             "SELECT Time,LS_YJL FROM '%s' WHERE CaseID = '%s' AND Time>=2" %(table,index)).fetchall()
    result = {
        'JX_IN1':JX_IN1,
        'JX_IN2':JX_IN2,
        'ZX_IN1':ZX_IN1,
        'ZX_IN2':ZX_IN2,
        'ZX_OUT1':ZX_OUT1,
        'ZX_OUT2':ZX_OUT2,
        'JX_OUT1':JX_OUT1,
        'JX_OUT2':JX_OUT2,
        'ZJ_U1':ZJ_U1,
        'ZJ_U2':ZJ_U2,
        'ZJ_D1':ZJ_D1,
        'ZJ_D2':ZJ_D2,
        'FL_JXWYL1':FL_JXWYL1,
        'FL_JXWYL2':FL_JXWYL2,
        'FL_ZKL1':FL_ZKL1,
        'FL_ZKL2':FL_ZKL2,
        'LS_YJL1':LS_YJL1,
        'LS_YJL2':LS_YJL2,
        }
    return result



