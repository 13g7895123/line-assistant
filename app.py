
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '234'

@app.route('/.well-known/pki-validation/<string:text_name>/')
def ssl_test(str):
    return '2344'

@app.route('/.well-known/pki-validation/EB8B3233208300C9948562303D9F3A84.txt/')
def EB8B3233208300C9948562303D9F3A84():
    return render_template("EB8B3233208300C9948562303D9F3A84.txt")

if __name__ == '__main__':
    app.run()
