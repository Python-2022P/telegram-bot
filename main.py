import telegram
import os
# TOKEN = os.environ['TOKEN']
TOKEN = os.environ['token']

print(TOKEN)


bot = telegram.Bot(TOKEN)
updates=bot.getUpdates()
first_update=updates.message.message_id
while True :
    last_update=updates.message.message_id
    chat=updates.message.from_user
    if first_update!=last_update:
        if updates.message.text:
            bot.sendMessage(last_update,updates.message.text)
        elif updates.message.photo:
            bot.sendPhoto(last_update,updates.message.photo[-1].file_id)
        first_update=updates.message.message_id
