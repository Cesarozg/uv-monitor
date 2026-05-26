def indiceuv(ciudad, datos_uv, obtener_datos_uv): 
  if datos_uv:
      print(f"Datos de radiación ultravioleta para la ciudad de: {ciudad}")
      print(f"Índice UltraVioletas en la ciudad que indicaste: {datos_uv['result']['uv']}")

  else:
      print(f"No se encontraron datos UV para la ciudad de: {ciudad}")
