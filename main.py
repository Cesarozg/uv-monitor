import os
from modulos.menu import mostrar_menu
from modulos.excel import crear_tabla_excel
from modulos.graficas import graficar_comparacion

datos_ciudades = []

# Leer API key desde variable de entorno (.env)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  

api_key = os.getenv("OPENUV_API_KEY", "")
ciudad = None

if not api_key:
    print("Advertencia: No se encontró OPENUV_API_KEY en el entorno.")
    print("Crea un archivo .env con: OPENUV_API_KEY=tu_api_key\n")

# Mostramos el menu
mostrar_menu(api_key, ciudad, datos_ciudades)

with open("datos_ciudades.txt", "w") as archivo:
    for ciudad_info in datos_ciudades:
        archivo.write(
            f"Ciudad: {ciudad_info['ciudad']}, UV: {ciudad_info['uv']}, "
            f"Radiación: {ciudad_info['radiacion']}, Ozono: {ciudad_info['ozono']}\n"
        )

crear_tabla_excel(datos_ciudades)
graficar_comparacion(datos_ciudades)
