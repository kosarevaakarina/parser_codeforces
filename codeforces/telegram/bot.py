import telebot
from django.conf import settings
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from codeforces.telegram.services import get_tasks_with_rating, get_tasks_with_tags

bot = telebot.TeleBot(settings.TELEGRAM_BOT_API, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Обрабатывает команду /start"""
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.add(KeyboardButton("Выбрать уровень сложности"))
    markup.add(KeyboardButton("Выбрать тему задачи"))
    bot.send_message(chat_id=message.chat.id, text="Выбрать задачу:", reply_markup=markup)


@bot.message_handler()
def send_rating(message):
    """Обрабатывает команду запроса задач по уровню сложности и теме"""
    if message.text == 'Выбрать уровень сложности':
        bot.send_message(chat_id=message.chat.id,
                         text='Для выбранного уровня сложности будет предложено до 10 задач, '
                              'для просмотра задачи необходимо перейти по ссылке')
        msg = bot.send_message(chat_id=message.chat.id, text="Введите уровень сложности: ")
        bot.register_next_step_handler(msg, rating)
    if message.text == 'Выбрать тему задачи':
        bot.send_message(chat_id=message.chat.id,
                         text='Для выбранной темы будет предложено до 10 задач, '
                              'для просмотра задачи необходимо перейти по ссылке')
        msg = bot.send_message(chat_id=message.chat.id, text="Введите тему задач: ")
        bot.register_next_step_handler(msg, tags)


def rating(message):
    """Выводит пользователю задачи по введенному уровню сложности"""
    data = get_tasks_with_rating(message.text)
    empty = '<b>Список задач</b>:\n'
    if data == empty:
        bot.send_message(chat_id=message.chat.id, text='Задач с такой сложностью нет')
    else:
        bot.send_message(chat_id=message.chat.id, text=data)


def tags(message):
    """Выводит пользователю задачи по введенному уровню сложности"""
    data = get_tasks_with_tags(message.text.lower())
    empty = '<b>Список задач</b>:\n'
    if data == empty:
        bot.send_message(chat_id=message.chat.id, text='Задач с такой темой нет')
    else:
        bot.send_message(chat_id=message.chat.id, text=data)
