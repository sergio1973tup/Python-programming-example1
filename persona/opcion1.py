from os import system
rotulos = ['id','Nombre','Edad']
nuevaPersona = {}

def opcion1():
    system('cls')
    print('Ingree una persona')
    nuevaPersona = {i: (input(f'ingrese {i}: ')) for i in rotulos}

    return nuevaPersona