from flask import Flask,request,jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

# 동아리 회비 안내
@application.route("/fee",methods=['POST'])
def fee():
    
    req = request.get_json()    # 신입생인지 재학생인지 request로 구분

    userRes = req["userRequest"]["utterance"]   #사용자 발화 저장 -> 사용자가 챗봇 채팅방에 친 명령어 -> 이걸로 유사도 검사해서 
    member_type = req["action"]["clientExtra"]["member_type"]	#바로가기 parameter 저장
    
    # 그냥 parameter도 저장할 수 있었는데 기억이 안나요

    fee = 0     # 회비 저장용 변수
    
    # request에서 파싱한 정보를 바탕으로 학생 구분해서 fee 에 알맞은 회비 저장
    if member_type == "신입생":
        fee = 20000
    elif member_type == "재학생":
        fee = 20000
    
    # 출력 양식 -> simpleText, simpleImage 등 여러가지 양식 있음
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        # 동아리 회비 안내 -> fee 는 정수형 변수라서 str(fee)로 형변환
                        "text": "[동아리 회비]\n"+member_type+" : " + str(fee) + "원"    
                    }
                }
            ]
        }
    }
    
    return jsonify(res) # json 형식으로 리턴

# Wi-Fi 비밀번호 안내
@application.route("/wifi",methods=['POST'])
def Wifi():
    req = request.get_json()
    
    # 결과 출력
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "Wi-Fi name : 어서와코딩은처음이지 (5G)\nPassword : 518interface"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)