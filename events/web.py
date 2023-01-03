from line_bot_api import *
import requests


def weather(event):
    city = 'tainan'
    api_key = 'b85f1d04ed29cb2e9f8acc9c041658b0'
    address = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    data = requests.get(address)
    print(round(data.json()['main']['temp'] - 273.15, 2))
    template = round(data.json()['main']['temp'] - 273.15, 2)

    text_message = TextSendMessage(f'現在{city}的溫度是{template}°C')
    line_bot_api.reply_message(event.reply_token, text_message)
