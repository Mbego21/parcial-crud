import json
import os

def confirmar_inventario():
    if not os.path.exists("inventario.json"):
        with open("inventario.json", "w") as file:
            json.dump([],file)
        print("Archivo inventario.json creado.")

def cargar_inventario():
    with open("inventario.json", "r") as file:
        return json.load(file)
        
def modificar_inventario(inventario):
    with open("inventario.json", 'w') as file:
        json.dump(inventario, file, indent=4)

def crear_producto(inventario):
    producto = input("nombre del producto: ")
    for productos in inventario:
        if productos["nombre"] == producto:
            print("El producto ya existe.")
            return
    precio = input("precio del producto: ")
    cantidad = input("cantidad en stock: ")
    inventario.append({"nombre": producto, "precio": precio, "cantidad": cantidad})
    modificar_inventario(inventario)
    print("Su producto ha sido agregado.")

def mostrar_todos_productos(inventario):
    if not inventario:
        print("el inventario está vacío.")
    else:
        print("lista de productos:")
        for producto in inventario:
            print(f"Producto: {producto['nombre']}\nPrecio: {producto['precio']}\nCantidad: {producto['cantidad']}\n")

def mostrar_producto(inventario):
    nombre_producto = input("nombre del producto: ")
    for producto in inventario:
        if producto["nombre"] == nombre_producto:
            print(f"Producto: {producto['nombre']}\nPrecio: {producto['precio']}\nCantidad: {producto['cantidad']}\n")
            return
    print("el producto no existe.") 

def actualizar_producto(inventario):
    nombre_producto = input("nombre del producto: ")
    for producto in inventario:
        if producto["nombre"] == nombre_producto:
            nuevo_precio = input("nuevo precio del producto: ")
            nueva_cantidad = input("nueva cantidad en stock: ")
            if nuevo_precio:
                producto["precio"] = nuevo_precio
            if nueva_cantidad:
                producto["cantidad"] = nueva_cantidad
            modificar_inventario(inventario)
            print("el producto ha sido actualizado.")
            return
    print("el producto no existe.")      

def eliminar_producto(inventario):
    nombre_producto = input("ingrese el nombre del producto a eliminar: ")
    for producto in inventario:
        if producto["nombre"] == nombre_producto:
            inventario.remove(producto)
            modificar_inventario(inventario)
            print("el producto ha sido eliminado.")
            return
    print("el producto no existe.")

def menu():
    confirmar_inventario()
    inventario = cargar_inventario()
    while True:
        print("--Inventario --"+"\n"+"1. Crear producto"+"\n"+"2. Mostrar todos los productos"+"\n"+"3. Mostrar informacion de un producto"+"\n"+"4. Actualizar producto"+"\n"+"5. Eliminar producto"+"\n"+"6. Salir")
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            crear_producto(inventario)
        elif opcion == "2":
            mostrar_todos_productos(inventario)
        elif opcion == '3':
            mostrar_producto(inventario)
        elif opcion == '4':
            actualizar_producto(inventario)
        elif opcion == '5':
            eliminar_producto(inventario)
        elif opcion == '6':
            break
        else:
            print("opcion no valida. intentalo de nuevo.")

menu()