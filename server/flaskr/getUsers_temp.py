import pypyodbc
from werkzeug.security import check_password_hash, generate_password_hash

DRIVER = 'Microsoft Access Driver (*.mdb)'
DBQ = '../instance/RPV-Simulation.mdb'
PWD = '123456'         #密码明示，应优化
pypyodbc.lowercase = False
db = pypyodbc.win_connect_mdb('Driver={};DBQ={};PWD={}'.format(DRIVER,DBQ,PWD))
cursor = db.cursor()
#sql = "INSERT INTO tbStrucGeom1 (D1,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D2,D3,D4,D5,D6,D7,D8,D9,L1,L2,R1,R3,R4,SG_ID,SR2,h1,h2,h3,h4,h5,h6,h7,h8,m,n,t1,t2,θ) VALUES ('4000','4684','4071.7','4085.11','3989.1','4002.58','4007','4164','4158','149.5','216','4350','4674','3000','105','162','3925.8','3799','3951','16.5','11.7','400','150','120','SG-new111','2035','200','850','600','279.4','136','0.66','280','200','58','64','164','234','19.77')"

def delete(cursor,table_name,index,column):
    sql = 'DELETE FROM ' + table_name + ' WHERE ' + column + '=' + "'" + index + "'"
    cursor.execute(sql)

sql = "DELETE FROM tbStrucGeom1 WHERE ID=?"
cursor.execute(sql,(137,))
cursor.commit()
cursor.close()

