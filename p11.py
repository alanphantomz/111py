#Dado dos numeros A y B realizar la division entera por restas sucesivas
#desplegar los numeros, el cociente y elresiduo
dividendo=int(input("dividendo:"))
divisor=int(input("divisor:"))
contador=0

while dividendo >= divisor:
    dividendo-=divisor
    contador+=1

print("El cociente es:",contador)
print("El residuo es:",dividendo)
    
