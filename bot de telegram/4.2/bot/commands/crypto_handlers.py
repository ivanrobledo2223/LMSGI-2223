from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from bot.funciones import *


async def crypto_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Función que se encarga de manejar el comando /crypto
    """