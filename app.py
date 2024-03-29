from flask import Flask, request, abort
from events.winmai import *
from events.weather import *
from events.crawler import *
from events.push_msg import *
# from flask_mysqldb import MySQL
from pymysql import *
from flask_sqlalchemy import SQLAlchemy
from line_bot_api import *
# from extensions import db, migrate

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' \
                                        'line_assistant_user:820820@localhost:3306' \
                                        '/db_line_assistant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/')
def home():
    return 'This is test page.'


@app.route('/db')
def db():
    command = "SELECT * FROM crawler_log WHERE NAME='chickpt'"
    data = db.engine.execute(command)
    # print(data)
    return 'ok'


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
    if message_text[:7] == 'weather':
        weather(event, message_text)
    if message_text == 'uid':
        push_msg(event)

    if message_text != '':
        line_bot_api.reply_message(event.reply_token, message_text) 
    # if message_text == 'breathe_chickpt':
        # breathe_chickpt(event)


if __name__ == '__main__':
    app.debug = True
    app.run()
