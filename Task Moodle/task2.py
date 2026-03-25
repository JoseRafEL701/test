#Gestionar varios productos en el inventario mediante un menú interactivo.
#Organizar registros, validar datos y obtener estadísticas básicas de forma sencilla.
#Aplicar estructuras condicionales (if/elif/else) y bucles (while y for) en Python, utilizando listas y diccionarios para almacenar productos, validar entradas y calcular estadísticas del inventario.

# -------------------------------
# Solicitar datos al usuario
# -------------------------------

while True:
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre:  # Verificamos que no esté vacío
        break
    print("Error: El nombre no puede estar vacío. Intente nuevamente.")

# Validación del precio
while True:
    try:
        precio_texto = input("Ingrese el precio unitario: ").strip()
        precio = float(precio_texto)
        if precio <= 0:
            print("Error: El precio debe ser mayor que 0. Intente nuevamente.")
            continue
        break
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el precio (ej: 1500.50)")

# Validación de la cantidad
while True:
    try:
        cantidad_texto = input("Ingrese la cantidad en inventario: ").strip()
        cantidad = int(cantidad_texto)
        if cantidad < 0:
            print("Error: La cantidad no puede ser negativa. Intente nuevamente.")
            continue
        break
    except ValueError:
        print("Error: Ingrese un número entero válido para la cantidad (ej: 12)")

# -------------------------------
# Procesamiento (cálculo)
# -------------------------------

costo_total = precio * cantidad

# -------------------------------
# Mostrar resultado
# -------------------------------

print("\n" + "="*50)
print("          REGISTRO DE PRODUCTO")
print("="*50)
print(f"Producto      : {nombre}")
print(f"Precio unitario: ${precio:,.2f}")
print(f"Cantidad      : {cantidad}")
print(f"Total         : ${costo_total:,.2f}")
print("="*50)

# Fin del programa