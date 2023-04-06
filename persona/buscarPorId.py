from os import system
from persona import detallePersona

def buscarPorId(listaPersonas):
    system('cls')
    Id = input('ingrese el ID de la persona que desea ver: ') 
    for i in listaPersonas:
        if(i['id'] == Id):
            for j,k in i.items():
                if(j == 'Relacion'):
                    print(f'{j} En relacion con la persona: ')
                    detallePersona.detallePersona(listaPersonas, i[j])
                else: 
                    print(f'{j}-{k}')
