import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from bot.commands import *  # importamos todos los comandos (que contiene las funciones que manejan los comandos)
import constants as ct # importamos el fichero constants.py (que contiene las constantes)

# EL FICHERO MAIN.PY DEBE CONTENER EL CÓDIGO QUE SE EJECUTA CUANDO SE LANZA EL BOT DESDE LA CONSOLA
# DEBE ESTAR LO MÁS LIMPIO POSIBLE, SIN CÓDIGO DE MÁS, PARA QUE SEA FÁCIL DE ENTENDER Y DE MODIFICAR
# TODOS LA FUNCIONALIDAD DEBE ESTAR EN OTROS FICHEROS, QUE SE IMPORTEN EN ESTE

#Configurar el logging (explico en clase)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
    

if __name__ == '__main__':
    #Obtengo el Token desde una variable-entorno (en vuestro caso no hace falta y es necesario que el profesor tenga el Token disponible para Evaluar)
    # Vosotros teneís que obtener el tocken desde las constantes....
    # 
    application = ApplicationBuilder().token(ct.Constants.TELEGRAM_BOT_TOKEN).build()



    # ----- Incluir aquí debajo el resto de comandos que queramos que el bot escuche  ----------
    
    cmdStartHandler = CommandHandler('start', generic_handlers.start_handler)
    application.add_handler(cmdStartHandler)

    cmdSobreMiHandler = CommandHandler('sobremi', generic_handlers.Sobremi_handler)
    application.add_handler(cmdSobreMiHandler)

    cmdMunicipiosHandler = CommandHandler('municipios',territorio_municipio_handlers.municipios_handler)
    application.add_handler(cmdMunicipiosHandler)

    cmdProvinciasHandler = CommandHandler('provincias', territorio_provincia_handlers.provincias_handler)
    application.add_handler(cmdProvinciasHandler)

    cmdTiempoHandler = CommandHandler('tiempo', tiempo_actual_handler.tiempo_handler)
    application.add_handler(cmdTiempoHandler)

    cmdPrevisionHandler = CommandHandler('prevision', tiempo_prevision_handlers.prevision_handler)
    application.add_handler(cmdPrevisionHandler)

    cmdPrevisionHandler = CommandHandler('crypto', crypto_handlers.crypto_handler)
    application.add_handler(cmdPrevisionHandler)

    locationMessageHandler = MessageHandler(filters.LOCATION, generic_handlers.location_handler)
    application.add_handler(locationMessageHandler)



    # --------------------------------------- FIN COMANDOS --------------------------------------- #

    #Utiliza en caso de que el comando no sea reconocido
    unknown_handler = MessageHandler(filters.COMMAND,generic_handlers.unknown_handler)
    application.add_handler(unknown_handler)
    
    #Queda esperando a que el usuario introduzca comandos..
    application.run_polling()