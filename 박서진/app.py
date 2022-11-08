from flask import Flask, request, jsonify

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello goorm!"



# Interface introduction
@application.route("/introduction",methods = ['POST'])
def introduction():
    req = request.get_json()
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "인터페이스 소개\n" + "동아리 연혁 : 1988년\n"+ "주요 활동\n1. 동아리 자체 대회/ 전시회\n2. 다양한 스터디\n3. 소모임 활동"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)
    

# Interface activity schedule
@application.route("/schedule",methods = ['POST'])
def schedule():
    req = request.get_json()
    
    userRes = req["userRequest"]["utterance"]
    Month_type = req["action"]["clientExtra"]["Month_type"]
    
    dic = {"3월" : "1학기 개강총회, 신입생 환영회, 봄엠티", 
           "4월" : "스터디, 소모임",
           "5월" : "기엠티",
           "6월" : "게임 대회",
           "7월" : "1학기 종강총회",
           "8월" : "여름엠티 or 가을 엠티",
           "9월" : "2학기 개강총회",
           "10월" : "기타 행사(게임 대회, 상영 행사)",
           "11월" : "창립제",
           "12월" : "프로그래밍 전시회, 2학기 종강 총회"
          }
    
    if Month_type == "3월":
        schedule = dic["3월"]
    elif Month_type == "4월":
        schedule = dic["4월"]
    elif Month_type == "5월":
        schedule = dic["5월"]
    elif Month_type == "6월":
        schedule = dic["6월"]
    elif Month_type == "7월":
        schedule = dic["7월"]
    elif Month_type == "8월":
        schedule = dic["8월"]
    elif Month_type == "9월":
        schedule = dic["9월"]
    elif Month_type == "10월":
        schedule = dic["10월"]
    elif Month_type == "11월":
        schedule = dic["11월"]
    elif Month_type == "12월":
        schedule = dic["12월"]
        
    res = {
         "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": Month_type + " 동아리 일정 안내\n" + schedule
                    }
                }
            ]
        }
    }
    return jsonify(res)


# Information on the number of people Interface members
@application.route("/people",methods = ['POST'])
def people():
    req = request.get_json()
    
    userRes = req["userRequest"]["utterance"]
    Generation_type = req["action"]["clientExtra"]["Generation_type"]
    
    dic_gen = {30 : 10, 31 : 20, 32 : 34, 33 : 45, 34 : 50, 35 : 70}
    
    if Generation_type == "30기":
        people = dic_gen[30]
    elif Generation_type == "31기":
        people = dic_gen[31]
    elif Generation_type == "32기":
        people = dic_gen[32]
    elif Generation_type == "33기":
        people = dic_gen[33]
    elif Generation_type == "34기":
        people = dic_gen[34]
    elif Generation_type == "35기":
        people = dic_gen[35]
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "인터페이스 " + Generation_type + " : " + str(people) + "명"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


# Interface suggestion
@application.route("/suggestion",methods = ['POST'])
def suggestion():
    req = request.get_json()
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": ""
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)