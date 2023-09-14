from django.db import models

NULLABLE = {'blank': True, 'null': True}


class TaskCodeforces(models.Model):
    """Модели задачи"""
    contest_id = models.CharField(max_length=20, verbose_name='ID задания')
    index = models.CharField(max_length=20, verbose_name='индекс задания')
    title = models.CharField(max_length=300, verbose_name='название задания')
    task_url = models.CharField(verbose_name='ссылка на задание')
    solved_count = models.CharField(verbose_name='количество решений', **NULLABLE)
    rating = models.CharField(verbose_name='уровень сложности', **NULLABLE)
    tags = models.CharField(max_length=200, verbose_name='тема задачи', **NULLABLE)

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        """Строковое представление модели"""
        return f'Задача {self.contest_id}{self.index} {self.title} ({self.tags})'
