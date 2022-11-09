from flask import Flask, request, abort
from line_bot_api import *
from events.winmai import *
from events.crawler import *

app = Flask(__name__)


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
    if message_text == 'breath_chickpt':
        breathe_chickpt(event)


if __name__ == '__main__':
    app.run()
