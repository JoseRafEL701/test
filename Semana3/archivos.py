# archivos.py
# Módulo responsable de la persistencia del inventario en archivos CSV
# Usa: módulo csv, manejo de excepciones, validación de filas

import csv
import os

def guardar_csv(inventario, nombre_archivo="inventario.csv"):
    """Guarda el inventario en un archivo CSV con encabezado.
    Usa: csv.DictWriter"""
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "precio", "cantidad"])
            escritor.writeheader()
            escritor.writerows(inventario)
        print(f"✅ Inventario guardado correctamente en '{nombre_archivo}'")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")


def cargar_csv(nombre_archivo="inventario.csv"):
    """Carga el inventario desde un archivo CSV.
    Retorna: lista de diccionarios + número de filas omitidas.
    Maneja filas inválidas sin cerrar el programa."""
    inventario = []
    filas_omitidas = 0
    
    if not os.path.exists(nombre_archivo):
        print(f"⚠️  El archivo '{nombre_archivo}' no existe.")
        return inventario, 0
    
    try:
        with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila_num, fila in enumerate(lector, 1):
                try:
                    nombre = fila["nombre"].strip()
                    precio = float(fila["precio"])
                    cantidad = int(fila["cantidad"])
                    
                    if not nombre or precio <= 0 or cantidad < 0:
                        raise ValueError("Datos inválidos")
                    
                    inventario.append({
                        "nombre": nombre.capitalize(),
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except (KeyError, ValueError, TypeError):
                    filas_omitidas += 1
                    print(f"⚠️  Fila {fila_num} omitida (datos inválidos).")
    except Exception as e:
        print(f"❌ Error al leer el archivo CSV: {e}")
        return [], 0
    
    if filas_omitidas > 0:
        print(f"ℹ️  Se omitieron {filas_omitidas} filas inválidas.")
    
    return inventario, filas_omitidas