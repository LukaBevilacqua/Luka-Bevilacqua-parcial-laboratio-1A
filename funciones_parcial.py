def menu():
    print("-----------------------------------------")
    print("|  *** Menu de Opciones ***             |")
    print("-----------------------------------------")
    print("|  1- Cargar datos desde archivo        |")
    print("|  2- Listar cantidad por marca         |")
    print("|  3- Listar insumos por marca          |")
    print("|  4- Buscar insumo por característica  |")
    print("|  5- Listar insumos ordenados          |")
    print("|  6- Realizar compras                  |")
    print("|  7- Guardar en formato JSON           |")
    print("|  8- Leer desde formato JSON           |")
    print("|  9- Actualizar precios                |")
    print("|  10- salir                            |")
    print("-----------------------------------------")
    opcion = input("Ingrese opcion: ").strip()
    return opcion

def cargar_datos(ruta:str, formato_lectura:str, lista)->list:
    with open(ruta, formato_lectura, encoding="utf-8") as file:
        lineas = file.readlines()
        lista_spliteada = []
        lista_replace = []
        for linea in lineas[1:]:
            lista_replace.append(linea.replace("\n", ""))
        for linea in lista_replace:
            lista_spliteada.append(linea.split(","))
        for elemento in lista_spliteada:
            lista.append({"ID": elemento[0], "NOMBRE": elemento[1],"MARCA": elemento[2], "PRECIO": elemento[3], "CARACTERISTICAS": elemento[4]})
    return lista

def listar_cantidad_por_marca(lista:list):
    cantidad_por_marca = {}
    for elemento in lista:
        marca = elemento['MARCA']
        if marca in cantidad_por_marca:
            cantidad_por_marca[marca] += 1
        else:
            cantidad_por_marca[marca] = 1
    for marca, cantidad in cantidad_por_marca.items():
        print(f"Marca: {marca} | Cantidad: {cantidad}")
        print("-----------------------------------------------")


def esta_en_lista(lista:list, key:str)->bool:
    esta = False
    for elemento in lista:
        if elemento == key:
            esta = True
            break
    return esta


def listar_insumos_por_marca(lista:list):
    marcas = []
    for insumos in lista:
        if not esta_en_lista(marcas, insumos['MARCA']):
            marcas.append(insumos['MARCA'])
    for marca in marcas:
        print("------------------------------------")
        print("Marca: " + marca)
        for insumos in lista:
            if insumos['MARCA'] == marca:
                print(insumos['NOMBRE'], insumos['PRECIO'])


def buscarInsumoPorLista(lista:list):
    caracteristica = input("Ingrese la caracteristica que desea en su producto: ").capitalize()
    insumos_encontrados = []
    for insumo in lista:
        caracteristicas = insumo['CARACTERISTICAS'].split('~')
        if caracteristica in caracteristicas:
            insumos_encontrados.append(insumo)
    if len(insumos_encontrados) > 0:
        print("---------------------------------------------------------------------")
        print("Insumos encontrados:")
        for insumo in insumos_encontrados:
            print(f"ID: {insumo['ID']} NOMBRE:{insumo['NOMBRE']} MARCA: {insumo['MARCA']} PRECIO:{insumo['PRECIO']}")
        print("---------------------------------------------------------------------")
    else:
        print("No se encontro ningun insumo con esa caracteristica")


def listarInsumosOrdenados(lista:list):
    n = len(lista)
    for i in range(n - 1): 
        for j in range(n - i - 1):
            if lista[j]['MARCA'] > lista[j + 1]['MARCA'] or (lista[j]['MARCA'] == lista[j + 1]['MARCA'] and lista[j]['PRECIO'] < lista[j + 1]['PRECIO']):
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        for insumo in lista:
            caracteristicas = insumo['CARACTERISTICAS'].split('~')
            primera_caracteristica = caracteristicas[0]
            print(f" MARCA: {insumo['MARCA']} ID: {insumo['ID']} NOMBRE: {insumo['NOMBRE']} PRECIO: {insumo['PRECIO']} CARACTERÍSTICA: {primera_caracteristica}")


def realizarCompras(lista:list):
    lista_marcas = []
    lista_insumos_comprados = []
    lista_cantidad_insumos_comprados = []
    contador_compras = 0
    almacenador_precios = 0
    while True:
        rta = input("Ingrese la marca del producto que desea comprar: ").capitalize().strip()
        print("---------------------------------------------------------------------")
        for insumo in lista:
            if insumo['MARCA'] == rta:
                lista_marcas.append(insumo)
                print(f" ID: {insumo['ID']} MARCA: {insumo['MARCA']}  NOMBRE: {insumo['NOMBRE']} PRECIO: {insumo['PRECIO']}")
        print("---------------------------------------------------------------------")
        rta = input("Escriba el ID del producto que desea comprar: ").strip()
        while not rta.isdigit():
            rta = input("Por favor, escriba el ID del producto que desea comprar: ")
        print("---------------------------------------------------------------------")
        for insumo in lista_marcas:
            if insumo['ID'] == rta:
                lista_insumos_comprados.append(insumo)
                rta = input("Cuantos desea comprar? :").strip()
                while not rta.isdigit() and not rta > 0:
                    rta = input("Por favor ponga un numero que sea valido, cuantos desea comprar? :").strip
                lista_cantidad_insumos_comprados.append(rta)
                print(f"Guardamos {lista_cantidad_insumos_comprados[contador_compras]} productos con el ID: {insumo['ID']} para usted")
        print("---------------------------------------------------------------------")
        subtotal = float(lista_marcas[contador_compras]['PRECIO'].replace("$","")) * float(lista_cantidad_insumos_comprados[contador_compras])
        almacenador_precios += subtotal
        print(almacenador_precios)
        rta = input("Desea comprar algo mas? s/n: ").strip().lower()
        while rta != "s" and rta != "n":
            rta = input("Por favor, responda con s/n: ").strip().lower()
        if rta == "n":
            print(f"El total de la compra es: ${almacenador_precios}")
            break
        contador_compras += 1
        print("---------------------------------------------------------------------")
    factura = open("factura.txt","w")
    if len(lista_insumos_comprados) > 0:
        for i in range(len(lista_insumos_comprados)):
            insumo = lista_insumos_comprados[i]
            cantidad = lista_cantidad_insumos_comprados[i]
            factura.write("CANTIDAD: {}\nPRODUCTO: {}, {}\nSUBTOTAL: {}\n".format(cantidad, insumo['MARCA'], insumo['NOMBRE'], insumo['PRECIO']))
        factura.write("TOTAL: {}\n".format(almacenador_precios))
    factura.close()


def guardarEnFormatoJSON():
    pass