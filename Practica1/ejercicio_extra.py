list = []
while True:
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto")
    print("3. Listar productos")
    print("4. Cerrar programa")
    option = input("Seleccione una opcion: ")
    if option == "1":
        name = input("Ingrese nombre del producto: ")
        stock = int(input("Ingrese cantidad de productos: "))
        flag=False
        for search in list:
            if search["Producto"] == name:
                search["Cantidad"] += stock
                flag=True
        if flag == False:
            product = {"Producto":name,"Cantidad":stock}
            list.append(product)
    elif option == "2":
        name = input("Ingrese nombre de producto a eliminar: ")
        cont = 0
        flag = False
        for search in list:
            if search["Producto"] == name:
                del list[cont]
                flag = True
            cont+=1
        if flag == False:
            print("No existe el producto",name)
    elif option == "3":
        for product in list:
            print(product["Producto"],product["Cantidad"])
    elif option == "4":
        break