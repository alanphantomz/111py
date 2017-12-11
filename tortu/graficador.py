from turtle import Screen, Turtle
from math import sin, pi, cos

pantalla = Screen()
pantalla.title("seno y coseno!!")
pantalla.setup(1025, 200)
pantalla.screensize(1000, 175)

# param(x1, y1, x2, y2)
pantalla.setworldcoordinates(-2*pi, -1, 2*pi, 1)
pantalla.delay(0)  # Tiempo que transcurre entre 2 fotogramas 

# rayamos la cancha
tortu = Turtle()
tortu.pencolor("blue")
tortu.hideturtle()
tortu.penup()
tortu.goto(-2*pi, 0)
tortu.pendown()
tortu.goto(2*pi, 0)
tortu.penup()
tortu.goto(0, -1)
tortu.pendown()
tortu.goto(0, 1)

# dibujamos la curva
tortuga = Turtle()
tortuga.pencolor("green")
tortuga.speed(0)
tortuga.hideturtle()

tortuga2 = Turtle()
tortuga2.pencolor("orange")
tortuga2.speed(0)
tortuga2.hideturtle()


# lectura de datos
x1 = float(input("Limite inferior del intervalo: "))
x2 = float(input("Limite superior del intervalo: "))
puntos = int(input("Cuantos puntos mostrar: "))

# x = -2 * pi
# dx =  4 * pi / 200 # Exactamente 200 puntos
x = x1
dx = (x2 -  x1) / puntos

tortuga.penup()
tortuga.goto(x, sin(x))
tortuga.pendown()

tortuga2.penup()
tortuga2.goto(x, cos(x))
tortuga2.pendown()

while x <= x2:
    tortuga2.goto(x, cos(x))
    tortuga.goto(x, sin(x))
    x += dx

pantalla.exitonclick()

