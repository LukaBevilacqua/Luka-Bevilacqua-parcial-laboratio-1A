import json

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
    print("|  10- Agregar nuevo producto           |")
    print("|  11- Guardar datos actualizados       |")
    print("|  12- Salir                            |")
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
        factura.write("TOTAL: ${}\n".format(almacenador_precios))
    factura.close()


def guardarEnFormatoJSON(lista:list):
    lista_alimentos = []
    for insumo in lista:
        if "Alimento" in insumo['NOMBRE']:
            lista_alimentos.append(insumo)
    with open("Alimentos.json", "w", encoding="utf-8") as file:
        json.dump(lista_alimentos, file, indent=4)


def leerDesdeFormatoJSON(lista:list):
    with open("Alimentos.json", "r") as file:
        lista = json.load(file)
    for insumo in lista:
        print(f"ID: {insumo['ID']} NOMBRE: {insumo['NOMBRE']} MARCA: {insumo['MARCA']} PRECIO: {insumo['PRECIO']} CARACTERISTICAS: {insumo['CARACTERISTICAS']}\n")


def actualizarPrecios(lista:list):
    lista_insumos_actualizados = list(map(lambda insumo: {
        "ID": insumo['ID'],
        "NOMBRE": insumo['NOMBRE'],
        "MARCA": insumo['MARCA'],
        "PRECIO": "${:.2f}".format(float(insumo['PRECIO'].replace("$","")) * 1.084),
        "CARACTERISTICAS": insumo['CARACTERISTICAS']
    }, lista))
    with open("insumos.csv", "w", newline="", encoding="utf-8") as file:
        file.write("ID, NOMBRE, MARCA, PRECIO, CARACTERISTICAS\n")
        for insumo in lista_insumos_actualizados:
            linea = "{},{},{},{},{}\n".format(insumo['ID'], insumo['NOMBRE'], insumo['MARCA'], insumo['PRECIO'], insumo['CARACTERISTICAS'])
            file.write(linea)

def agregarNuevoProducto(lista:list):
    lista_productos_nuevos_marcas = []
    lista_ids = []
    lista_nombres = []
    lista_precios = []
    lista_caracteristicas = []
    aux = []
    with open("marcas.txt", "r") as file:
        contenido = file.read()
        print("--------------------------------")
        print(contenido)
        print("--------------------------------")
        file.close()
    rta = input("Que marca desea agregar?: ").capitalize().strip()
    if rta in contenido:
        lista_productos_nuevos_marcas.append(rta)
        print("--------------------------------")
        rta = input("Ingrese el ID: ").strip()
        while not rta.isdigit():
            print("--------------------------------")
            print("El ID ingresado no es un numero")
            rta = input("Ingrese un ID: ").strip()
        id = len(lista)
        while int(rta) < id:
            print("--------------------------------")
            print("El ID ya existe")
            rta = input("Ingrese un ID: ").strip()
        lista_ids.append(rta)
        print("--------------------------------")
        rta = input("Ingrese el nombre del producto: ").capitalize().strip()
        lista_nombres.append(rta)
        print("--------------------------------")
        rta = input("Ingrese el precio del producto: ")
        while not rta.isdigit() and float(rta) < 0:
            print("--------------------------------")
            print("El valor ingresado no es valido")
            rta = input("Ingrese el precio del producto nuevamente: ")
        lista_precios.append(rta)
        print("--------------------------------")
        rta = input("Ingrese una caracteristica del producto: ").capitalize().strip()
        lista_caracteristicas.append(rta)
        aux.append({"ID": lista_ids, "NOMBRE": lista_nombres,"MARCA": lista_productos_nuevos_marcas, "PRECIO": lista_precios, "CARACTERISTICAS": lista_caracteristicas})
        for elemento in aux:
            lista.append({"ID": elemento['ID'], "NOMBRE": elemento['NOMBRE'],"MARCA": elemento['MARCA'], "PRECIO": elemento['PRECIO'], "CARACTERISTICAS": elemento['CARACTERISTICAS']})
        print("------------------------------------------")
        print("| Se agrego un nuevo producto a la lista |")
        print("------------------------------------------")
    else:
        print("No se encontro la marca ingresada")




def guardarDatosActualizados(lista:list):
    rta = input("Eliga el formato de exportacion csv/json: ").lower().strip()
    if rta == "json":
        rta = input("Ingrese el nombre del archivo: ").capitalize().strip
        with open(rta, "w", encoding="utf-8") as file:
            json.dump(lista, file, indent=4)
    elif rta == "csv":
        rta = input("Ingrese el nombre del archivo: ").capitalize().strip
        with open(rta, "w", encoding="utf-8") as file:
            file.write("ID, NOMBRE, MARCA, PRECIO, CARACTERISTICAS\n")
        for insumo in lista:
            linea = "{},{},{},{},{}\n".format(insumo['ID'], insumo['NOMBRE'], insumo['MARCA'], insumo['PRECIO'], insumo['CARACTERISTICAS'])
            file.write(linea)
    else:
        print("el formato de exportacion no es valido")










