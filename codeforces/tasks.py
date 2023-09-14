from celery import shared_task
from dotenv import load_dotenv
from codeforces.services import parser_codeforces

load_dotenv()


@shared_task
def parser_codeforces_task():
    """Периодическая задача: парсинг сайта Codeforces каждый час"""
    parser_codeforces('https://codeforces.com/api/problemset.problems?lang=ru')
