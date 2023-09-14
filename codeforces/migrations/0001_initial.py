# Generated by Django 4.2.4 on 2023-08-31 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskCodeforces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_number', models.CharField(max_length=20, verbose_name='номер задания')),
                ('title', models.CharField(max_length=50, verbose_name='название задания')),
                ('task_url', models.URLField(verbose_name='ссылка на задание')),
                ('number_of_solutions', models.SmallIntegerField(verbose_name='количество решений')),
                ('difficulty_level', models.SmallIntegerField(verbose_name='уровень сложности')),
                ('task_topic', models.CharField(max_length=50, verbose_name='тема задачи')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
            },
        ),
    ]
