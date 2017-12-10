#Dado un numero X determinar si es un numero primo,
#desplegar el numero y el mensaje
print("Ingrese un numero entero:")
x=int(input(">"))
contador=1
for i in range(2,x+1):
    if(x%i==0):
        contador+=1
if contador==2:print("El numero",x,"es primo")
else:print("El numero",x,"no es primo")
