def push_msg(event):
    uid = event.source.userId

    text_message = TextSendMessage(uid)
    line_bot_api.reply_message(event.reply_token, text_message)