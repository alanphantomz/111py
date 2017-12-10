#COMENZANDO CON FUNCIONES MATEMATICAS 
#Dado los lados de A,B,C de un triangulo cualesquiera, hallar
#y desplegar su area
#area=sqrt(s(s-a)(s-b)(s-c)) y s=(a+b+c)/2

import math
print("Ingrese a,b,c respectivamente:")
a=float(input())
b=float(input())
c=float(input())
s=(a+b+c)/2
parametro=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(parametro)
print("parametro de sqrt:",parametro)
print("S=",s)
print("El area es:",area)
