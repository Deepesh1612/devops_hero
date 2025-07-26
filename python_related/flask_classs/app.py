from flask import Flask
app=Flask(__name__)

@app.route('/',methods=['GET'])
def helloworld():
    return 'Hello World'

@app.route('/aboutus')
def aboutus():
    return 'This is about US'

@app.route('/contactus',methods=['POST'])
def contactus():
    return 'This is contact US'

if __name__=='__main__':
    app.run(port=3000,debug=True)

