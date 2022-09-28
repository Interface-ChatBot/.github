import pymysql
import mysql_user_info

#데이터 베이스에서 데이터 가져오기
def fetch():
    with pymysql.connect(db=user['db'], host=user['host'], user=user['user'], passwd=user['passwd'], port=user['port'], charset=user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'SELECT * FROM member'
            cur.execute(sql)
            db.commit()

            data = cur.fetchall()

    return data

#멤버 이름, 학번 확인 함수
def member_check(user_input):
    c = 0
    for i in data:
        if i['name'] == user_input[0] and i['id'] == int(user_input[1]):
            c = 1
            break

    return c

user = mysql_user_info.user_info
data = fetch()

#유저 입력
user_input = input().split(' ')

#member_check 호출
cnt = member_check(user_input)

#이름, 학번을 '학번 이름' 형식으로 입력했을시 member_check 함수를 통해 DB 안에 이름과 학번이 정확하게 일치하면 1을 반환, 아닐시 0을 반환