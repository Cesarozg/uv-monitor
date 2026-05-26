import time
from modulos.datosuv import indiceuv 
from modulos.radiacion import indrad
from modulos.datos import obtener_datos_uv
from modulos.ozono import infozono
def mostrar_menu(api_key, ciudad, datos_ciudades):
  cddiferente = None
  while True:
    print("Bienvenido al menú:")
    print("1. Ingresar una ciudad")
    print("2. Consultar datos UV")
    print("3. Consultar Indicios de radiación")
    print("4. Consultar Nivel de Ozono")
    print("5. Salir")

    if ciudad is None:
      print("No haz ingresado una ciudad.")

    opcion = int(input("Ingrese la opcion que desea consultar: "))

    if opcion == 1:
        ciudad = input("Ingrese el nombre de la ciudad: ")
    elif opcion == 2:
        if ciudad is None:
            print("Aun no has ingresado una ciudad.")
        else:
            datos_uv = obtener_datos_uv(api_key, ciudad)
            indiceuv(ciudad, datos_uv, obtener_datos_uv)
            sn = input("¿Desea almacenar esta información? (s/n): ")
            if sn == "s":
                if ciudad == cddiferente:
                    datos_ciudades[1]['uv'] = datos_uv['result']['uv'] 
                else:
                    datos_ciudades.append({'ciudad': ciudad, 'uv': datos_uv['result']['uv'], 'radiacion': None, 'ozono': None})
                print("Datos almacenados correctamente\n")
            else:
                print("Datos no almacenados\n")
                time.sleep(1.5)
            cddiferente = ciudad
    elif opcion == 3:
        if ciudad is None:
            print("Aún no has ingresado una ciudad.")
        else:
            datos_uv = obtener_datos_uv(api_key, ciudad)
            indrad(ciudad, datos_uv, obtener_datos_uv)
            sn = input("¿Desea almacenar esta información? (s/n): ")
            if sn == "s":
                if ciudad == cddiferente:
                    datos_ciudades[-1]['radiacion'] = datos_uv['result']['uv_max'] 
                else:
                    datos_ciudades.append({'ciudad': ciudad, 'uv': None, 'radiacion': datos_uv['result']['uv_max'], 'ozono': None})
                print("Datos almacenados correctamente\n")
            else:
                  print("Datos no almacenados\n")
                  time.sleep(1.5)
            cddiferente = ciudad
    elif opcion == 4:
        if ciudad is None:
            print("Aún no has ingresado una ciudad.")
        else:
            datos_uv = obtener_datos_uv(api_key, ciudad)
            infozono(ciudad, datos_uv, obtener_datos_uv)
            sn = input("¿Desea almacenar esta información? (s/n): ")
            if sn == "s":
                if ciudad == cddiferente:
                    datos_ciudades[-1]['ozono'] = datos_uv['result']['ozone'] 
                else:
                    datos_ciudades.append({'ciudad': ciudad, 'uv': None, 'radiacion': None, 'ozono': datos_uv['result']['ozone']})
                print("Datos almacenados correctamente\n")
            else:
                  print("Datos no almacenados\n")
                  time.sleep(1.5)
            cddiferente = ciudad
          
    elif opcion == 5:
          print("Gracias por usar nuestro programa, nos vemos.")
          break
    else:
          print("Opción no válida. Por favor, ingresa una opción válida.")
        
  