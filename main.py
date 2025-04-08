from productos_controller import *
def menu():
    while True:
        print("\n--- ADMIN: GESTIÓN DE PRODUCTOS ---")
        print("1. Ver productos")
        print("2. Agregar producto")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            productos = obtener_productos()
            for p in productos:
                print(f"{p['id_producto']} | {p['nombre']} | ${p['precio']} | Stock: {p['stock']}")
        
        elif opcion == "2":
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            id_categoria = int(input("ID Categoría: "))
            fecha = input("Fecha de creación (YYYY-MM-DD): ")
            agregar_producto(nombre, descripcion, precio, stock, id_categoria, fecha)
            print("Producto agregado.")

        elif opcion == "3":
            id_producto = int(input("ID del producto a editar: "))
            nombre = input("Nuevo nombre: ")
            descripcion = input("Nueva descripción: ")
            precio = float(input("Nuevo precio: "))
            stock = int(input("Nuevo stock: "))
            id_categoria = int(input("Nuevo ID de categoría: "))
            editar_producto(id_producto, nombre, descripcion, precio, stock, id_categoria)
            print("Producto actualizado.")

        elif opcion == "4":
            id_producto = int(input("ID del producto a eliminar: "))
            eliminar_producto(id_producto)
            print("Producto eliminado.")

        elif opcion == "5":
            break

        else:
            print("Opción no válida")
menu()