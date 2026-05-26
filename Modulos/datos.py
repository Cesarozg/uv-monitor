import os
import requests
from geopy.geocoders import Nominatim

def obtener_datos_uv(api_key, ciudad):
    # Si no se pasa api_key, leerla del entorno
    if not api_key:
        api_key = os.getenv("OPENUV_API_KEY")
    if not api_key:
        print("Error: No se encontró la API key. Crea un archivo .env con OPENUV_API_KEY=tu_key")
        return None
    try:
        geolocalizador = Nominatim(user_agent="app_uv")
        ubicacion = geolocalizador.geocode(ciudad)
        if ubicacion:
            lat = ubicacion.latitude
            lon = ubicacion.longitude
            url = f"https://api.openuv.io/api/v1/uv?lat={lat}&lng={lon}"
            headers = {
                "x-access-token": api_key,
            }
            respuesta = requests.get(url, headers=headers)
            if respuesta.status_code == 200:
                return respuesta.json()
            else:
                print(f"Error al consultar la API: {respuesta.status_code}")
                return None
        else:
            print(f"No se encontró la ciudad: {ciudad}")
            return None
    except Exception as e:
        print(e)
        return None
