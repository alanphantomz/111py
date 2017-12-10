print("Leer dos numeros A y B, del mayor restarle\
el menor, Desplegar el resultado")
A=float(input("A:"))
B=float(input("B:"))

if (A>B):
    print("Resultado es:",A-B)
elif (B>A):
    print("Resultado es:",B-A)
else:
    print("El resultado es: 0 pues\
 A y B son iguales!!")
