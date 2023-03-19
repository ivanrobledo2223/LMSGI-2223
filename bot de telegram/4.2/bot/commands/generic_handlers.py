from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

import bot.funciones.georef as geo
# Importamos las funciones que hemos creado en la carpeta /bot y todo sus ficheros. El fichero __init__.py es el que se encarga de importar todos los ficheros de la carpeta
from bot.funciones import *  

# FUNCIONES PARA MANEJAR COMANDOS EN TELEGRAM

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = ("\n"
        "🤖 Hola, Soy un bot! \n"
        "**Estas son mis habilidades**:\n\n"
        "/tiempo <cod.municipio> - Tiempo actual\n"
        "/tiempo <municipio>     - Tiempo actual\n"
        "/prevision <municipio> - Previsión tiempo\n"
        "/loc - Previsión tiempo\n"
        "..."
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message,parse_mode="markdown")

async def Sobremi_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = ("\n"
        "Nombre bot: IESAH 23LMSGI IRA\n"
        "creador: Iván\n"
        "asignatura: Lenguaje de Marcas 22-23\n"
        "Centro: IES Arroyo Harnina\n"
        "Ciclo: DAM"
    )
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message,parse_mode="markdown")

async def unknown_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Lo siento, no entiendo este comando.")
    
async def location_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    location = update.message.location

    # Ejemplo de método dentro de Utils.geo, para obtener la Georeferencia-inversa de una coordenada-gps
    resp = geo.getCityByLocation(location)
    if not resp:
        #Si la respuesta es None (valor Falsy) indicamos al usuario una respuesta amigable
        context.bot.send_message(chat_id=update.effective_chat.id, text="Lo siento no sé en qué ciudad está 🤔")    

    #Indicar en qué ciudad está el usuario.
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Usted está en {resp['city']}\nEn la dirección: {resp['description']}")