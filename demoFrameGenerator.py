import json
import os
import re
import copy
from datetime import datetime
from frame_generator.image_generator import ImageGenerator

def limpiar_texto(cadena, mantener_guion_bajo=False):
    tabla = str.maketrans('ÁÉÍÓÚÑáéíóúñ', 'AEIOUNaeioun')
    cadena = cadena.translate(tabla).strip().lower()
    if mantener_guion_bajo:
        cadena = re.sub(r'\s+', '_', cadena)
        return re.sub(r'[^a-z0-9_]', '', cadena)
    return re.sub(r'[^a-z0-9]', '', cadena)

def generar_imagen(map_data):
    nombre_reporte = map_data['data']['reporte']
    base_out = os.path.dirname(os.path.abspath(__file__))
    ruta_png = os.path.abspath(os.path.join(base_out, 'static', 'images', 'expo', f"{nombre_reporte}.png"))
    
    try:
        generator = ImageGenerator(map_data)
        generator.render()
        generator.output_png(ruta_png)
        generator.output_avif(ruta_png.replace('.png', '.avif'))
        print(f"✅ {nombre_reporte} generado con éxito.")
    except Exception as e:
        print(f"❌ Error en {nombre_reporte}: {str(e)}")

# --- PROCESO ---

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_base_json = os.path.join(BASE_DIR, 'frame_generator', 'data_map.json')
ruta_sipsa_json = os.path.abspath(os.path.join(BASE_DIR, 'project', 'data', 'json', 'promediosSipsaCiudad.json'))

try:
    with open(ruta_base_json, 'r', encoding='utf-8') as f:
        map_data_base = json.load(f)
    with open(ruta_sipsa_json, 'r', encoding='utf-8') as f:
        map_data_ciudad = json.load(f)
except Exception as e:
    print(f"❌ Error al cargar archivos: {e}")
    exit()

ciudad_objetivo = re.sub(r'[*.-]', '', "SAN JOSÉ DE CÚCUTA").strip().lower()
productos_unicos = {}

# Filtrado por fecha ISO
for item in map_data_ciudad:
    ciudad_limpia = re.sub(r'[*.-]', '', item['ciudad']).strip().lower()
    if ciudad_limpia == ciudad_objetivo:
        id_prod = limpiar_texto(item['producto'])
        fecha_item = datetime.fromisoformat(item['fechaCaptura'])
        
        if id_prod not in productos_unicos:
            productos_unicos[id_prod] = item
        else:
            fecha_exist = datetime.fromisoformat(productos_unicos[id_prod]['fechaCaptura'])
            if fecha_item > fecha_exist: productos_unicos[id_prod] = item

items_a_procesar = list(productos_unicos.values())

for item in items_a_procesar:
    current_config = copy.deepcopy(map_data_base)
    
    c_archivo = limpiar_texto(item['ciudad'])
    p_archivo = limpiar_texto(item['producto'], True)
    
    # Formateo de datos igual que en PHP
    p_visual = re.sub(r'[^\w\sáéíóúÁÉÍÓÚñÑ]', '', item['producto'])
    c_visual = re.sub(r'[^\w\sáéíóúÁÉÍÓÚñÑ]', '', item['ciudad'])
    
    try:
        precio_num = float(item['precioPromedio'])
        precio_str = f"${precio_num:,.0f}".replace(',', '.')
    except:
        precio_str = "$0"
    
    fecha_str = datetime.fromisoformat(item['fechaCaptura']).strftime("%d/%m/%Y")

    # AQUÍ SE RELLENAN LAS LLAVES QUE TU JSON YA TIENE
    current_config['data'].update({
        'producto': p_visual,
        'precio': precio_str,
        'ciudad': c_visual,
        'fecha': fecha_str,
        'reporte': f"reporte_{c_archivo}_{p_archivo}"
    })

    # Rutas de imágenes
    current_config['elements'][0]['path'] = './fotos/ciudad.png'
    current_config['elements'][1]['path'] = f"{c_archivo}{p_archivo}.png"
    current_config['elements'][2]['path'] = f"./fotos/{p_archivo}.png"

    generar_imagen(current_config)

print("\n--- PROCESO COMPLETADO ---")
