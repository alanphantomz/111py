# -*- coding: utf-8 -*-
#!/usr/bin/python3

def leeLista(n):
    lista = []
    for i in range(0, n):
        lista.append(int(input("[%d]: "%i)))
    return lista

def mostrarLista(lista):
    for i in lista:
        print(i, end = ' ')




def main():
    n = int(input("Ingrese tamanio: "))
    mi_lista = leeLista(n)
    mostrarLista(mi_lista)

main()