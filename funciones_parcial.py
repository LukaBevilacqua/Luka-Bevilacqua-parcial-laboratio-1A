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
    opcion = input("Ingrese opcion: ")
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
    flag_cambio = True
    contador = 1
    while flag_cambio:
        for insumo in range(len(lista) - contador):
            if insumo['MARCA'] > insumo['MARCA' + 1]:
                aux = insumo['MARCA']
                insumo['MARCA'] = insumo['MARCA' + 1]
                insumo['MARCA' + 1] = aux
                flag_cambio = True
            print(insumo)
        contador = contador + 1



# def realizarCompras(lista:list):
#     pass