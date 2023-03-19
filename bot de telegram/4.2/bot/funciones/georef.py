import os
import requests
import constants as ct
from telegram import Location

# Utilizar la Api de RapidAPI <Forward & Reverse Geocoding>. Se necesita registro. Usar email@iesarroyoharnina.
def getCityByLocation(location :Location):
    """
    Obtiene la georeferencia inversa desde un (latitud,longitud)
    Para obtener el esquema de la respuesta, haz una petición

    Devuelve {
        "city": "Madrid",
        "postalCode": "28001",
        "description": "Calle de la Montera, 28001 Madrid, España",
    }
    """
    import requests

    url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/forward"

    querystring = {"street":"34 West 13th Street","city":"New York City","state":"NY","postalcode":"10011","country":"USA","accept-language":"en","polygon_threshold":"0.0"}

    headers = {
        "X-RapidAPI-Key": "d3b3d31c64msh3bdc45477fc8f12p1d7593jsn5864370762b0",
        "X-RapidAPI-Host": "forward-reverse-geocoding.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)



    url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/reverse"

    querystring = {"lat":location.latitude,"lon":location.longitude,"accept-language":"en","polygon_threshold":"0.0"}

    headers = {
        "X-RapidAPI-Key": ct.Constants.RAPID_API_TOKEN_GEOREF,
        "X-RapidAPI-Host": "forward-reverse-geocoding.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code!=200:
        return None

    #Respuesta esperada
    """
    {
    "licence": "Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright",
    "osm_id": 150182922,
    "address": {
        "road": "South Michigan Avenue",
        "state": "Illinois",
        "building": "Congress Plaza Hotel",
        "county": "Cook County",
        "house_number": "500-510",
        "city": "Chicago",
        "suburb": "Loop",
        "country": "United States",
        "neighbourhood": "Loop",
        "country_code": "us",
        "postcode": "60604"
    },
    "osm_type": "way",
    "boundingbox": [
        "41.8751468",
        "41.8756014",
        "-87.6251579",
        "-87.6244969"
    ],
    "place_id": 136468986,
    "lat": "41.875375399999996",
    "lon": "-87.62482736161188",
    "display_name": "Congress Plaza Hotel, 500-510, South Michigan Avenue, Loop, Chicago, Cook County, Illinois, 60604, United States"
}
    """

    json_data= response.json()

    #Retornar un dictionario con los datos necesarios... abajo os dejo un ejemplo de una opción posible
    
    return {
        "city": json_data['address']['city'],
        "postalCode": json_data['address']['postcode'],
        "description": json_data['display_name'],
    }