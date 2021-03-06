import flask
import telebot
import conf
import random
import requests
import markovify

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN, threaded=False)

bot.remove_webhook()

bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH)

app = flask.Flask(__name__)


books = ('1_Igra_Prestolov', '2_Bitva_Korolei', '3_Burya_Mechei', '4_Pir_Stervyatnikov', '5_Tanets_S_Drakonami')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добрый вечер! Это бот, который, находясь под впечатлением от серии книг 'Песнь Льда и Пламени', научился выдавать фразы в стиле Джорджа Р. Р. Мартина (с помощью цепи имени Маркова) в ответ на любое Ваше сообщение. Give it a try!")

def mess_maker():
    books = ('1_Igra_Prestolov', '2_Bitva_Korolei', '3_Burya_Mechei', '4_Pir_Stervyatnikov', '5_Tanets_S_Drakonami')
    rb = random.choice(books)
    tex = requests.get('https://raw.githubusercontent.com/LZGod/pr2/master/home/%s' % rb)
    tt = tex.text
    m = markovify.Text(tt)

    mess = ''
    for i in range(5):
        mess=m.make_sentence()
    return(mess)

@bot.message_handler(func=lambda m: True)
def my_function(message):
    reply = mess_maker()
    bot.send_message(message.chat.id, '%s' %reply)

@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'

@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)
