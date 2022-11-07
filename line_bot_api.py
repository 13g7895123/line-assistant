from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, LocationSendMessage,
    TemplateSendMessage, ImageCarouselTemplate, ImageCarouselColumn, PostbackAction, PostbackEvent, FlexSendMessage
)

line_bot_api = LineBotApi('cEGDrGy07K3K9qFq1TWwmSxSWxkZ8YpI5YvhJVh/'
                          'hbwH7znknhOnDsl5c22QhtIng36iFC2tmgFlMveBVmQSJXHTu1pmm0SsPvvlbzW9zBEn/'
                          'lvB1LkMa02so7rjGpNNj8aeBhuvwCbZGTllDtnzIwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('685e0b7340abee12679132c72c91efc2')