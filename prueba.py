import os

productos={1:"Pantalones",
           2:"Camisas",
           3:"Corbatas",
           4:"Casacas"}

precios={1:200.00,
         2:120.00,
         3:50.00,
         4:350.00}

stocks={1:50,
       2:45,
       3:30,
       4:15}

#Listo
def mostrarProductos(productos,precios,stocks):
    print("#################################\nLista de Productos: \n#################################")
    for clave in productos:
        print(f"{clave}: {productos[clave]}, {precios[clave]}, {stocks[clave]}")
    print("#################################")
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
    print("#################################\n")


#Listo
def eliminarProducto(productos,precios,stocks):
    id=int(input("ingrese el id del producto a eliminar "))

    if id not in productos.keys():
        print("no se encuentra dicha id")
        return
    
    del productos[id]
    del precios[id]
    del stocks[id]

    productos_actualizados = {}
    precios_actualizados = {}
    stocks_actualizados = {}
        
    nueva_clave = 1
    for clave in sorted(productos.keys()):
        productos_actualizados[nueva_clave] = productos[clave]
        precios_actualizados[nueva_clave] = precios[clave]
        stocks_actualizados[nueva_clave] = stocks[clave]
        nueva_clave += 1
        
    return productos_actualizados, precios_actualizados, stocks_actualizados

#Listo
def actualizarProducto(productos,precios,stocks):
    id=int(input("ingrese el id del producto a actualizar "))
    if id not in productos.keys():
        print("la id no se encuentra en la lista de productos")
        print("¿desea agregar una nueva id? [S] o [N]")
        opcion=input("ingresa la opcion ")
        opcion=opcion.upper()
        if opcion=='S':
            agregarProducto(productos,precios,stocks)
            return
        elif opcion=='N':
            return
    
    prodNombre=input("ingrese el nuevo nombre del producto ")
    prodPrecio=float(input("ingrese el nuevo precio del producto "))
    prodStock=int(input("ingrese el nuevo stock del producto "))


    productos[id]=prodNombre
    precios[id]=prodPrecio
    stocks[id]=prodStock

##Listo
def agregarProducto(productos, precios, stocks):
    producto = input("Ingresa el producto a agregar: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))

    nueva_clave = max(productos.keys()) + 1 if productos else 1

    productos[nueva_clave] = producto
    precios[nueva_clave] = precio
    stocks[nueva_clave] = stock



while True:
    os.system('cls')
    mostrarProductos(productos,precios,stocks)

    opcion=int(input("ingresa la opción "))
    if opcion==1:
        agregarProducto(productos,precios,stocks)
    elif opcion==2:
        productos,precios,stocks=eliminarProducto(productos,precios,stocks)

    elif opcion==3:
        actualizarProducto(productos,precios,stocks)
    elif opcion==4:
        break
    os.system('cls')



