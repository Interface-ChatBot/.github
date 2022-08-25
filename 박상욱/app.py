from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#url
@app.route('/')
def index():
    return 'Hello Flask'

# membership fee
@app.route('/fee')
def fee():
    return {
        "freshman": "15000",
        "not freshman": "10000"
    }

@app.route('/login')
def login():
    return 'Login'

if __name__ == '__main__':
    app.run()