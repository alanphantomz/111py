#Dado un numero A determinar si es par o impar,
#mediante restas sucesivas desplegar el num y el sms
print("Ingrese un numero entero:")
A=int(input("A:"))
num=A
while A>=2:A-=2
if(A==0):print("El numero",num,"es par")
else:print("El numero",num,"es inpar")
    
    
