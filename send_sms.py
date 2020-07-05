from twilio.rest import Client
account_sid = 'AC34108df01ba5b152eeb9b8cd520f1306'
auth_token = 'id token on dashboard'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="hii Prabhjot !!",
                     from_='custom generated number',
                     to='+919826511137'
                 )

print(message.sid)