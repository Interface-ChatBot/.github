import pymysql
import mysql_user_info
import n_gram

#데이터 베이스에서 데이터 가져오기
def fetch():
    with pymysql.connect(db=user['db'], host=user['host'], user=user['user'], passwd=user['passwd'], port=user['port'], charset=user['charset']) as db:
        with db.cursor(pymysql.cursors.DictCursor) as cur:
            sql = 'SELECT * FROM command_list'
            cur.execute(sql)
            db.commit()

            data = cur.fetchall()

    return data

user = mysql_user_info.user_info
data = fetch()

#유저 입력
user_input = input()
user_input_ngram = n_gram.ngram(n_gram.n_list(user_input), 2)

#데이터베이스 데이터 값과 비교
for i in data:
    command_ngram = n_gram.ngram(n_gram.n_list(i['command']), 2)
    similarity = n_gram.similarity(user_input_ngram, command_ngram)
    print(similarity)