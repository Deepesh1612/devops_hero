from flask import Flask

fromgit = Flask(__name__)

@fromgit.route('/',methods=['GET'])
def helloworld():
    return 'hello world from git'

if __name__=="__main__":
    fromgit.run(port=3000,debug=True)