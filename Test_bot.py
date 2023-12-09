from decouple import config
import telebot, wikipedia  
from telebot import types  

wikipedia.set_lang('ru') 
token = config('TOKEN')
bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Сохранить')
button2 = types.KeyboardButton('Дальше')
keyboard.add(button1, button2)

shish='shish'

def getwiki(s):
    try:
        wikitext = wikipedia.page(s).content[:500]  #срез до 500 символов
        wikitext = wikitext.split('.')
        wikitext = ''.join(wikitext[:-1]) + '.'     #убираем последнее незаконченное предложение и ставим точку
        return wikitext
    except Exception as e:
        return 'В энциклопедии нет инфо об этом'

@bot.message_handler(commands=['start'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Отправьте мне любое слово, и я найду его значение в wikipedia', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message2, handle_text)
    

def handle_text(message):
    word = message.text
    info = getwiki(word)
    message2 = bot.send_message(message.chat.id, info, reply_markup=keyboard)
    print(message2.text)
    bot.register_next_step_handler(message2, save, info)

def save(message, info):
    if message.text.lower() == 'сохранить':
        with open('file.txt', 'a') as f:
            f.write(info + '\n')
        bot.send_message(message.chat.id, 'Вы успешно сохранили информацию', reply_markup=types.ReplyKeyboardRemove())
    start_message(message)

@bot.message_handler(commands='Иди нафиг'])
def start_message2(message):
    message2 = bot.send_message(message.chat.id, 'Сам Иди нафиг' reply_markup=types.ReplyKeyboardRemove())

bot.polling()
