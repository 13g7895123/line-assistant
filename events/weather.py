from line_bot_api import *
import requests


def weather(event, message_text):

    city = message_text.split('-')[1]
    api_key = 'b85f1d04ed29cb2e9f8acc9c041658b0'
    address = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    try:
        data = requests.get(address)
        print(round(data.json()['main']['temp'] - 273.15, 2))
        template = round(data.json()['main']['temp'] - 273.15, 2)
        msg = f'現在{city}的溫度是{template}°C'
    except Exception as e:
        msg = f'查詢錯誤，請確認城市名稱'

    text_message = TextSendMessage(msg)
    line_bot_api.reply_message(event.reply_token, text_message)
