#用 twilio 傳 簡訊
#1 . 檔名不能用 與 twilio 相同檔名
#2. 不要用 import os 的程式
#3. 到 twilio 網站 查詢 sid 與 token
from twilio.rest import Client
account_sid = 'A111'
auth_token = 'f'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="EricWu Go Go Go !.",
                     from_='+18596952721',
                     to='+8'
                 )

print(message.sid)
