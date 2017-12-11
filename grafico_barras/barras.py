# -*- coding: utf-8 -*-
#!/usr/bin/python3
from turtle import Turtle, Screen

def dibuja_barra(tortuga, porcentaje, titulo, anchura):
    # Dibuja barra
    tortuga.penup()
    tortuga.setheading(-90)
    tortuga.forward(5)
    tortuga.write(titulo)
    tortuga.backward(5)
    tortuga.pendown()

    tortuga.setheading(90)
    tortuga.forward(porcentaje)
    tortuga.write("%.2f"%porcentaje+"%")
    tortuga.setheading(0)
    tortuga.forward(anchura)
    tortuga.setheading(-90)
    tortuga.forward(porcentaje)
    tortuga.setheading(-180)
    tortuga.forward(anchura)



def reubica_tortuga(tortuga, distancia, anchura):
    tortuga.penup()
    tortuga.setheading(0)
    tortuga.forward(distancia + anchura)
    tortuga.pendown()

def main():
    # Dimensiones ventana
    ancho = 625
    alto = 625

    # Lectura de datos
    num_aprobados = int(input("Aprobados: "))
    num_suspensos = int(input("Suspensos: "))
    num_notables = int(input("Notables: "))
    num_sobresalientes = int(input("Sobresalientes: "))

    # Convirtiendo a porcentajes
    total = num_aprobados + num_notables + num_sobresalientes + num_suspensos
    aprobados = (num_aprobados * 100) / total
    suspensos = (num_suspensos * 100) / total
    notables = (num_notables * 100) / total
    sobresalientes = (num_sobresalientes * 100) / total

    # Inicializacion
    pantalla = Screen()
    pantalla.setup(ancho, alto)
    pantalla.screensize(ancho - 25, alto - 25)
    pantalla.setworldcoordinates(0, 0, 100, 100)

    tortuga = Turtle()
    tortuga.speed(0)
    tortuga.penup()
    tortuga.setheading(90)
    tortuga.forward(10)
    tortuga.setheading(0)
    tortuga.pendown()

    # Dibujando barras
    dibuja_barra(tortuga, aprobados, "aprobados", 10)
    reubica_tortuga(tortuga, 2, 10)

    dibuja_barra(tortuga, suspensos, "suspensos", 10)
    reubica_tortuga(tortuga, 2, 10)

    dibuja_barra(tortuga, notables, "notables", 10)
    reubica_tortuga(tortuga, 2, 10)

    dibuja_barra(tortuga, sobresalientes, "sobresalientes", 10)

    tortuga.hideturtle()
    pantalla.exitonclick()
main()
