from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Fuck off you cunt!"

@app.route('/command/<param>')
def command(param):
    return param
