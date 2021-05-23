import pypyodbc
from werkzeug.security import check_password_hash, generate_password_hash

DRIVER = 'Microsoft Access Driver (*.mdb)'
DBQ = 'C:/Users/Jayus/Desktop/RPVdb/server/instance/Users.mdb'
PWD = '123456'         #密码明示，应优化
pypyodbc.lowercase = False
db = pypyodbc.win_connect_mdb('Driver={};DBQ={};PWD={}'.format(DRIVER,DBQ,PWD))
cursor = db.cursor()
username = 'user1'
password = '123321'
cursor.execute('INSERT INTO users (USERNAME, PASSWORD) VALUES (?, ?)',
                (username, generate_password_hash(password)))
cursor.commit()