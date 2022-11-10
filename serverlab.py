from flask import Flask

bcs = Flask(__name__)

@bcs.route("/")
def hello_world():
    return "<p>Hello, World!</p>"