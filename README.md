# Телеграм бот для получения задач с сайта Codeforces

## Описание
* Настроена интеграция с Telegram.
* С помощью бота возможно получать подборку из 10 задач в зависимости от сложности и выбранной темы;
* Настроена периодическая задача через Celery, которая осуществляет парсинг задач с сайта Codeforces каждый час;
* Имеется список зависимостей.
* Результат проверки Flake8 равен 100%, при исключении миграций.

## Технологии

* Python
* Django, DRF
* PostgreSQL
* Celery, Redis
* TelegramBotApi

---

### Запуск приложения в локальной сети:

_Для запуска проекта необходимо клонировать репозиторий и создать и активировать виртуальное окружение:_

```
python3 -m venv venv

source venv/bin/activate
```

_Установить зависимости:_

```
pip install -r requirements.txt
```

_Для работы с переменными окружениями необходимо создать файл .env и заполнить его согласно файлу .env.sample_

_Выполнить миграции:_

```
python3 manage.py migrate
```
_Создать администратора:_

```
python3 manage.py createsuperuser
```

_Для заполнения БД запустить команду:_

```
python3 manage.py loaddata data.json
```

_Для запуска redis_:

```
redis-cli
```

_Для запуска celery:_

```
celery -A config worker --loglevel=info
```

_Для запуска django-celery-beat:_

```
celery -A config beat --loglevel=info
```

_Для запуска парсинга:_

```
python3 manage.py parser
```

_Для запуска бота:_

```
python3 manage.py bot
```


