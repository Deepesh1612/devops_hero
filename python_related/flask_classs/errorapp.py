from flask import Flask, request, jsonify 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def helloWorld():
    return 'Hello World'

@app.route('/aboutus')
def extra():
    return 'this is about us page'

@app.route('/contactus', methods=['POST'])
def contactus():
    return 'this is contact us page'

@app.route('/course')
def course():
    return 'this is about us page'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
