# =====================================================
# SISTEMA DE GESTIÓN DE INVENTARIO
# =====================================================
# Se utiliza: listas, diccionarios, if/elif/else, while y for
# =====================================================

def mostrar_menu():
    """Función que muestra el menú principal"""
    print("\n" + "="*50)
    print("       SISTEMA DE GESTIÓN DE INVENTARIO")
    print("="*50)
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas del inventario")
    print("7. Salir")
    print("="*50)


def agregar_producto(inventario):
    """Función para agregar un nuevo producto
    Usa: input(), while (validación), try/except (manejo de errores)"""
    print("\n--- Agregar Nuevo Producto ---")
    
    # Validación del nombre (no puede estar vacío)
    nombre = input("Nombre del producto: ").strip()
    while not nombre:
        print("¡Error! El nombre no puede estar vacío.")
        nombre = input("Nombre del producto: ").strip()
    
    # Validación del precio
    try:
        precio = float(input("Precio unitario ($): "))
        if precio <= 0:
            print("¡Error! El precio debe ser mayor a 0.")
            return
    except ValueError:
        print("¡Error! Debes ingresar un número válido para el precio.")
        return
    
    # Validación de la cantidad
    try:
        cantidad = int(input("Cantidad en stock: "))
        if cantidad < 0:
            print("¡Error! La cantidad no puede ser negativa.")
            return
    except ValueError:
        print("¡Error! Debes ingresar un número entero para la cantidad.")
        return
    
    # Crear diccionario y agregarlo a la lista
    producto = {
        "nombre": nombre.capitalize(),
        "precio": precio,
        "cantidad": cantidad
    }
    
    inventario.append(producto)   # Agrega el diccionario a la lista
    print(f" Producto '{nombre}' agregado correctamente.")


def mostrar_productos(inventario):
    """Función para mostrar todos los productos
    Usa: for (recorrer lista)"""
    if not inventario:
        print("\n  El inventario está vacío.")
        return
    
    print("\n--- LISTA DE PRODUCTOS ---")
    print(f"{'N°':<3} {'Nombre':<20} {'Precio':<10} {'Cantidad':<10} {'Valor Total':<12}")
    print("-" * 60)
    
    for i, producto in enumerate(inventario, 1):   # Bucle for con enumerate
        valor_total = producto["precio"] * producto["cantidad"]
        print(f"{i:<3} {producto['nombre']:<20} ${producto['precio']:<9.2f} "
              f"{producto['cantidad']:<10} ${valor_total:<10.2f}")


def buscar_producto(inventario):
    """Función para buscar un producto por nombre
    Usa: for (recorrer lista) + if (comparación)"""
    if not inventario:
        print("\n  El inventario está vacío.")
        return
    
    nombre_buscar = input("\nIngrese el nombre del producto a buscar: ").strip().capitalize()
    
    for producto in inventario:          # Recorre la lista con for
        if producto["nombre"].lower() == nombre_buscar.lower():   # Comparación insensible a mayúsculas
            print("\n✅ Producto encontrado:")
            print(f"Nombre     : {producto['nombre']}")
            print(f"Precio     : ${producto['precio']:.2f}")
            print(f"Cantidad   : {producto['cantidad']}")
            print(f"Valor total: ${producto['precio'] * producto['cantidad']:.2f}")
            return   # Sale de la función al encontrar
    
    print(f"❌ No se encontró ningún producto con el nombre '{nombre_buscar}'.")


def actualizar_producto(inventario):
    """Función para actualizar un producto existente
    Usa: if/else, try/except y enumerate"""
    if not inventario:
        print("\n  El inventario está vacío.")
        return
    
    mostrar_productos(inventario)
    
    try:
        indice = int(input("\nIngrese el número del producto a actualizar: ")) - 1
        if indice < 0 or indice >= len(inventario):
            print("¡Error! Número de producto inválido.")
            return
    except ValueError:
        print("¡Error! Debes ingresar un número válido.")
        return
    
    producto = inventario[indice]
    print(f"\nActualizando: {producto['nombre']}")
    
    # Actualizar nombre (opcional)
    nuevo_nombre = input(f"Nuevo nombre (Enter para mantener): ").strip()
    if nuevo_nombre:
        producto["nombre"] = nuevo_nombre.capitalize()
    
    # Actualizar precio (opcional)
    nuevo_precio = input(f"Nuevo precio (Enter para mantener): ").strip()
    if nuevo_precio:
        try:
            precio = float(nuevo_precio)
            if precio > 0:
                producto["precio"] = precio
        except ValueError:
            print("Precio inválido. Se mantiene el anterior.")
    
    # Actualizar cantidad (opcional)
    nueva_cantidad = input(f"Nueva cantidad (Enter para mantener): ").strip()
    if nueva_cantidad:
        try:
            cantidad = int(nueva_cantidad)
            if cantidad >= 0:
                producto["cantidad"] = cantidad
        except ValueError:
            print("Cantidad inválida. Se mantiene la anterior.")
    
    print(" Producto actualizado correctamente.")


def eliminar_producto(inventario):
    """Función para eliminar un producto
    Usa: pop() para eliminar de la lista"""
    if not inventario:
        print("\n  El inventario está vacío.")
        return
    
    mostrar_productos(inventario)
    
    try:
        indice = int(input("\nIngrese el número del producto a eliminar: ")) - 1
        if indice < 0 or indice >= len(inventario):
            print("¡Error! Número de producto inválido.")
            return
    except ValueError:
        print("¡Error! Debes ingresar un número válido.")
        return
    
    producto_eliminado = inventario.pop(indice)   # Elimina y retorna el producto
    print(f" Producto '{producto_eliminado['nombre']}' eliminado correctamente.")


def mostrar_estadisticas(inventario):
    """Función para calcular estadísticas
    Usa: len(), for (suma), max() con lambda"""
    if not inventario:
        print("\n  El inventario está vacío. No hay estadísticas.")
        return
    
    total_productos = len(inventario)                    # Cantidad total de productos
    valor_total_inventario = 0
    
    # Calcular valor total con bucle for
    for producto in inventario:
        valor_total_inventario += producto["precio"] * producto["cantidad"]
    
    # Encontrar el producto más caro
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    
    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    print(f"Total de productos diferentes : {total_productos}")
    print(f"Valor total del inventario    : ${valor_total_inventario:.2f}")
    print(f"Producto más caro             : {producto_mas_caro['nombre']} (${producto_mas_caro['precio']:.2f})")


# ====================== FUNCIÓN PRINCIPAL ======================
def main():
    """Función principal del programa
    Usa: while (bucle principal del menú)"""
    inventario = []  # Lista vacía que guardará diccionarios de productos
    
    print("¡Bienvenido al Sistema de Gestión de Inventario!")
    
    while True:   # Bucle while que mantiene el menú activo
        mostrar_menu()
        
        opcion = input("\nSeleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            mostrar_productos(inventario)
        elif opcion == "3":
            buscar_producto(inventario)
        elif opcion == "4":
            actualizar_producto(inventario)
        elif opcion == "5":
            eliminar_producto(inventario)
        elif opcion == "6":
            mostrar_estadisticas(inventario)
        elif opcion == "7":
            print("\n ¡Gracias por usar el Sistema de Gestión de Inventario!")
            break
        else:
            print(" Opción inválida. Por favor seleccione una opción entre 1 y 7.")
        
        input("\nPresione Enter para continuar...")


# ====================== EJECUCIÓN DEL PROGRAMA ======================
if __name__ == "__main__":
    main()