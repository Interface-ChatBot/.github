from flask import Flask,request,jsonify

application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello goorm!"

# ���Ƹ� ȸ�� �ȳ�
@application.route("/fee",methods=['POST'])
def fee():
    
    req = request.get_json()    # ���Ի����� ���л����� request�� ����

    userRes = req["userRequest"]["utterance"]   #����� ��ȭ ���� -> ����ڰ� ê�� ä�ù濡 ģ ��ɾ� -> �̰ɷ� ���絵 �˻��ؼ� 
    member_type = req["action"]["clientExtra"]["member_type"]	#�ٷΰ��� parameter ����
    
    # �׳� parameter�� ������ �� �־��µ� ����� �ȳ���

    fee = 0     # ȸ�� ����� ����
    
    # request���� �Ľ��� ������ �������� �л� �����ؼ� fee �� �˸��� ȸ�� ����
    if member_type == "���Ի�":
        fee = 20000
    elif member_type == "���л�":
        fee = 20000
    
    # ��� ��� -> simpleText, simpleImage �� �������� ��� ����
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        # ���Ƹ� ȸ�� �ȳ� -> fee �� ������ ������ str(fee)�� ����ȯ
                        "text": "[���Ƹ� ȸ��]\n"+member_type+" : " + str(fee) + "��"    
                    }
                }
            ]
        }
    }
    
    return jsonify(res) # json �������� ����

# Wi-Fi ��й�ȣ �ȳ�
@application.route("/wifi",methods=['POST'])
def Wifi():
    req = request.get_json()
    
    # ��� ���
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

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)