from flask import Flask,request,jsonify

app = Flask(__name__)


@app.route("/")
def start():
    return "Hello goorm!"

@app.route("/fee",methods=['POST'])
def fee():
    # ���Ի����� ���л����� request�� ����
    req = request.get_json()
    
    member_type = req["action"]["detailParams"]["Member_type"]["value"]	
    
    fee = 0
    
    if member_type == "���л�":
        fee = 20000
    elif member_type == "���Ի�":
        fee = 20000
    else :
        fee = 0
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "[���Ƹ� ȸ��] ���Ի� : 20000��, ���л� : 20000��",
                        "request": req
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

@app.route("/hello",methods=['POST'])
def hello():
    # ���Ի����� ���л����� request�� ����
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

#�������̽� �Ұ�
@app.route("/intro",methods=['POST'])
def intro():
    
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "�ȳ��ϼ��� �������б� �߾ӵ��Ƹ� �������̽��Դϴ�."
                    }
                }
            ]
        }
    }
    
    return jsonify(res)

# �������̽� �����䰭
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
    if(userReq == "�׽�Ʈ"):
        res['outputs']['simpletext']['link'] = "text"
    
    return res
    

if __name__ == "__main__":
    chatbot.run(host='0.0.0.0', port=5000, threaded=True)