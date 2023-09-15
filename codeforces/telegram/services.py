import random

from codeforces import models


def get_tasks(tasks):
    data_str = "<b>Список задач</b>:\n"
    num = 1
    for task in tasks:
        data_str = data_str + (
            f'<b>Задача №{num}</b> {task.title}.\nСсылка: {task.task_url}.\nТэги: {task.tags}.\n'
            f'Количество решений: {task.solved_count}.\nСложность: {task.rating}\n'
            f'\n')
        num += 1
    return data_str


def get_tasks_with_rating(rating):
    """Возвращает списком до 10 задач в рандомном порядке по заданной сложности"""
    rating_task = list(models.TaskCodeforces.objects.filter(rating=rating))
    tasks = random.sample(rating_task, min(10, len(rating_task)))
    data_str = get_tasks(tasks)
    return data_str


def get_tasks_with_tags(tags):
    """Возвращает списком до 10 задач в рандомном порядке по заданной теме"""
    tags_task = list(models.TaskCodeforces.objects.filter(tags__contains=tags))
    tasks = random.sample(tags_task, min(10, len(tags_task)))
    data_str = get_tasks(tasks)
    return data_str
