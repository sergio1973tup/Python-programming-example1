from os import system
import time
from persona import detallePersona

def mostrar(listaPersonas):
    system('cls')
    if(len(listaPersonas) > 0):
        for i in listaPersonas:
            for j,v in i.items():
                if(j == 'Relacion'):
                    print(f'Relacionado con la persona: ')
                    detallePersona.detallePersona(listaPersonas, i[j])
                else: 
                    print(f'{j}-{v}')
            print('\n')