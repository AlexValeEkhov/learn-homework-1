"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from ephem import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Введи команду /planet и название планеты на английском, если хочешь узнать о них.')

planets ={
    "mercury": Mercury(now()),
    "venus": Venus(now()),
    "mars": Mars(now()),
    "jupiter": Jupiter(now()),
    "saturn": Saturn(now()),
    "uranus": Uranus(now()),
    "pluto": Pluto(now())
}

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def planet_const(update, context):
    c = 0
    text = (update.message.text).lower()              
    find_planet = text.split()                 
    for word in find_planet:  
      for key in planets: 
        if word == key: 
          const = constellation(planets[f"{word}"]) 
          print(const)
          update.message.reply_text(f'Планета {(word).capitalize()} находится в созвездии {const}')
          c = 1
    if c == 0:         
        update.message.reply_text('Нет такой планеты')


def main():
    mybot = Updater("5751095837:AAGYZtVX1HEOvmKEggLT36DOHrY2qcz-3NU", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', planet_const))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()