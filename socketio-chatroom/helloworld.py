#coding:utf-8

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/123")
def hello2():
    return "ni hao"

if __name__ == "__main__":
    app.run()