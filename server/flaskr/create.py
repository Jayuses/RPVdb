#!/RPVdb/server/flaskr/create.py
# -*- conding: utf-8 -*-
# 蓝图文件'create.py',创建数据

import functools
from flask import (
    Blueprint, request
    )
from flaskr.db import get_db
from flask import Flask, jsonify

casedata = {'status':None}

bp = Blueprint('create', __name__, url_prefix='/create')

@bp.route('/case',methods=['POST','GET'])
def create_case():
    '''在创建tbCaseStrucX中创建案例'''
    response_status = 0;
    if request.method == 'POST':
        case = request.get_json()
        CaseID = case.get('CaseID')
        caseinfo = case.get('caseinfo')
        db = get_db()
        cursor = db.cursor()
        sql1 = 'SELECT ID from tbCasesStruc'+str(caseinfo['style'])+' WHERE CaseID='+"'"+CaseID+"'"
        id = cursor.execute(sql1).fetchone()
        if id:
            casedata['status'] = 2
        else:
            sql2 = 'INSERT INTO tbCasesStruc'+str(caseinfo['style'])+\
                ' (CaseID,SG_ID,LC_ID,MHead,MHeadAM,MRPV,MRPVAM,MBolt,MBoltAM,MLayer,MLayerAM)'+\
                'VALUES (?,?,?,?,?,?,?,?,?,?,?)'
            cursor.execute(sql2,(CaseID,caseinfo['SG_ID'],caseinfo['LC_ID'],
                                 caseinfo['MHead'][0],caseinfo['MHead'][1],
                                 caseinfo['MRPV'][0],caseinfo['MRPV'][1],
                                 caseinfo['MBolt'][0],caseinfo['MBolt'][1],
                                 caseinfo['MLayer'][0],caseinfo['MLayer'][1]))
            cursor.commit()
            casedata['status'] = 1
        cursor.close()
    else:
        response_status = casedata['status']
    return jsonify(response_status)

@bp.route('/geom',methods=['POST','GET'])
def create_geom():
    '''在tbStrucGeom中创建结构尺寸库'''
    response_status = 0;
    if request.method == 'POST':
        geom = request.get_json()
        geomData = geom.get('newGeom')
        geomStyle = geom.get('style')
        db = get_db()
        cursor = db.cursor()
        sql1 = 'SELECT ID from tbStrucGeom'+str(geomStyle)+' WHERE SG_ID='+"'"+geomData['SG_ID']+"'"
        id = cursor.execute(sql1).fetchone()
        sgid = geomData.pop('SG_ID')
        if id:
            pass
        else:
            sql1 = 'INSERT INTO tbStrucGeom'+str(geomStyle)+'(SG_ID) VALUES (?)'
            cursor.execute(sql1,(sgid,))
        for key,value in geomData.items():
            val = value
            if key == 'ID':
                continue
            sql = 'UPDATE tbStrucGeom'+str(geomStyle)+' SET '+key+'=?'+' WHERE SG_ID='+"'"+sgid+"'"
            if isinstance(val,str):
                val = float(val)
            cursor.execute(sql,(val,))        
        cursor.commit()
        casedata['status'] = 1
        cursor.close()
    else:
        response_status = casedata['status']
    return jsonify(response_status)        

@bp.route('/load',methods=['POST','GET'])
def create_load():
    '''在tbLoadCon中创建加载工况,在tbLoadTP中创建温度压力'''
    response_status = 0;
    if request.method == 'POST':
        load = request.get_json()
        loadCon = load.get('newCon')
        loadStyle = load.get('style')
        loadTP = load.get('newTP')
        db = get_db()
        cursor = db.cursor()

        sql1 = 'SELECT ID from tbLoadCon'+str(loadStyle)+' WHERE LC_ID='+"'"+loadCon['LC_ID']+"'"
        id = cursor.execute(sql1).fetchone()
        lcid = loadCon.pop('LC_ID')
        if id:
            pass
        else:
            sql1 = 'INSERT INTO tbLoadCon'+str(loadStyle)+'(LC_ID) VALUES (?)'
            cursor.execute(sql1,(lcid,))
        for key,value in loadCon.items():
            val = value
            if key == 'ID':
                continue
            sql = 'UPDATE tbLoadCon'+str(loadStyle)+' SET '+key+'=?'+' WHERE LC_ID='+"'"+lcid+"'"
            if isinstance(val,str) and key!='LT':
                val = float(val)
            cursor.execute(sql,(val,))

        sql2 = 'DELETE FROM tbLoadTP'+str(loadStyle)+' WHERE LC_ID='+"'"+lcid+"'"
        cursor.execute(sql2)
        for item in loadTP:
            sql2 = 'INSERT INTO tbLoadTP'+str(loadStyle)+' (LC_ID,[Time],Temperature,Pressure) VALUES (?,?,?,?)'
            cursor.execute(sql2,(lcid,float(item['time']),float(item['T']),float(item['p'])))
        
        cursor.commit()
        casedata['status'] = 1
        cursor.close()
    else:
        response_status = casedata['status']
    return jsonify(response_status)

@bp.route('/mater',methods=['POST','GET'])
def create_mater():
    '''创建材料库'''
    response_status = 0;
    if request.method == 'POST':
        mater = request.get_json()
        materData = mater.get('newData')
        MaterID = mater.get('newMater')
        db = get_db()
        cursor = db.cursor()
        id = cursor.execute('SELECT ID FROM tbMater WHERE MaterID='+"'"+MaterID+"'").fetchone()
        if id:
            pass
        else:
            cursor.execute("INSERT INTO tbMater (MaterID) VALUES (?)",(MaterID,))
        for key,value in materData.items():
            mater_mod(MaterID,value,cursor,key)
        cursor.commit()
        casedata['status'] = 1
        cursor.close()
    else:
        response_status = casedata['status']
    return jsonify(response_status)

def mater_mod(MaterID,data,cursor,key):
    if len(data) == 1 and (data[0]['T'] == '' or data[0]['value'] == ''):
        pass
    else:
        sql1 = "DELETE FROM tb"+key+" WHERE MaterID="+"'" + MaterID + "'"
        cursor.execute(sql1)
        sql2 = "INSERT INTO tb"+key+" (MaterID,Temperature,Variable) VALUES (?,?,?)"
        for item in data:
            if key == 'Density':
                data_tuple = (MaterID,float(item['T']),float(item['value'])*1e-10)
            else:
                data_tuple = (MaterID,float(item['T']),float(item['value']))
            cursor.execute(sql2,data_tuple)