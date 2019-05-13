#架設伺服器
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('1eFV5ZsduXAASYETD9Cjv1k85pJnCpEX/fvkkuHDLUiKwdKBqUnJxs+Qymey6eIVvIVu1PfJ94OAOWEVP7U7evNY4ZEeYtCwODMe7TMOsRgJ5S6Bc5Lk54JHRaXnNryri8DZJPpq+vUbVz7ab5clqQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f3f641502b14084134b607008b1a9e6b')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #設定回覆訊息
    msg = event.message.text

    r = ' 我看不懂你說甚麼' #預設回覆訊息

    if '給我貼圖' in msg:
        Sticker_Message = StickerSendMessage(
            package_id='11537',
            sticker_id='52002738'
        )
        #line_bot_api.reply_message(event.reply_token, Sticker_Message)
        elif '哭哭' in msg:
            Sticker_Message = StickerSendMessage(
                package_id='11538',
                sticker_id='51626522'
            )
            #line_bot_api.reply_message(event.reply_token, Sticker_Message)
        elif msg in ['累', '死', '想睡']:
            Sticker_Message = StickerSendMessage(
                package_id='11537',
                sticker_id='52002757'
            )    
        line_bot_api.reply_message(
            event.reply_token, 
            Sticker_Message)

    if msg in ['hi', 'Hi', '安安']: #寫成清單
        r = '你好'
        elif msg in ['吃飯了嗎？', '你吃飯了嗎']:
            r = '還沒耶' 
        elif msg == '你是誰':
            r = '我是line機器人'
        elif '訂位' in msg:
            r = '你想訂位是嗎？'         

        #傳送訊息
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=r))#回傳文字訊息


if __name__ == "__main__":
    app.run()