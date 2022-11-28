import pymysql
import mysql_user_info

#데이터 베이스에서 데이터 가져오기
def _fetch():
    with pymysql.connect(db=_user['db'], host=_user['host'], user=_user['user'], passwd=_user['passwd'], port=_user['port'], charset=_user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'SELECT * FROM member'
            cur.execute(sql)
            db.commit()

            data = cur.fetchall()

    return data

#이름, 학번을 [학번 이름] 리스트 형식으로 member_check 함수에 넣었을 경우 DB 안에 있는 데이터 중 이름과 학번이 정확하게 일치하면 1을 반환, 아닐시 0을 반환
def member_check(user_input):
    data = _fetch()

    c = 0
    for i in data:
        if i['name'] == user_input[0] and i['id'] == int(user_input[1]):
            c = 1
            break

    return c

_user = mysql_user_info.user_info


#예시
'''
from member_check import

cnt = member_check(input().split(' '))
'''