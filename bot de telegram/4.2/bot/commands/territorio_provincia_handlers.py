from telegram import Update
from telegram.ext import ContextTypes
from bot.funciones import *


async def provincias_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Función que se encarga de manejar el comando /provincias
    """
    #Tenemos disponible el fichero funciones/bot/territorio.py, que contiene la función getListaProvincias()
    resp = territorio.getListaProvincias()
    if resp is None:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Error al obtener las provincias")
        return

    text_send_to_bot = "Listado de provincias:\n\n"

    for provinciaDict in resp["provincias"]:
        text_send_to_bot += f"{provinciaDict['codigo']}-({provinciaDict['nombre']}) - ({provinciaDict['region']})\n"

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_send_to_bot)