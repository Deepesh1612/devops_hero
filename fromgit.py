from flask import Flask

fromgit = Flask(__name__)

@fromgit.route('/',methods=['GET'])
def helloworld():
    return 'hello world from git'

@fromgit.route('/',methods=['POST'])
def helloworld():
    return 'About Us'

if __name__=="__main__":
    fromgit.run(port=3000,debug=True)