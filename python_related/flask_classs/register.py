from flask import Flask, request, jsonify
import csv
app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    print(request.get_json())
    data = request.get_json()
    username = data['name']
    password = data['pass']
    age = data['age']
    department = data['depart']

    print(username)
    if username=='deepesh' and password=='deepesh123':
        with open('newemploy.csv', mode='r') as file:
        csvfile = csv.reader(file)

    else:
            return 'Incorrect Credentials'

if __name__=='__main__':
    app.run(port=3000,debug=True)



    for lines in csvfile:
        print(lines)

