# -------------------------------
# Gestionar varios productos en el inventario mediante un menú interactivo.
# Organizar registros, validar datos y obtener estadísticas básicas de forma sencilla.
# Aplicar estructuras condicionales (if/elif/else) y bucles (while y for) en Python,
# utilizando listas y diccionarios para almacenar productos, validar entradas
# y calcular estadísticas del inventario.
# -------------------------------

inventario = []  # Lista de diccionarios donde se guardan los productos


# -------------------------------
# Funciones de validación
# -------------------------------

def pedir_nombre():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            return nombre
        print("Error: El nombre no puede estar vacío. Intente nuevamente.")

def pedir_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio unitario: ").strip())
            if precio <= 0:
                print("Error: El precio debe ser mayor que 0. Intente nuevamente.")
                continue
            return precio
        except ValueError:
            print("Error: Ingrese un valor numérico válido para el precio (ej: 1500.50)")

def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en inventario: ").strip())
            if cantidad < 0:
                print("Error: La cantidad no puede ser negativa. Intente nuevamente.")
                continue
            return cantidad
        except ValueError:
            print("Error: Ingrese un número entero válido para la cantidad (ej: 12)")



    # Cantidad total de productos registrados
    cantidad_total = len(inventario)

    # Valor total del inventario (sumatoria de precio × cantidad)
    valor_total = 0
    for p in inventario:
        valor_total += p["precio"] * p["cantidad"]

    print("=" * 40)
    print(f"  Cantidad total de productos : {cantidad_total}")
    print(f"  Valor total del inventario  : ${valor_total:,.2f}")
    print("=" * 40)

def mostrar_menu():
    print("\n" + "=" * 40)
    print("       GESTIÓN DE INVENTARIO")
    print("=" * 40)
    print("  1. Agregar producto")
    print("  2. Listar productos")
    print("  3. Eliminar producto")
    print("  4. Calcular estadísticas")
    print("  0. Salir")
    print("=" * 40)

import Task
# -------------------------------
# Punto de entrada principal
# -------------------------------

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            calcular_estadisticas()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor elige entre 0 y 4.")

main()