# app.py
# Programa principal - Menú interactivo (opciones 1-9)
# Usa: while, if/elif/else, import de módulos

from servicios import (
    agregar_producto, mostrar_productos, buscar_producto,
    actualizar_producto, eliminar_producto, mostrar_estadisticas
)
from archivos import guardar_csv, cargar_csv

def mostrar_menu():
    """Muestra el menú principal actualizado (1-9)"""
    print("\n" + "="*55)
    print("       SISTEMA DE GESTIÓN DE INVENTARIO")
    print("="*55)
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas del inventario")
    print("7. Guardar inventario en CSV")
    print("8. Cargar inventario desde CSV")
    print("9. Salir")
    print("="*55)


def main():
    """Función principal que controla el flujo del sistema"""
    inventario = []  # Lista de diccionarios
    print("¡Bienvenido al Sistema de Gestión de Inventario!")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-9): ").strip()
        
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
            guardar_csv(inventario)
        elif opcion == "8":
            print("\n--- Cargar Inventario desde CSV ---")
            print("1. Sobrescribir inventario actual")
            print("2. Fusionar (agregar al actual)")
            sub_op = input("Elija (1 o 2): ").strip()
            
            nuevo_inventario, omitidas = cargar_csv()
            if nuevo_inventario:
                if sub_op == "1":
                    inventario = nuevo_inventario
                    print(" Inventario sobrescrito correctamente.")
                elif sub_op == "2":
                    inventario.extend(nuevo_inventario)
                    print(" Productos fusionados correctamente.")
                else:
                    print("Opción inválida. No se cargó nada.")
        elif opcion == "9":
            print("\n ¡Gracias por usar el Sistema de Gestión de Inventario!")
            break
        else:
            print(" Opción inválida. Por favor seleccione entre 1 y 9.")
        
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()