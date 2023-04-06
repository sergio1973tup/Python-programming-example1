from os import system
import time
from persona import opcion3

def eliminar(listaPersonas):
    if(len(listaPersonas) > 0):
        opcion3.mostrar(listaPersonas)
        
        id = input('elija el id de la persona que desea eliminar: ')
        count = 0
        for i in listaPersonas:
            if(id == i['id']):
                return count
            count = count+1