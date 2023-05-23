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
detaildata = {"geom":None,"mater":None,"load":None,"result":None}
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
        des = [('ID',  0)]
        error = None
        if   datalist['style'] == 1 :
            #请求类型1，返回球形顶盖算例数据目录{'CaseID':''}
            caselist = cursor.execute('SELECT CaseID FROM tbCasesStruc1').fetchall()
            datalist['caselist'] = tup2dic(caselist,des)
            cursor.close()
        elif datalist['style'] == 2 :
            #请求类型2，返回内带平台球形顶盖算例数据目录{'CaseID':''}
            caselist = cursor.execute('SELECT CaseID FROM tbCasesStruc2').fetchall()
            datalist['caselist'] = tup2dic(caselist,des)
            cursor.close()
        elif datalist['style'] == 3 :
            #请求类型3，返回平顶盖算例数据目录{'caseID':''}
            caselist = cursor.execute('SELECT CaseID FROM tbCasesStruc3').fetchall()
            datalist['caselist'] = tup2dic(caselist,des)
            cursor.close()
        elif datalist['style'] == 4 :
            #请求类型4，返回结构尺寸目录[ {'ID':'','CaseID':[caseID1,caseID2,.....] } ......]
            datalist['caselist'] = searchGeom(cursor)
            cursor.close()
        elif datalist['style'] == 5 :
            #请求类型5，返回材料目录{'MaterID':''}
            caselist = cursor.execute('SELECT MaterID FROM tbMater').fetchall()
            datalist['caselist'] = tup2dic(caselist,des)
            cursor.close()
        elif datalist['style'] == 6 :
            #请求类型6，返回工况目录[{'LT':'','LC':[{'LC_ID':'','CaseID':[LC_ID1,LC_ID2,....]}....]}....]
            datalist['caselist'] = searchLc(cursor)
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
            loadt = cursor.execute(
                    "SELECT Time,Temperature FROM tbLoadTP1 WHERE LC_ID = '%s'" %(index)).fetchall()
            loadp = cursor.execute(
                    "SELECT Time,Pressure FROM tbLoadTP1 WHERE LC_ID = '%s'" %(index)).fetchall()
            #输出载荷条件和温度压力
            detaildata['load'] = {
                'loadCon':loadcon,
                'loadT':loadt,
                'loadP':loadp
                }
            cursor.close()
        elif style == 2:
            loadcondition = cursor.execute(
                    "SELECT * FROM tbLoadCon2 WHERE LC_ID = '%s'" %(index)).fetchone()
            loadcon = composedict(cursor.description,loadcondition)
            loadt = cursor.execute(
                    "SELECT Time,Temperature FROM tbLoadTP2 WHERE LC_ID = '%s'" %(index)).fetchall()
            loadp = cursor.execute(
                    "SELECT Time,Pressure FROM tbLoadTP2 WHERE LC_ID = '%s'" %(index)).fetchall()
            #输出载荷条件和温度压力
            detaildata['load'] = {
                'loadCon':loadcon,
                'loadT':loadt,
                'loadP':loadp
                }
            cursor.close()
        elif style == 3:
            loadcondition = cursor.execute(
                    "SELECT * FROM tbLoadCon3 WHERE LC_ID = '%s'" %(index)).fetchone()
            loadcon = composedict(cursor.description,loadcondition)
            loadt = cursor.execute(
                    "SELECT Time,Temperature FROM tbLoadTP3 WHERE LC_ID = '%s'" %(index)).fetchall()
            loadp = cursor.execute(
                    "SELECT Time,Pressure FROM tbLoadTP3 WHERE LC_ID = '%s'" %(index)).fetchall()
            #输出载荷条件和温度压力
            detaildata['load'] = {
                'loadCon':loadcon,
                'loadT':loadt,
                'loadP':loadp
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
        detaildata['result'] = getResult(cursor,style,index)
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

def getResult(cursor,type,index):
    '''获取分类完好的算例结果'''
    table = 'tbResultsStruc'+str(type)
    sql = "SELECT Time,JX_IN FROM " + table + " WHERE CaseID = ? AND Time<=2"
    JX_IN1 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time*0.0002778,JX_IN FROM " + table + " WHERE CaseID = ? AND Time>=2"
    JX_IN2 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time,ZX_IN FROM " + table + " WHERE CaseID = ? AND Time<=2"
    ZX_IN1 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time*0.0002778,ZX_IN FROM " + table + " WHERE CaseID = ? AND Time>=2"
    ZX_IN2 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time,ZX_OUT FROM " + table + " WHERE CaseID = ? AND Time<=2"
    ZX_OUT1 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time*0.0002778,ZX_OUT FROM " + table + " WHERE CaseID = ? AND Time>=2"
    ZX_OUT2 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time,JX_OUT FROM " + table + " WHERE CaseID = ? AND Time<=2"
    JX_OUT1 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time*0.0002778,JX_OUT FROM " + table + " WHERE CaseID = ? AND Time>=2"
    JX_OUT2 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time,ZJ_U FROM " + table + " WHERE CaseID = ? AND Time<=2"
    ZJ_U1 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time*0.0002778,ZJ_U FROM " + table + " WHERE CaseID = ? AND Time>=2"
    ZJ_U2 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time,ZJ_D FROM " + table + " WHERE CaseID = ? AND Time<=2"
    ZJ_D1 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time*0.0002778,ZJ_D FROM " + table + " WHERE CaseID = ? AND Time>=2"
    ZJ_D2 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time,FL_JXWYL FROM " + table + " WHERE CaseID = ? AND Time<=2"
    FL_JXWYL1 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time*0.0002778,FL_JXWYL FROM " + table + " WHERE CaseID = ? AND Time>=2"
    FL_JXWYL2 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time,FL_ZKL FROM " + table + " WHERE CaseID = ? AND Time<=2"
    FL_ZKL1 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time*0.0002778,FL_ZKL FROM " + table + " WHERE CaseID = ? AND Time>=2"
    FL_ZKL2 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time,LS_YJL*1E-6 FROM " + table + " WHERE CaseID = ? AND Time<=2"
    LS_YJL1 = cursor.execute(sql ,(index,)).fetchall()
    sql = "SELECT Time*0.0002778,LS_YJL*1E-6 FROM " + table + " WHERE CaseID = ? AND Time>=2"
    LS_YJL2 = cursor.execute(sql ,(index,)).fetchall()
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

def searchGeom(cursor):
    '''搜寻所有几何尺寸案例库，并将案例按库名分类'''
    outlist = [] #输出形式为 [ {'ID':'','CaseID':[caseID1,caseID2,.....] } ......]
    idlist = [] #辅助列表
    caselist = cursor.execute('SELECT CaseID,SG_ID FROM tbCasesStruc1').fetchall()
    for li in caselist:
        if li[1] not in idlist:
            outlist.append({'ID':li[1],'CaseID':[{'case':li[0]},],'style':1})
            idlist.append(li[1])
        else:
            outlist[idlist.index(li[1])]['CaseID'].append({'case':li[0]})

    caselist = cursor.execute('SELECT CaseID,SG_ID FROM tbCasesStruc2').fetchall()
    for li in caselist:
        if li[1] not in idlist:
            outlist.append({'ID':li[1],'CaseID':[{'case':li[0]},],'style':2})
            idlist.append(li[1])
        else:
            outlist[idlist.index(li[1])]['CaseID'].append({'case':li[0]})

    caselist = cursor.execute('SELECT CaseID,SG_ID FROM tbCasesStruc3').fetchall()
    for li in caselist:
        if li[1] not in idlist:
            outlist.append({'ID':li[1],'CaseID':[{'case':li[0]},],'style':3})
            idlist.append(li[1])
        else:
            outlist[idlist.index(li[1])]['CaseID'].append({'case':li[0]})

    return outlist

def searchLc(cursor):
    '''搜寻所有工况库，并将案例按库名分类'''
    #输出形式为 [{'LT':'','LC':[{'LC_ID':'','CaseID':[LC_ID1,LC_ID2,....]}....]}....]
    fList = []  #最终输出列表
    outlist = []  #检索tbCasesStruc得到的'LC_ID'与'CaseID'匹配列表
    idlist = []   #辅助列表
    #检索tbCasesStruc
    caselist = cursor.execute('SELECT CaseID,LC_ID FROM tbCasesStruc1').fetchall()
    for li in caselist:
        if li[1] not in idlist:
            outlist.append({'ID':li[1],'CaseID':[{'case':li[0]},],'style':1})
            idlist.append(li[1])
        else:
            outlist[idlist.index(li[1])]['CaseID'].append({'case':li[0]})

    caselist = cursor.execute('SELECT CaseID,LC_ID FROM tbCasesStruc2').fetchall()
    for li in caselist:
        if li[1] not in idlist:
            outlist.append({'ID':li[1],'CaseID':[{'case':li[0]},],'style':2})
            idlist.append(li[1])
        else:
            outlist[idlist.index(li[1])]['CaseID'].append({'case':li[0]})

    caselist = cursor.execute('SELECT CaseID,LC_ID FROM tbCasesStruc3').fetchall()
    for li in caselist:
        if li[1] not in idlist:
            outlist.append({'ID':li[1],'CaseID':[{'case':li[0]},],'style':3})
            idlist.append(li[1])
        else:
            outlist[idlist.index(li[1])]['CaseID'].append({'case':li[0]})

    #检索tbLoadCon
    ltlist = []   #辅助列表
    calist = []
    caselist = cursor.execute('SELECT LC_ID,LT FROM tbLoadCon1').fetchall()
    for li in caselist:
        if li[1] not in ltlist:
            fList.append({'LT':li[1],'LC':[li[0],]})
            ltlist.append(li[1])
            calist.append(li[0])
        else:
            if li[0] not in calist:
                fList[ltlist.index(li[1])]['LC'].append(li[0]) 
                calist.append(li[0])
            else:
                continue

    caselist = cursor.execute('SELECT LC_ID,LT FROM tbLoadCon2').fetchall()
    for li in caselist:
        if li[1] not in ltlist:
            fList.append({'LT':li[1],'LC':[li[0],]})
            ltlist.append(li[1])
            calist.append(li[0])
        else:
            if li[0] not in calist:
                fList[ltlist.index(li[1])]['LC'].append(li[0]) 
                calist.append(li[0])
            else:
                continue

    caselist = cursor.execute('SELECT LC_ID,LT FROM tbLoadCon3').fetchall()
    for li in caselist:
        if li[1] not in ltlist:
            fList.append({'LT':li[1],'LC':[li[0],]})
            ltlist.append(li[1])
            calist.append(li[0])
        else:
            if li[0] not in calist:
                fList[ltlist.index(li[1])]['LC'].append(li[0]) 
                calist.append(li[0])
            else:
                continue
    #将fList内的'LC_ID'替换为outlist中的元素
    i = 0
    while i < len(fList):
        j = 0
        while j < len(fList[i]['LC']):
            if fList[i]['LC'][j] in idlist:
                fList[i]['LC'][j] = outlist[idlist.index(fList[i]['LC'][j])]
            else:
                fList[i]['LC'][j] = []
            j += 1
        i += 1
    
    return fList