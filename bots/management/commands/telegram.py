from django.core.management import BaseCommand
from bots.telegram_bot import bot


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        bot.infinity_polling()
