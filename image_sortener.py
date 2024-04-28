import os
import shutil
from datetime import datetime

def obtener_fecha_modificacion(archivo_path):
    fecha_modificacion = os.path.getmtime(archivo_path)
    return datetime.fromtimestamp(fecha_modificacion)

def organizar_fotos_por_fecha_modificacion(carpeta):
    archivos = os.listdir(carpeta)
    
    for archivo in archivos:
        archivo_path = os.path.join(carpeta, archivo)
        if os.path.isfile(archivo_path):
            fecha_modificacion = obtener_fecha_modificacion(archivo_path)
            anho = str(fecha_modificacion.year)
            mes = fecha_modificacion.strftime('%B')
            nueva_carpeta_anho = os.path.join(carpeta, anho)
            nueva_carpeta_mes = os.path.join(nueva_carpeta_anho, mes)
            
            if not os.path.exists(nueva_carpeta_anho):
                os.mkdir(nueva_carpeta_anho)
            if not os.path.exists(nueva_carpeta_mes):
                os.mkdir(nueva_carpeta_mes)
            
            shutil.move(archivo_path, nueva_carpeta_mes)
            print(f"Archivo '{archivo}' movido a '{nueva_carpeta_mes}'")

carpeta_actual = os.getcwd()
organizar_fotos_por_fecha_modificacion(carpeta_actual)
