#import flask
from flask import Flask, request, jsonify

#시작: 모듈명을 __name__으로 넘기고 app이라는 객체 생성
app = Flask(__name__)

#경로 입력 ('/': 시작페이지)
@app.route('/')
#뷰 함수: URL호출 시 호출되는 함수
def hello():
    return 'Hello Flask'

@app.route('/animal', methods=['POST'])
def animal():
    req = request.get_json()
    animal_type = req["action"]["detailParams"]["Animal_type"]["value"]	# json파일 읽기
    answer = animal_type
    
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)