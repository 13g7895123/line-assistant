from flask import Flask, request, abort
from events.winmai import *
from events.crawler import *
from flask_mysqldb import MySQL

app = Flask(__name__)

mysql = MySQL()
mysql.init_app(app)
app.config['MYSQL_USER'] = 'user_name'
app.config['MYSQL_PASSWORD'] = 'user_password'
app.config['MYSQL_HOST'] = 'sql3.example.net'
app.config['MYSQL_DB'] = 'Database_name'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def home():
    return 'This is test page.'


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # LINE傳過來的訊息
    message_text = str(event.message.text).lower()

    if message_text == 'socket':
        socket(event)
    if message_text == 'breathe_chickpt':
        breathe_chickpt(event)


if __name__ == '__main__':
    app.run()
