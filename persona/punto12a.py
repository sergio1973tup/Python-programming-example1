from os import system
from persona import opcion3

def Relacion(listaPersonas):
    opcion3.mostrar(listaPersonas)

    seleccion = input('seleccione por el id la persona que va a relacionar: ')

    count = 0
    for i in listaPersonas:
        if(seleccion == i['id']):
            opcion3.mostrar(listaPersonas)
            listaPersonas[count]['Relacion'] = input('seleccione el id de la persona con la que tendra relacion: ') 
        count = count+1
    
    