import os
from funciones_parcial import *

lista_insumos = []
flag_cargar_lista = False
flag_json = False
flag_nuevos_productos = False

while True:
    os.system("cls")
    match(menu()):
        case "1":
            if flag_cargar_lista == False:
                cargar_datos("insumos.csv", "r", lista_insumos)
                flag_cargar_lista = True
                print("Se cargo la lista correctamente")
            else:
                print("La lista ya esta cargada")
        case "2":
            if flag_cargar_lista:
                listar_cantidad_por_marca(lista_insumos)
            else:
                print("Primero debe cargar la lista")
        case "3":
            if flag_cargar_lista:
                listar_insumos_por_marca(lista_insumos)
            else:
                print("Primero debe cargar la lista")
        case "4":
            if flag_cargar_lista:
                buscarInsumoPorLista(lista_insumos)
            else:
                print("Primero debe cargar la lista")
        case "5":
            if flag_cargar_lista:
                listarInsumosOrdenados(lista_insumos)
            else:
                print("Primero debe cargar la lista")
        case "6":
            if flag_cargar_lista:
                realizarCompras(lista_insumos)
            else:
                print("Primero debe cargar la lista")
        case "7":
            if flag_cargar_lista:
                guardarEnFormatoJSON(lista_insumos)
                flag_json = True
            else:
                print("Primero debe cargar la lista")
        case "8":
            if flag_cargar_lista and flag_json:
                leerDesdeFormatoJSON(lista_insumos)
            else:
                print("Primero debe cargar la lista o guardar en formato JSON")
        case "9":
            if flag_cargar_lista:
                actualizarPrecios(lista_insumos)
            else:
                print("Primero debe cargar la lista")
        case "10":
            if flag_cargar_lista:
                agregarNuevoProducto(lista_insumos)
                flag_nuevos_productos = True
            else:
                print("Primero debe cargar la lista")
        case "11":
            if flag_cargar_lista and flag_nuevos_productos:
                guardarDatosActualizados(lista_insumos)
            else:
                print("No hay productos nuevos para actualizar")
        case "12":
            rta = input("Seguro que desea salir? s/n: ").lower().strip()
            if rta == "s":
                break
    os.system("pause")
