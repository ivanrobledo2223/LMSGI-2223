import requests

def getListaProvincias():

    """
    Retorna todas las provincias:
{
        "num_provincias": len(listaProvincias),
        "provincias": listaProvincias
    }
    """
    # Aqui se llama a la petición por el método GET (obtener)
    response = requests.get("https://www.el-tiempo.net/api/json/v2/provincias")

    if response.status_code!=200:
        return None


    #Retorno request Provincias
    """
    provincias: [{
            "CODPROV": "01",
            "NOMBRE_PROVINCIA": "Araba/Álava",
            "CODAUTON": "16",
            "COMUNIDAD_CIUDAD_AUTONOMA": "País Vasco/Euskadi",
            "CAPITAL_PROVINCIA": "Vitoria-Gasteiz"
        }
        , ...
        ],
    """

    # obtener la información en formato Json
    json_data = response.json()
    provinciasRetornadas = json_data["provincias"]

    #Voy a devolver una lista de provincias, con el formato que quiero
    listaProvincias = []
    for provinciaDict in provinciasRetornadas:
        listaProvincias.append(
            {
            "nombre": provinciaDict["NOMBRE_PROVINCIA"],
            "codigo": provinciaDict["CODPROV"],
            "region": provinciaDict["COMUNIDAD_CIUDAD_AUTONOMA"],
            }
        )

    return {
        "num_provincias": len(listaProvincias),
        "provincias": listaProvincias
    }

    #await context.bot.send_message(chat_id=update.effective_chat.id, text=text_send_to_bot)

def getListaMunicipios():
    """
    Retorna todas los municipios:
{
        "num_municipios": len(listaMunicipios),
        "municipios": listaMunicipios
    }
    """
    # Aqui se llama a la petición por el método GET (obtener)
    response = requests.get("https://www.el-tiempo.net/api/json/v2/municipios")

    if response.status_code!=200:
        return None


    #Retorno request Municipios
    """
    {
        "CODIGOINE": "01001000000",
        "ID_REL": "1010014",
        "COD_GEO": "01010",
        "CODPROV": "01",
        "NOMBRE_PROVINCIA": "Araba\/\u00c1lava",
        "NOMBRE": "Alegr\u00eda-Dulantzi",
        "POBLACION_MUNI": 2925,
        "SUPERFICIE": 1994.5872,
        "PERIMETRO": 35069,
        "CODIGOINE_CAPITAL": "01001000101",
        "NOMBRE_CAPITAL": "Alegr\u00eda-Dulantzi",
        "POBLACION_CAPITAL": "2815",
        "HOJA_MTN25": "0113-3",
        "LONGITUD_ETRS89_REGCAN95": -2.51243731,
        "LATITUD_ETRS89_REGCAN95": 42.83981158,
        "ORIGEN_COORD": "Mapa",
        "ALTITUD": 568,
        "ORIGEN_ALTITUD": "MDT5",
        "DISCREPANTE_INE": 0
    },
    """

    # obtener la información en formato Json
    json_data = response.json()
    municipiosRetornados = json_data["municipios"]

    #Voy a devolver una lista de municipios, con el formato que quiero
    listaMunicipios = []
    for municipioDict in municipiosRetornados:
        listaMunicipios.append(
            {
            "nombre": municipioDict["NOMBRE_PROVINCIA"],
            "codigo": municipioDict["CODPROV"],
            "capital": municipioDict["NOMBRE_CAPITAL"],
            }
        )

    return {
        "num_municipios": len(listaMunicipios),
        "municipios": listaMunicipios
    }

    #await context.bot.send_message(chat_id=update.effective_chat.id, text=text_send_to_bot)