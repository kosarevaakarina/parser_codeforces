from django.core.management import BaseCommand

from codeforces.tasks import parser_codeforces_task


class Command(BaseCommand):
    """Команда для запуска парсинга сайта Codeforces: python3 manage.py parser"""
    def handle(self, *args, **options):
        try:
            parser_codeforces_task()
        except Exception:
            raise 'Ошибка при попытке парсинга'
