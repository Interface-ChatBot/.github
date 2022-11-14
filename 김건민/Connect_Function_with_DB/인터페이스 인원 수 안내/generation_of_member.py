import pymysql
import mysql_user_info

#데이터 베이스에서 데이터 가져오기
def _fetch():
    with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'], charset=_user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'SELECT * FROM generation'
            cur.execute(sql)
            db.commit()

            data = cur.fetchall()

    return data

#기수별 인원수를 [{generation:기수, num:인원수}] 형식의 딕셔너리 리스트로 반환
def generation():
    data = _fetch()

    return data

_user = mysql_user_info.user_info

'''
from generation_of_member import *

generation = generation()

for l in generation:
    print(f'Generation : {l["generation"]} | Number : {l["num"]}')
'''