# -*- coding: euc-kr -*-

from flask import Flask,request,jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

# 동아리 회비 안내
@application.route("/fee",methods=['POST'])
def fee():
    # 신입생인지 재학생인지 request로 구분
    
    req = request.get_json()

    userRes = req["userRequest"]["utterance"]	 				#사용자 발화 저장
    member_type = req["action"]["clientExtra"]["member_type"]	#바로가기 parameter 저장
        
    fee = 0
    
    if member_type == "신입생":
        fee = 20000
    elif member_type == "재학생":
        fee = 20000
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "[동아리 회비]\n"+member_type+" : " + str(fee) + "원",
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

# Wi-Fi 비밀번호 안내
@application.route("/wifi",methods=['POST'])
def wifi():
    req = request.get_json()
    
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

# 동아리 재실 / 퇴실 여부 체크
@application.route("/isroom",methods=['POST'])
def isroom():
    
    req = request.get_json()
    
    userRes = req["userRequest"]["utterance"]	 #사용자 발화 저장
    
    pnum = 0	#DB에서 가져오기
    text = ""
    
    if userRes == "재실":
        # DB 재실인원 증가
        pnum += 1
        
    elif userRes == "퇴실":
        # DB 재실인원 감소
        pnum += -1
            
    text = "현재 재실 인원은 " + str(pnum) + "명 입니다."
    
    # 6시에 재실인원 0으로 초기화
    
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ]
        }
    }
        
    return jsonify(res)



# 동아리 재실 인원 안내
@application.route("/peoplenum",methods=['POST'])
def peoplenum():
    
    pnum = 1	# DB에서 값 가져오기
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "현재 동아리방 재실 인원 : " + str(pnum)
                    }
                }
            ]
        }
    }
        
    return jsonify(res)



# 동아리방 위치 안내
@application.route("/clubroom",methods=['POST'])
def clubroom():
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "동아리방 위치 : 세종대학교 학생회관 518호\nhttps://naver.me/F6mxi8mf"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


if __name__ == "__main__":
    application.run(host='10.128.0.2', port=5000, threaded=True)