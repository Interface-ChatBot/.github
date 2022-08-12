#import flask
from flask import Flask

#시작: 모듈명을 __name__으로 넘기고 app이라는 객체 생성
app = Flask(__name__)

#경로 입력 ('/': 시작페이지)
@app.route('/')
#뷰 함수: URL호출 시 호출되는 함수
def hello():
    return 'Hello Flask'

@app.route('/login')
def login():
    return 'Login'

if __name__ == '__main__':
    #flask앱 실행 
    app.run()