from turtle import Screen, Turtle

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)

lado = int(input("Ingrese el tamanio: "))

tortuga = Turtle()

# Dibuja triangulo equilatero
tortuga.forward(lado)
tortuga.left(120)
tortuga.forward(lado)
tortuga.left(120)
tortuga.forward(lado)

pantalla.exitonclick()