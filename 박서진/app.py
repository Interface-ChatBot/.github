from flask import Flask
from flask_cors import CORS
app = Flask(__name__)

#URL
@app.route('/')
def hello():
    return 'Hello Flask'

# Information on the number of people Interface members
@app.route('/people')
def people():
    data =  {
        "30th": "10",
        "31st": "20",
        "32nd": "34",
        "33rd": "45",
        "34th": "50",
        "35th": "70"
    }
    return data
    
# Interface introduction
@app.route('/introduction')
def introduction():
    return {
        "Founding Date": "1989.08"
    }

# Interface requirements
@app.route('/require')
    
@app.route('/login')
def login():
    return 'Login'

if __name__ == '__main__':
    app.run()