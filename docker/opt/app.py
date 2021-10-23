from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    greeting = "Hello World"
    return greeting
