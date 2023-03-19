from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from bot.funciones import *
import requests
import json







    #if len(context.args) == 0:
        # location_keyboard = KeyboardButton(text="📌 enviar posición", request_location=True,)
        # custom_keyboard = [[ location_keyboard ]]
        # reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        # await context.bot.send_message(chat_id=update.message.chat_id,text="Te gustaría compartir la ubicación conmigo?", reply_markup=reply_markup)
        #return
    
    #if len(context.args) == 1:
        #El usuario a introducido un código de municipio o un nombre de municipio
        # pass


    #if len(context.args) >= 2:
        #indicar al usuario que el comando no admite más de un argumento
        #pass

