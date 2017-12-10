#Calcular el factorial de un numero N,
#mostrar el numero y su factorial
print("Ingrese un numero entero:")
N=int(input("N:"))
F,i=1,1
while i<=N:
    F*=i
    i+=1
print("El factorial es:",F)
