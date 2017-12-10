#En la expresion A+X=B, dados los valores de A y B
#hallar el valor de X sin realizar la operacion de resta X=B-A
#(suponiendo que X > 0 y A <= B)
print("Ingrese A y B; A menor o igual q B por favor")
A=int(input("A:"))
B=int(input("B:"))
x=0
while (A+x)!=B:x+=1
print("El valor de x es:",x)
    
