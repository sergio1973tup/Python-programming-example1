from os import system
from persona import opcion1, opcion2, opcion3, punto12a, buscarPorId
import time


menu = ['1-CARGAR','2-ELIMINAR','3-MOSTRAR','4-RELACIONAR','5-BUSCAR POR ID', '6-SALIR']

def Menu():
    listaPersonas = []
    opcion = ''
    while(opcion != '6'):
        system('cls')
        for i in menu:
            print(f'{i}: ')
        opcion = input('seleccione la que desea hacer: ')

        if(opcion == '1'):
            listaPersonas.append(opcion1.opcion1())
        elif(opcion == '2'):
            listaPersonas.pop(opcion2.eliminar(listaPersonas))
        elif(opcion == '3'):
            opcion3.mostrar(listaPersonas)
            time.sleep(3)
        elif(opcion == '4'):
            punto12a.Relacion(listaPersonas)
        elif(opcion == '5'):
            buscarPorId.buscarPorId(listaPersonas)
            time.sleep(3)
        
    system('cls')
    print('Gracias por usarnos')
    time.sleep(2)
    system('cls')
