from line_bot_api import *

def push_msg(event):
    # uid = event.source.userId

    text_message = TextSendMessage('123')
    line_bot_api.reply_message(event.reply_token, text_message)