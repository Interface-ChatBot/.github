import pymysql
import mysql_user_info

#데이터 베이스에서 데이터 가져오기
def _fetch():
    with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'], charset=_user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'SELECT * FROM wifi'
            cur.execute(sql)
            db.commit()

            data = cur.fetchall()

    return data

#[{name:'name', pw:'pw'}] 형식의 딕셔너리 리스트 형식으로 wifi 비밀번호 반환
def wifi():
    data = _fetch()

    return data

_user = mysql_user_info.user_info


#예시
'''
from wifi_pw import *

Wifi = wifi()

#출력예시
for i in Wifi:
    print(f'{i["name"]} {i["pw"]}')
'''