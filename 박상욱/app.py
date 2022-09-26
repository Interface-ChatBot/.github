from flask import Flask,request,jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

@application.route("/fee",methods=['POST'])
def fee():
    
    req = request.get_json()

    userRes = req["userRequest"]["utterance"]	 				#?ъ슜??諛쒗솕 ???
    member_type = req["action"]["clientExtra"]["member_type"]	#諛붾줈媛湲?parameter ???
        
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
                        "text": "동아리 회비\n" + member_type + " : " + str(fee) + "원",
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

@application.route("/wifi",methods=['POST'])
def wifi():
    req = request.get_json()
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "Wi-Fi name : 어서와코딩은처음이지? (5G)\nPassword : 518interface"
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
    
    if userRes == "?ъ떎":
        # DB ?ъ떎?몄썝 利앷?
        pnum += 1
        
    elif userRes == "?댁떎":
        # DB ?ъ떎?몄썝 媛먯냼
        pnum += -1
            
    text = "?꾩옱 ?ъ떎 ?몄썝? " + str(pnum) + "紐??낅땲??"
    
    # 6?쒖뿉 ?ъ떎?몄썝 0?쇰줈 珥덇린??
    
    
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
    
    pnum = 1	# DB?먯꽌 媛?媛?몄삤湲?
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "?꾩옱 ?숈븘由щ갑 ?ъ떎 ?몄썝 : " + str(pnum)
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
                        "text": "동아리방 위치 : 세종대하굑 학생회관 518호\nhttps://naver.me/F6mxi8mf"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


if __name__ == "__main__":
    # application.run(host='10.128.0.2', port=5000, threaded=True)
    application.run(host='0.0.0.0', port=5000, threaded=True)