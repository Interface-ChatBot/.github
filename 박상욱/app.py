from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/")
def start():
    return "Hello goorm!"

@app.route("/fee",methods=['POST'])
def fee():
    # 신입생인지 재학생인지 request로 구분
    req = request.get_json()
    
    member_type = req["action"]["detailParams"]["Member_type"]["value"]	
    
    fee = 0
    
    if member_type == "재학생":
        fee = 20000
    elif member_type == "신입생":
        fee = 20000
    else :
        fee = 0
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "[동아리 회비] 신입생 : 20000원, 재학생 : 20000원",
                        "request": req
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

@app.route("/hello",methods=['POST'])
def hello():
    # 신입생인지 재학생인지 request로 구분
    req = request.get_json()
    
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "Hello KakaoTalk"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

#인터페이스 소개
@app.route("/intro",methods=['POST'])
def intro():
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕하세요 세종대학교 중앙동아리 인터페이스입니다."
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

# 인터페이스 모집요강
@chatbot.route("/guide",methods=['POST'])
def guide():
    
    body = request.get_json()
    userReq = body['userRequest']['utterance']    
    res = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "link": "https://sejong-interface.github.io/"
                        }
                    }
                ]
            }
        }   
    if(userReq == "테스트"):
        res['outputs']['simpletext']['link'] = "text"
    
    return res
    

if __name__ == "__main__":
    chatbot.run(host='0.0.0.0', port=5000, threaded=True)