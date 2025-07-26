from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/login',methods=['POST'])
def login():
    print(request.get_json())
    data = request.get_json()
    username = data['name']
    password = data['pass']
    print(username)
    if username=='deepesh' and password=='deepesh123':
            return 'login successfull'
    else:
            return 'Incorrect Credentials'


if __name__=='__main__':
    app.run(port=3000,debug=True)