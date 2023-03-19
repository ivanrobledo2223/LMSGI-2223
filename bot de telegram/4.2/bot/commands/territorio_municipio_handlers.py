from telegram import Update
from telegram.ext import ContextTypes
from bot.funciones import *
import requests
import random


async def municipios_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Función que se encarga de manejar el comando /municipios
    """
    if len(context.args) == 0:
        for id in range(1,53):
            if id < 10:
                id = f"0{id}"
            else:
                str(id)
            data = getMunicipios(id)

            keys = list(data.keys())
            nombreProvincia = data[keys[0]]["NOMBRE_PROVINCIA"]
            message = f"Municipios de {nombreProvincia}\n\n"

            municipiosParaSacar = 10

            if len(keys) < 10:
                municipiosParaSacar = len(keys)

            municipios_seleccionados = random.sample(list(data),municipiosParaSacar)

            for key in municipios_seleccionados:
                message+=data[key]["NOMBRE"] + "\n"
            await context.bot.send_message(chat_id=update.effective_chat.id,text=message)  
            pass  #Elimina esto cuando hayas implementado la función


def getMunicipios( codProv):
        data = request(f"https://www.el-tiempo.net/api/json/v1/provincias/{codProv}/municipios")
        if codProv == "01":
            idlist = list(range(0,len(data)))
            diction = {id:data[id] for id in idlist}
            return diction
        return data

        for munID in municipios.keys():
            municipio = municipios[munID]
            codigo = (municipio["CODIGOINE"])[:5]
            text += "{} - {NOMBRE}\n".format(codigo,**municipio)
            
def request(url):
    data = requests.get(url).json()
    return data