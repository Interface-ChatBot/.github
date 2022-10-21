from flask import Flask,request,jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/fee",methods=['POST'])
def fee():
    
    req = request.get_json()

    userRes = req["userRequest"]["utterance"]	 				#??????꾩룇裕??????
    member_type = req["action"]["clientExtra"]["member_type"]	#?꾩룆?餓λ뛼泥???parameter ????
        
    fee = 0
    
    if member_type == "재학생":
        fee = 20000
    elif member_type == "신입생":
        fee = 20000
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "동아리 회비 안내\n" + member_type + " : " + str(fee) + "원"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


@application.route("/wifi",methods=['POST'])
def wifi():
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "Wi-Fi name : 어서와코딩은 처음이지 (5G)\nPassword : 518interface"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

''''
@application.route("/isroom",methods=['POST'])
def isroom():
    
    req = request.get_json()
    
    userRes = req["userRequest"]["utterance"]	 
    
    pnum = 0	
    text = ""
    
    if userRes == "????:
        # DB ????筌뤾쑴??嶺뚯빘鍮?
        pnum += 1
        
    elif userRes == "??怨룸펲":
        # DB ????筌뤾쑴???띠룆흮??
        pnum += -1
            
    text = "?熬곣뫗???????筌뤾쑴??? " + str(pnum) + "嶺????낅퉵??"
    
    # 6??戮?뱺 ????筌뤾쑴??0??怨쀬Ŧ ?貫?껆뵳??
    
    
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
 '''

'''
@application.route("/peoplenum",methods=['POST'])
def peoplenum():
    
    pnum = 1	# DB????????띠럾??筌뤾쑴沅롧뼨?
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "?熬곣뫗?????덊닡?洹먮맦而??????筌뤾쑴??: " + str(pnum)
                    }
                }
            ]
        }
    }
        
    return jsonify(res)
'''


@application.route("/clubroom",methods=['POST'])
def clubroom():
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "서울특별시 광진구 능동로 209 세종대학교 학생회관 518호\nhttps://naver.me/F6mxi8mf"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


if __name__ == "__main__":
    # application.run(host='10.128.0.2', port=5000, threaded=True)
    application.run(host='0.0.0.0', port=5000, threaded=True)