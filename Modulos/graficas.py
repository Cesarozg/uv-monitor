import matplotlib.pyplot as plt
import pandas as pd
def graficar_comparacion(datos_ciudades):
  df = pd.DataFrame(datos_ciudades)

  # Graficar datos UV
  plt.figure(figsize=(12, 6))
  plt.bar(df['ciudad'], df['uv'], label='UV', color='skyblue', alpha=0.7)
  plt.xlabel('Ciudad', fontsize=14)
  plt.ylabel('Índice UV', fontsize=14)
  plt.title('Comparación de datos UV por Ciudad', fontsize=16)
  plt.legend(fontsize=12)
  plt.xticks(rotation=45, ha="right", fontsize=12)
  plt.yticks(fontsize=12)
  plt.tight_layout()
  plt.savefig('grafico_uv.png', bbox_inches='tight')
  plt.show()

  # Graficar datos de radiación
  plt.figure(figsize=(12, 6))
  plt.bar(df['ciudad'], df['radiacion'], label='Radiación', color='lightcoral', alpha=0.7)
  plt.xlabel('Ciudad', fontsize=14)
  plt.ylabel('Nivel de Radiación', fontsize=14)
  plt.title('Comparación de datos de Radiación por Ciudad', fontsize=16)
  plt.legend(fontsize=12)
  plt.xticks(rotation=45, ha="right", fontsize=12)
  plt.yticks(fontsize=12)
  plt.tight_layout()
  plt.savefig('grafico_radiacion.png', bbox_inches='tight')
  plt.show()

  # Graficar datos de Ozono
  plt.figure(figsize=(12, 6))
  plt.bar(df['ciudad'], df['ozono'], label='Ozono', color='moccasin', alpha=0.7)
  plt.xlabel('Ciudad', fontsize=14)
  plt.ylabel('Nivel de Ozono', fontsize=14)
  plt.title('Comparación de datos de Ozono por Ciudad', fontsize=16)
  plt.legend(fontsize=12)
  plt.xticks(rotation=45, ha="right", fontsize=12)
  plt.yticks(fontsize=12)
  plt.tight_layout()
  plt.savefig('grafico_ozono.png', bbox_inches='tight')
  plt.show()
