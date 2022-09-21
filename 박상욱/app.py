# -*- coding: euc-kr -*-

from flask import Flask,request,jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

# ���Ƹ� ȸ�� �ȳ�
@application.route("/fee",methods=['POST'])
def fee():
    # ���Ի����� ���л����� request�� ����
    
    req = request.get_json()

    userRes = req["userRequest"]["utterance"]	 				#����� ��ȭ ����
    member_type = req["action"]["clientExtra"]["member_type"]	#�ٷΰ��� parameter ����
        
    fee = 0
    
    if member_type == "���Ի�":
        fee = 20000
    elif member_type == "���л�":
        fee = 20000
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "[���Ƹ� ȸ��]\n"+member_type+" : " + str(fee) + "��",
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

# Wi-Fi ��й�ȣ �ȳ�
@application.route("/wifi",methods=['POST'])
def wifi():
    req = request.get_json()
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "Wi-Fi name : ����ڵ���ó������ (5G)\nPassword : 518interface"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

# ���Ƹ� ��� / ��� ���� üũ
@application.route("/isroom",methods=['POST'])
def isroom():
    
    req = request.get_json()
    
    userRes = req["userRequest"]["utterance"]	 #����� ��ȭ ����
    
    pnum = 0	#DB���� ��������
    text = ""
    
    if userRes == "���":
        # DB ����ο� ����
        pnum += 1
        
    elif userRes == "���":
        # DB ����ο� ����
        pnum += -1
            
    text = "���� ��� �ο��� " + str(pnum) + "�� �Դϴ�."
    
    # 6�ÿ� ����ο� 0���� �ʱ�ȭ
    
    
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



# ���Ƹ� ��� �ο� �ȳ�
@application.route("/peoplenum",methods=['POST'])
def peoplenum():
    
    pnum = 1	# DB���� �� ��������
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "���� ���Ƹ��� ��� �ο� : " + str(pnum)
                    }
                }
            ]
        }
    }
        
    return jsonify(res)



# ���Ƹ��� ��ġ �ȳ�
@application.route("/clubroom",methods=['POST'])
def clubroom():
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "���Ƹ��� ��ġ : �������б� �л�ȸ�� 518ȣ\nhttps://naver.me/F6mxi8mf"
                    }
                }
            ]
        }
    }
    
    return jsonify(res)


if __name__ == "__main__":
    application.run(host='10.128.0.2', port=5000, threaded=True)