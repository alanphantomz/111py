import random


def cifrar(cad, incasc, recub):
    n_cad = ''
    for j in cad:
        asc = ord(j)
        for i in range(recub * 2 + 1):
            if i == recub:
                n_cad = n_cad + chr(asc - incasc)
            else:
                n_cad = n_cad + chr(random.randint(33, 122))  # randomico desde el 0 hasta el numero de palabras
    return n_cad
