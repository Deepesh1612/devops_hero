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


import csv

with open('newemploy.csv', mode='w') as file:
    csvfile = csv.reader(file)

    for lines in csvfile:
        print(lines)




# import csv

# with open('employ.csv', mode='r') as file:
#     csvfile = csv.reader(file)

#     for lines in csvfile:
#         print(lines)

# from flask import Flask, request, jsonify 

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def helloWorld():
#     return 'Hello World'

# @app.route('/aboutus')
# def extra():
#     return 'this is about us page'

# @app.route('/contactus', methods=['POST'])
# def contactus():
#     return 'this is contact us page'

# @app.route('/course')
# def course():
#     return 'this is about us page'

# if __name__ == '__main__':
#     app.run(port=3000, debug=True)
