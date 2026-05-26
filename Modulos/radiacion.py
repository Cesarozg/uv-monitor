def indrad(ciudad, datos_uv, obtener_datos_uv):
  if datos_uv:
    print(f"Nivel de radiación {ciudad}: {datos_uv['result']['uv_max']}\n")
  else:
    print(f"No se pudieron obtener indicios de radiación para la ciudad de: {ciudad}")