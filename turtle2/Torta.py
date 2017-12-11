# -*- coding: utf-8 -*-
#!/usr/bin/python3
from turtle import Screen, Turtle

# Calificaciones
suspenso = 10
aprobados = 20
notables = 40
sobresalientes = 30

# Radio del circulo
radio = 300
# Dimenciones de la ventana
ancho = 625
alto = 625

# Inicialización
pantalla = Screen()
pantalla.setup(ancho, alto)
pantalla.screensize(ancho - 25, alto - 25)

tortuga = Turtle()
tortuga.speed(0)  # maxima velocidad

# Dibujo del circulo
tortuga.penup()
tortuga.goto(0, -radio)
tortuga.pendown()
tortuga.circle(radio)
tortuga.penup()
tortuga.home()
tortuga.pendown()

# Dibujo de la linea para los suspensos
angulo = 360 * suspenso/100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

# Escribir el texto para los suspensos
tortuga.penup()
tortuga.right(angulo/2)
tortuga.forward(radio/2)
tortuga.write('Suspensos')
tortuga.backward(radio/2)
tortuga.left(angulo/2)
tortuga.pendown()

# Dibujo de la linea para los aprobados
angulo = 360 * aprobados/100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

# Escribe el texto aprobados
tortuga.penup()
tortuga.right(angulo/2)
tortuga.forward(radio/2)
tortuga.write("Aprobados")
tortuga.backward(radio/2)
tortuga.left(angulo/2)
tortuga.pendown()

# Dibuja linea para los notables
angulo = 360 * notables/100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

# Escribe el texto para los notables
tortuga.penup()
tortuga.right(angulo/2)
tortuga.forward(radio/2)
tortuga.write("Notables")
tortuga.backward(radio/2)
tortuga.left(angulo/2)
tortuga.pendown()

# Dibujo de la linea para los sobresalientes
angulo = 360 * sobresalientes / 100
tortuga.left(angulo)
tortuga.forward(radio)
tortuga.backward(radio)

# Escribir el texto para los sobresalientes
tortuga.penup()
tortuga.right(angulo / 2)
tortuga.forward(radio/2)
tortuga.write("Sobresalientes")
tortuga.backward(radio / 2)
tortuga.left(angulo / 2)
tortuga.pendown()

tortuga.hideturtle()

# Salir cuando se haga click
pantalla.exitonclick()