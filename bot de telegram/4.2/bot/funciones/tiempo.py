import requests

def getTiempoActual(municipioUser):
    municipios = requests.get("https://www.el-tiempo.net/api/json/v2/municipios%22")
    if municipios.status_code != 200:
        return None

    municipioJson = municipios.json()

    codigosMunicipio = []
    for municipio in municipioJson:
        if (municipio["NOMBRE"].capitalize() == municipioUser.capitalize()):
            codigosMunicipio.append({
                "codigoProvincia": municipio["CODPROV"],
                "codigoGeo": municipio["COD_GEO"]
            })

    codProv = codigosMunicipio[0]["codigoProvincia"]
    codGeo = codigosMunicipio[0]["codigoGeo"]
    respuesta = requests.get(f"https://www.el-tiempo.net/api/json/v2/provincias/%7BcodProv%7D/municipios/%7BcodGeo%7D%22")
    if respuesta.status_code != 200:
        return None

    tiempoMuni = respuesta.json()