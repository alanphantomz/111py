#Dado los valores a,b,c que son los coeficientes de la ecuacion
#de segundo grado, hallar sus raices reales, desplegar los resultados
#x=(-b+-sqrt(b*b-4*a*c))/(2*a)
import math
print("Ingrese a,b,c respectivamente:")
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
#validacion de los datos ingresados
discriminante=b**2-4*a*c
if(discriminante>0):
    x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    print("X1=",x1)
    print("X2=",x2)    
elif discriminante==0:
    x1=x2=-b/(2*a)
    print("X1=",x1)
    print("X2=",x2)
else:
    print("No existen raices reales!!!")


