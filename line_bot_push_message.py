from line_bot_api import *


def push_msg(uid, msg):
    line_bot_api.push_message(uid, TextSendMessage(text=msg))
