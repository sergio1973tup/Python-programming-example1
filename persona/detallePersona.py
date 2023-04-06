from os import system

def detallePersona(listaPersonas, id):
    count = 0
    for i in listaPersonas:
        if(i['id'] == id):
            for j,v in listaPersonas[count].items():
                print(f'{j} - {v}')
        count = count+1
