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

    r = ' 我看不懂你在說甚麼耶' #預設回覆訊息

    if '給我貼圖' in msg:
        Sticker_Message = StickerSendMessage(
            package_id='11537',
            sticker_id='52002738'
        )
        line_bot_api.reply_message(event.reply_token, Sticker_Message)
    elif '哭哭' in msg:
        Sticker_Message = StickerSendMessage(
            package_id='11538',
            sticker_id='51626522'
        )
        line_bot_api.reply_message(event.reply_token, Sticker_Message)
    elif '想睡' in msg:
        Sticker_Message = StickerSendMessage(
            package_id='11538',
            sticker_id='51626513'
        )    
        line_bot_api.reply_message(event.reply_token, Sticker_Message)
    
    elif '來打架阿' in msg:
        Sticker_Message = StickerSendMessage(
            package_id='11537',
            sticker_id='52002767'
        )    
        line_bot_api.reply_message(event.reply_token, Sticker_Message)
    
    elif '還不睡嗎？' in msg:
        Sticker_Message = StickerSendMessage(
            package_id='11537',
            sticker_id='52002770'
        )    
        line_bot_api.reply_message(event.reply_token, Sticker_Message)   

    elif '拜拜' in msg:
        Sticker_Message = StickerSendMessage(
            package_id='11538',
            sticker_id='51626494'
        )    
        line_bot_api.reply_message(event.reply_token, Sticker_Message)
    elif '機器人' in msg:
        Sticker_Message = StickerSendMessage(
            package_id='11537',
            sticker_id='52002768'
        )    
        line_bot_api.reply_message(event.reply_token, Sticker_Message)      

    if msg in ['hi', 'Hi', '安安']: #寫成清單
        r = '你好'
    elif msg in ['吃飯了嗎？', '你吃飯了嗎']:
        r = '還沒耶' 
    elif msg == '你是誰':
        r = '我是line機器人'
    elif '訂位' in msg:
        r = '你想訂位是嗎？'         
    elif msg in ['好累', '好睏']:
        r = '去休息阿'
    elif '你在想甚麼？' in msg:
        r = '在想妳啊'

    if msg in ['我在想你' , '好想你啊', '好想你阿', '好想好想你阿']:
        r = '我也是~' 
    elif msg in ['不快去睡嗎？', '還不去睡？']:
        r = '再等等' 
    elif msg in ['乖點', '不要皮', '快去睡']:
        r = '好~'
    elif msg in ['你在幹嘛？', '你在幹嘛', '你在做甚麼？', '你在做甚麼', '你在做什麼？',  '你在做什麼？']: 
        r = '在打程式囉~'
    elif msg in ['想我嗎？', '有想我嗎']:
        r = '有喔~'              
    #傳送訊息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))#回傳文字訊息


if __name__ == "__main__":
    app.run()