def infozono(ciudad, datos_uv, obtener_datos_uv):
  if datos_uv:
    print(f"Capa de ozono en {ciudad}: {datos_uv['result']['ozone']}\n")
  else:
    print(f"No se pudieron obtener indices de la capa de ozono para la ciudad de: {ciudad}")