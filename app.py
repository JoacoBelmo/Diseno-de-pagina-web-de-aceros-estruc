import pandas as pd
import json

# Ruta del archivo Excel en la carpeta Downloads
direccion = r'C:\Users\usuario\Documents\Joaquin\Base datos aceros.xlsx'

# Lee el archivo Excel y carga la hoja 'GENERAL' en un DataFrame
datos_df = pd.read_excel(direccion, sheet_name='GENERAL')

# Convierte los datos del DataFrame a un diccionario
datos_dict = datos_df.to_dict(orient='records')

# Guarda el diccionario como un archivo JSON
ruta_json = 'datos.json'
with open(ruta_json, 'w', encoding='utf-8') as json_file:
    json.dump(datos_dict, json_file, ensure_ascii=False, indent=4)

print(f"Archivo JSON guardado en: {ruta_json}")

ruta_html_indices = 'indices.html'
with open(ruta_html_indices, 'w', encoding='utf-8') as html_file:
    # Escribe el encabezado HTML
    html_file.write('<!DOCTYPE html>\n')
    html_file.write('<html>\n')
    html_file.write('<head>\n')
    html_file.write('<title>Índices del Excel</title>\n')
    html_file.write('</head>\n')
    html_file.write('<body>\n')
    html_file.write('<h1>Índices del Excel con Nombres</h1>\n')
    html_file.write('<ul>\n')
    # Itera sobre los elementos del diccionario
    for indice, datos in datos_dict.items():
        # Obtiene el nombre del elemento actual
        nombre = datos.get('nombre', '')  # Cambia 'nombre' por la columna que contiene los nombres
        # Obtiene el valor de la primera columna del DataFrame para el elemento actual
        primera_columna = datos_df.loc[indice, datos_df.columns[0]]
