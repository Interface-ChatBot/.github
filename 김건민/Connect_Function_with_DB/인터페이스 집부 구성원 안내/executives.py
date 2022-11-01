import pymysql
import mysql_user_info

#데이터 베이스에서 데이터 가져오기
def _fetch():
    with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'], charset=_user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'SELECT * FROM executives'
            cur.execute(sql)
            db.commit()

            data = cur.fetchall()

    return data

#임원진 정보를 [{name:'name', position:'position', email:'email'}] 형식의 딕셔너리 리스트로 반환
def executives():
    data = _fetch()

    return data

_user = mysql_user_info.user_info

#예시
'''
from executives import *

executives = executives()

#출력예시
for e in executives:
    print(f'Name : {e["name"]} | Position : {e["position"]} | Email : {e["email"]}')'''