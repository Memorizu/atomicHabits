import telebot
from django.conf import settings
from users.models import User


token = settings.TELEGRAM_TOKEN
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Приветствую! Для дальнейших уведомлений о ваших привычках напишите свой Email')


@bot.message_handler(func=lambda message: True)
def handle_email_input(message):
    chat_id = message.chat.id
    email = message.text

    if User.objects.filter(email=email).exists():
        user = User.objects.get(email=email)
        user.chat_id = chat_id
        user.save()

        bot.send_message(chat_id,
                         text='Ваш Email подтвержден. Теперь вы будете получать уведомления в этот чат.')
    else:
        bot.send_message(chat_id, text='Такого Email не существует. Проверьте ваш Email.')
