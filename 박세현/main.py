from flask import Flask, request, jsonify
from res import RES

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello goorm!" #구름 서버 사용



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
    
    text = "[동아리 회비]\n" + member_type + " : " + str(fee) + "원"
    
    res = RES(text)
    
    return jsonify(res)

# Wi-Fi 비밀번호 안내
@application.route("/wifi",methods=['POST'])
def wifi():

    req = request.get_json()
    
    text = "Wi-Fi name : 어서와코딩은처음이지 (5G)\nPassword : 518interface"
    
    res = RES(text)
    
    
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
    
    
    res = RES(text)
        
    return jsonify(res)


# 동아리 재실 인원 안내
@application.route("/peoplenum",methods=['POST'])
def peoplenum():
    
    pnum = 1	# DB에서 값 가져오기
    
    text="현재 동아리방 재실 인원 : " + str(pnum)
    
    res = RES(text)
        
    return jsonify(res)



# 동아리방 위치 안내
@application.route("/clubroom",methods=['POST'])
def clubroom():
    
    text = "동아리방 위치 : 세종대학교 학생회관 518호\nhttps://naver.me/F6mxi8mf"
    
    res = RES(text)
    
    return jsonify(res)


# Interface introduction
@application.route("/introduction",methods = ['POST'])
def introduction():
    req = request.get_json()
    
    text= "세종대학교 중앙동아리 인터페이스 연혁"
    
    res = RES(text)
    
    return jsonify(res)
    

# Interface activity schedule
@application.route("/schedule",methods = ['POST'])
def schedule():
    req = request.get_json()
    
    text = "프로젝트 전시회"
    
    res = RES(text)
    
    return jsonify(res)


# Information on the number of people Interface members
@application.route("/people",methods = ['POST'])
def people():
    req = request.get_json()
    
    generation_type = req["action"]["detailParams"]["generation_type"]["value"]
    
    people = 0
    
    if generation_type == "30기":
        people = 10
    elif generation_type == "31기":
        people = 20
    elif generation_type == "32기":
        people = 34
    elif generation_type == "33기":
        people = 45
    elif generation_type == "34기":
        people = 50
    elif generation_type == "35기":
        people = 70
    
    
    text = "[기수별 인원 수]\n" + generation_type + " : " +str(people) + "명"
    
    res = RES(text)
    
    return jsonify(res)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)
