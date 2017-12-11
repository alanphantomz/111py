# -*- coding: cp1252 -*-
def decifrar(data, incasc, recub):
    mensaje = ""
    data = 'x' + data
    cont = 0  # de 1 hasta recub
    for i in data:
        if cont == recub * 2:
            mensaje = mensaje + chr(ord(i) + incasc)
            cont = 0
        else:
            cont += 1
    return mensaje


data = raw_input("Message>> ")
incasc = input("IncAsc>> ")
recub = input("Onion>> ")

print "Mensaje: " + decifrar(data, incasc, recub)
raw_input('press any key...')
