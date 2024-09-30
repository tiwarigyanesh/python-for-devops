from flask import Flask
#create flask app instance
app= Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World!'

# try this simple sample app to run on ec2 instance
app.run('0.0.0.0')