from turtle import Screen, Turtle
from math import sqrt

pantalla = Screen()
pantalla.setup(1025, 1025)
pantalla.screensize(1000, 1000)
pantalla.setworldcoordinates(-500, -500, 500, 500)
pantalla.delay(0)

x1 = -200
y1 = -200

velocidad_x1 = 0.1
velocidad_y1 = 0
m1 = 20

x2 = 200
y2 = 200
velocidad_x2 = -0.1
velocidad_y2 = 0
m2 = 20

cuerpo1 = Turtle("circle")
cuerpo1.color("red")
cuerpo1.speed(0)
cuerpo1.penup()
cuerpo1.goto(x1, y1)
cuerpo1.pendown()

cuerpo2 = Turtle("circle")
cuerpo2.color("blue")
cuerpo2.speed(0)
cuerpo2.penup()
cuerpo2.goto(x2, y2)
cuerpo2.pendown()
for t in range(100000):
    r = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    aceleracion_x1 = m2 * (x2 - x1) / r**3
    aceleracion_y1 = m2 * (y2 - y1) / r ** 3
    aceleracion_x2 = m1 * (x1 - x2) / r ** 3
    aceleracion_y2 = m1 * (y1 - y2) / r ** 3

    velocidad_x1 += aceleracion_x1
    velocidad_y1 += aceleracion_y1
    velocidad_x2 += aceleracion_x2
    velocidad_y2 += aceleracion_y2

    x1 += velocidad_x1
    y1 += velocidad_y1
    x2 += velocidad_x2
    y2 += velocidad_y2

    cuerpo1.goto(x1, y1)
    cuerpo2.goto(x2, y2)
pantalla.exitonclick()