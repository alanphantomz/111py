# -*- coding: utf-8 -*-
#!/usr/bin/python3
from turtle import Screen, Turtle

def dibuja_pedazo(radio, porcentaje, tortuga, titulo):
    # Dibujo de la linea
    angulo = 360 * porcentaje / 100
    tortuga.left(angulo)
    tortuga.forward(radio)
    tortuga.backward(radio)

    # Escribir el texto
    tortuga.penup()
    tortuga.right(angulo / 2)
    tortuga.forward(radio / 2)
    tortuga.write(titulo)
    tortuga.backward(radio / 2)
    tortuga.left(angulo / 2)
    tortuga.pendown()

def dibuja_circulo(radio, tortuga):
    tortuga.penup()
    tortuga.goto(0, -radio)
    tortuga.pendown()
    tortuga.circle(radio)
    tortuga.penup()
    tortuga.home()
    tortuga.pendown()

def main():
    # Titulos
    titSobre = "Sobresalientes"
    titApro = "Aprobados"
    titNotab = "Notables"
    titSuspen = "Suspensos"

    # Radio del circulo
    radio = 300

    # Dimenciones de la ventana
    ancho = 625
    alto = 625

    # Lectura de datos
    suspensos = float(input("Cant. Suspensos: "))
    aprobados = float(input("Cant. Aprobados: "))
    notables = float(input("Cant. Notables: "))
    sobresalientes = float(input("Cant. Sobresalientes: "))

    # Convertimos a porcentajes los datos recibidos
    total_estudiantes = suspensos + aprobados + notables + sobresalientes
    suspensos = (suspensos * 100) / total_estudiantes
    aprobados = (aprobados * 100) / total_estudiantes
    notables = (notables * 100) / total_estudiantes
    sobresalientes = (sobresalientes * 100) / total_estudiantes

    # Inicialización
    pantalla = Screen()
    pantalla.setup(ancho, alto)
    pantalla.screensize(ancho - 25, alto - 25)

    tortuga = Turtle()
    tortuga.speed(0)  # maxima velocidad
    dibuja_circulo(radio, tortuga)

    # Se dibuja la torta
    dibuja_pedazo(radio, suspensos, tortuga, titSuspen)
    dibuja_pedazo(radio, aprobados, tortuga, titApro)
    dibuja_pedazo(radio, notables, tortuga, titNotab)
    dibuja_pedazo(radio, sobresalientes, tortuga, titSobre)

    tortuga.hideturtle()

    # Salir cuando se haga click
    pantalla.exitonclick()

main()
