from django.contrib import admin

from codeforces.models import TaskCodeforces


@admin.register(TaskCodeforces)
class TaskAdmin(admin.ModelAdmin):
    """Административная панель модели TaskCodeforces"""
    list_display = ('contest_id', 'index', 'title', 'tags', 'rating')
    list_filter = ('title', 'tags')
