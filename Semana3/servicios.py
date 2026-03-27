# servicios.py
# Módulo con las funciones de negocio (CRUD + Estadísticas)
# Usa: listas, diccionarios, tuplas, bucles y condicionales

def agregar_producto(inventario):
    """Agrega un nuevo producto al inventario con validaciones."""
    print("\n--- Agregar Nuevo Producto ---")
    
    nombre = input("Nombre del producto: ").strip()
    while not nombre:
        print("¡Error! El nombre no puede estar vacío.")
        nombre = input("Nombre del producto: ").strip()
    
    try:
        precio = float(input("Precio unitario ($): "))
        if precio <= 0:
            print("¡Error! El precio debe ser mayor a 0.")
            return False
    except ValueError:
        print("¡Error! Debes ingresar un número válido para el precio.")
        return False
    
    try:
        cantidad = int(input("Cantidad en stock: "))
        if cantidad < 0:
            print("¡Error! La cantidad no puede ser negativa.")
            return False
    except ValueError:
        print("¡Error! Debes ingresar un número entero para la cantidad.")
        return False
    
    producto = {
        "nombre": nombre.capitalize(),
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print(f" Producto '{nombre}' agregado correctamente.")
    return True


def mostrar_productos(inventario):
    """Muestra todos los productos en formato tabla."""
    if not inventario:
        print("\n  El inventario está vacío.")
        return
    
    print("\n--- LISTA DE PRODUCTOS ---")
    print(f"{'N°':<3} {'Nombre':<20} {'Precio':<10} {'Cantidad':<10} {'Valor Total':<12}")
    print("-" * 65)
    
    for i, p in enumerate(inventario, 1):
        valor = p["precio"] * p["cantidad"]
        print(f"{i:<3} {p['nombre']:<20} ${p['precio']:<9.2f} {p['cantidad']:<10} ${valor:<10.2f}")


def buscar_producto(inventario):
    """Busca un producto por nombre."""
    if not inventario:
        print("\n  El inventario está vacío.")
        return
    
    nombre_buscar = input("\nIngrese el nombre del producto a buscar: ").strip().capitalize()
    
    for p in inventario:
        if p["nombre"].lower() == nombre_buscar.lower():
            print("\n Producto encontrado:")
            print(f"Nombre     : {p['nombre']}")
            print(f"Precio     : ${p['precio']:.2f}")
            print(f"Cantidad   : {p['cantidad']}")
            print(f"Valor total: ${p['precio'] * p['cantidad']:.2f}")
            return
    print(f" No se encontró el producto '{nombre_buscar}'.")


def actualizar_producto(inventario):
    """Actualiza la información de un producto."""
    if not inventario:
        print("\n  El inventario está vacío.")
        return
    
    mostrar_productos(inventario)
    try:
        idx = int(input("\nIngrese el número del producto a actualizar: ")) - 1
        if idx < 0 or idx >= len(inventario):
            print("¡Error! Número de producto inválido.")
            return
    except ValueError:
        print("¡Error! Debes ingresar un número válido.")
        return
    
    p = inventario[idx]
    print(f"\nActualizando: {p['nombre']}")
    
    nuevo_nombre = input(f"Nuevo nombre (Enter para mantener): ").strip()
    if nuevo_nombre:
        p["nombre"] = nuevo_nombre.capitalize()
    
    nuevo_precio = input(f"Nuevo precio (Enter para mantener): ").strip()
    if nuevo_precio:
        try:
            precio = float(nuevo_precio)
            if precio > 0:
                p["precio"] = precio
        except ValueError:
            print("Precio inválido. Se mantiene el anterior.")
    
    nueva_cantidad = input(f"Nueva cantidad (Enter para mantener): ").strip()
    if nueva_cantidad:
        try:
            cantidad = int(nueva_cantidad)
            if cantidad >= 0:
                p["cantidad"] = cantidad
        except ValueError:
            print("Cantidad inválida. Se mantiene la anterior.")
    
    print(" Producto actualizado correctamente.")


def eliminar_producto(inventario):
    """Elimina un producto del inventario."""
    if not inventario:
        print("\n El inventario está vacío.")
        return
    
    mostrar_productos(inventario)
    try:
        idx = int(input("\nIngrese el número del producto a eliminar: ")) - 1
        if idx < 0 or idx >= len(inventario):
            print("¡Error! Número de producto inválido.")
            return
    except ValueError:
        print("¡Error! Debes ingresar un número válido.")
        return
    
    eliminado = inventario.pop(idx)
    print(f" Producto '{eliminado['nombre']}' eliminado correctamente.")


def obtener_estadisticas(inventario):
    """Calcula estadísticas y retorna una tupla.
    Retorna: (unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock)"""
    if not inventario:
        return 0, 0.0, None, None
    
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    
    return unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock


def mostrar_estadisticas(inventario):
    """Muestra las estadísticas del inventario de forma clara."""
    unidades, valor, caro, mayor_stock = obtener_estadisticas(inventario)
    
    if unidades == 0:
        print("\n  El inventario está vacío. No hay estadísticas.")
        return
    
    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    print(f"Unidades totales en stock     : {unidades}")
    print(f"Valor total del inventario    : ${valor:.2f}")
    print(f"Producto más caro             : {caro['nombre']} (${caro['precio']:.2f})")
    print(f"Producto con mayor stock      : {mayor_stock['nombre']} ({mayor_stock['cantidad']} unidades)")