#Dado tres numeros A,B,C determinar y desplegar cual es el mayor
print("Introduzca tres numeros:")
A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))
if A>B:
    if A>C:print("El numero mayor es:",A)
    elif C>A:print("El numero mayor es:",C)
    else:print(A,"y",C,"son iguales y ambos son los mayores")
elif B>A:
    if B>C:print("El numero mayor es:",B)
    elif C>B:print("El numero mayor es:",C)
    else:print(B,"y",C,"son iguales y ambos son los mayores")
elif (C>B): print(C,"es el mayor y",A,"y",B,"son iguales")
elif (B>C): print(C,"es el menor y",A,"y",B,"son iguales y mayores")
else: print(A,B,C,"son iguales")
