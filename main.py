import telegram
import os
TOKEN = os.environ['TOKEN']


bot = telegram.Bot(TOKEN)
updates=bot.getUpdates()
last_update = updates[-1]
chat_id = last_update.message.from_user.id
p = last_update.message.photo[0]
bot.sendPhoto(chat_id, p.file_id)
print(p)

