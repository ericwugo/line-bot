# 用 flask 架設伺服器 Line bot


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('37thqHgLzV1GSjbe0e6hvFaRN03yxaASHtry/qHiWg6p+lPZ7cTfKwBCW3flo1AFnkPcqCBx1WVc1T/dqSb283OgRI8uUGHc8HOLE6UWf+klEPWihVhkqnrHVWVX/YgM8Ph/ZIjbxE5JdLsY+ufDfgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('999bdd8307dbea0ba00dabdc80ed5b0c')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
