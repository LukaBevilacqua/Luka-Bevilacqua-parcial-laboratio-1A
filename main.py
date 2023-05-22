import os
from funciones_parcial import *

lista_insumos = []
flag_cargar_lista = False

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
            listarInsumosOrdenados(lista_insumos)
        case "10":
            rta = input("Seguro que desea salir? s/n: ").lower().strip()
            if rta == "s":
                break
    os.system("pause")
