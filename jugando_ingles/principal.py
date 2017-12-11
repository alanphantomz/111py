def muestraLista(lista):
    for i in range(len(lista)):
        print("[%s]"%lista[i],end="")
    print()
    return

def muestraMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print("[%s]"%matriz[i][j],end="")
        print()
    print()
    return

#IMPORTS
import random

#preguntaremos en español
palabras=[['sombrero','hat'],['sol','sun'],['tierra','land'],['country','pais']]
possibleTranslations=[
    ['hat','sun','too',0],
    ['hair','hearth','sun',0],
    ['brash','fat','land',0],
    ['pais','patria','ciudad',0]
    ]
vidas=5
puntaje=0
string="""Bienvenido a tu juego don adivinador,
Un juego en el que podras divertirte adivinando
La opcion correcta.
Numero de vidas=5
"""
print(string)
while  len(palabras)>0 and vidas>0:
    ran=random.randint(0,len(palabras)-1)#randomico desde el 0 hasta el numero de palabras
    print("\nCual es la traduccion para: %s?"%palabras[ran][0])
    print("1. %s     2. %s       3. %s"%(possibleTranslations[ran][0],possibleTranslations[ran][1],possibleTranslations[ran][2]))
    option=input("Escribe la palabra correcta: ")
    if palabras[ran][1]==option:
        puntaje+=1
        print("SI, adivinaste!!!")
    else:
        vidas-=1
        print("NO, fallaste :-( \a")
    possibleTranslations[ran][3]+=1
    if possibleTranslations[ran][3]>=3:
        del palabras[ran]
        del possibleTranslations[ran]
    
print("\nFin del juego :-(")
print("Numero de vidas: %d/5"%vidas)
print("Tu puntaje: %d"%puntaje)
print("Palabras sin completar: %d"%len(palabras))
