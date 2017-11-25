# Импортируем нужные компоненты
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# Функция, которая соединяется с платформой Telegram, "тело" нашего бота
import logging
import ephem
import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start. Я скажу тебе в каком созвездии планета!'
    #print(1/0)
    print(text)
    update.message.reply_text(text)


def space(bot, update):
    date=datetime.datetime.now()
    #logging.info(user_text)
    #update.message.reply_text('Введите планету  ')
    planeta=update.message.text
    print(planeta) 
    print(len(planeta))
    print(planeta[9:])
    planeta=planeta[9:]
    print('Итог ', planeta) 
       #update.message.reply_text('Введите дату согласно формату ГГГГ/ММ/ДД ')
    #date=update.message.text 

    #planeta=input('Введите планету  ')
    #date=input('Введите дату согласно формату ГГГГ/ММ/ДД ')
    #reply_to_user= update.message.text 
    if planeta =='Mars' :
        mars = ephem.Mars(date)
        reply_to_user=ephem.constellation(mars)

    elif planeta =='Mercury' :
        mercury  = ephem.Mercury(date)
        reply_to_user=ephem.constellation(mercury)

    elif planeta =='Venus' :
        venus = ephem.Venus(date)
        reply_to_user=ephem.constellation(venus)

    elif planeta =='Jupiter' :
        jupiter = ephem.Jupiter(date)
        reply_to_user=ephem.constellation(jupiter)

    elif planeta =='Saturn' :
        saturn = ephem.Saturn(date)
        reply_to_user=ephem.constellation(saturn)

    elif planeta =='Uranus' :
        uranus = ephem.Mars(date)
        reply_to_user=ephem.constellation(uranus)

    elif planeta =='Neptune' :
        neptune = ephem.Neptune(date)
        reply_to_user=ephem.constellation(neptune)

    elif planeta =='Pluto' :
        pluto  = ephem.Pluto(date)
        reply_to_user=ephem.constellation(pluto)
 
    #update.message.reply_text(user_text)

    update.message.reply_text(reply_to_user)


'''

def talk_to_me(bot, update):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text)

def talk_to_me_planet(planeta, bot, update):
    
    update.message.reply_text('Введите планету  ')
    planeta = update.message.text 
    #return planeta 
    update.message.reply_text(planeta )
    #if planeta=='Mars':
     #  return planeta 

def talk_to_me_date(date, bot, update):
    update.message.reply_text('Введите дату согласно формату ГГГГ/ММ/ДД ')
   
    date=update.message.text 
    #return date 
    update.message.reply_text(date)

    '''

def main():
    updater = Updater("478411131:AAFn2nvMqaDicbbqE2Xsta_L4cQu1MY-zPM")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planeta",space))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me_planet))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me_date))
    #a=dp.add_handler(MessageHandler(Filters.text, talk_to_me_planet))
    #b=dp.add_handler(MessageHandler(Filters.text, talk_to_me_date))
    #dp.add_handler(MessageHandler(Filters.text, space)
    
    updater.start_polling()
    updater.idle()

# Вызываем функцию - эта строчка собственно запускает бота
main()
