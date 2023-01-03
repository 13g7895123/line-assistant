from line_bot_api import *
import hashlib
import datetime


def socket(event):
    # 當天日期
    today = datetime.datetime.now().strftime('%Y%m%d')
    # 轉換密碼
    pwd = str(today) + '45894216'
    # 加密取得SOCKET密碼
    sha512_str = hashlib.sha512(str(pwd).encode('utf-8')).hexdigest()
    # 透過LINE回傳
    text_message = TextSendMessage(sha512_str)
    line_bot_api.reply_message(event.reply_token, text_message)
