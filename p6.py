#Dados dos numeros A y B, realizar el producto
#de los dos numeros por sumas sucesivas, almacener
#resultado en una variable P, mostrar el resultado.

A=int(input("A:"))
B=int(input("B:"))
P=0
for x in range(B) : P+=A
print("El producto es:",P)
