from turtle import Turtle, Screen

pantalla = Screen()
# tamaño de ventana
pantalla.setup(425, 225)
# superficie de dibujo
pantalla.screensize(400, 200)

tortuga = Turtle()

# Primer cuadrado
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

# Tortuga levanta el lapiz
tortuga.penup()

tortuga.right(90)
tortuga.forward(100)

# Tortuga apoya el lapiz
tortuga.pendown()

# Segundo cuadrado
tortuga.forward(100)

tortuga.left(90)
tortuga.forward(100)

tortuga.left(90)
tortuga.forward(100)

tortuga.left(90)
tortuga.forward(100)

pantalla.exitonclick()