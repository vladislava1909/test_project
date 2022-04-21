import telebot
#  импортировать модуль telebot и создать объект bot,
#  используя токен, полученный при регистрации.

TOKEN = '5344798817:AAG7jtDI6I185jn8Y7NKkvGIid2X829Yg24'

bot = telebot.TeleBot(TOKEN)


# # Обрабатываются все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass


# Обработчик отправляет текстовое сообщение
# в ответ на голосовое сообщение от пользователя.

@bot.message_handler(content_types=['voice'])
def voice_answer(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'У вас красивый голос!')

# Допишите обработчик так, чтобы он из сообщения брал username
# и выдавал приветственное сообщение с привязкой к пользователю.


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, f"Приветствую, {message.chat.username}")

# Обработчик, который отправляет текстовое сообщение
# в ответ сообщение от пользователя с типом текст.


@bot.message_handler(content_types=['text'])
def function_name(message):
    bot.send_message(message.chat.id, "This is a message handler")


# Обработчик, который на сообщения с фотографией будет отвечать сообщением
# «Nice meme XDD». Бот должен отвечать не отдельным сообщением,
# а с привязкой к картинке.

@bot.message_handler(content_types=['photo'])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

# Чтобы запустить бота, нужно воспользоваться методом polling.
bot.polling(none_stop=True)
# Параметр none_stop=True говорит, что бот должен стараться не прекращать работу
# при возникновении каких-либо ошибок.
