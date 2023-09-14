from django.core.management import BaseCommand
from codeforces.telegram.bot import bot


class Command(BaseCommand):
    """Команда для запуска бота: python3 manage.py bot"""

    def handle(self, *args, **options):
        try:
            bot.infinity_polling()
        except Exception:
            raise 'Ошибка при запуске бота'
