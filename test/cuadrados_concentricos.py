from turtle import Turtle, Screen

def dibujaCuadradosConcentricos(tortuga):
    tortuga.pencolor("green")
    # Cuadrado 200 x 200
    tortuga.forward(200)
    tortuga.left(90)
    tortuga.forward(200)
    tortuga.left(90)
    tortuga.forward(200)
    tortuga.left(90)
    tortuga.forward(200)

    tortuga.penup()
    tortuga.left(90)
    tortuga.forward(50)
    tortuga.left(90)
    tortuga.forward(50)
    tortuga.right(90)
    tortuga.pendown()

    # Cuadrado concentrico: 100 x 100
    tortuga.forward(100)
    tortuga.left(90)
    tortuga.forward(100)
    tortuga.left(90)
    tortuga.forward(100)
    tortuga.left(90)
    tortuga.forward(100)

def trianguloEquilatero(tortuga, lado):
    tortuga.pencolor("orange")
    tortuga.pensize(1)
    # Dibuja triangulo equilatero
    tortuga.forward(lado)
    tortuga.left(120)
    tortuga.pensize(2)
    tortuga.forward(lado)
    tortuga.left(120)
    tortuga.pensize(3)
    tortuga.forward(lado)

def posicionamientoAbsoluto(tortuga):
    tortuga.goto(0, 0)
    tortuga.forward(100)
    tortuga.right(90)
    tortuga.pencolor("blue")
    tortuga.forward(150)

    tortuga.home()
    tortuga.forward(250)
    tortuga.backward(500)
    tortuga.penup()
    tortuga.forward(250)
    tortuga.left(90)
    tortuga.pendown()
    tortuga.forward(250)
    tortuga.left(180)
    tortuga.forward(500)

    tortuga.home()
    tortuga.pensize(1)
    tortuga.setheading(45) # angulos 45 con respecto a la abscisa
    tortuga.forward(100)

def trianguloEquiSinLeftRight():
    mi_tortuga = Turtle()
    mi_tortuga.hideturtle()
    mi_tortuga.pensize(10)
    mi_tortuga.pencolor("blue")
    mi_tortuga.home()
    mi_tortuga.setheading(60)

    # lados = 150
    mi_tortuga.forward(150)

    mi_tortuga.home()
    mi_tortuga.setheading(0)
    mi_tortuga.forward(150)

    mi_tortuga.goto(150, 0)
    mi_tortuga.setheading(120)
    mi_tortuga.forward(150)

def trianguloEquiSinLeftRightSeg():
    mi_tortuga = Turtle()
    mi_tortuga.hideturtle()
    mi_tortuga.pensize(10)
    mi_tortuga.pencolor("blue")
    mi_tortuga.home()
    mi_tortuga.setheading(60)

    # lados = 150
    mi_tortuga.forward(150)

    mi_tortuga.setheading(mi_tortuga.towards(150, 0))
    mi_tortuga.forward(150)

    mi_tortuga.setheading(mi_tortuga.towards(0, 0))
    mi_tortuga.forward(150)

def cuadradosConcentricosSinLeftRight():
    mi_tortuga = Turtle()
    mi_tortuga.hideturtle()
    mi_tortuga.pencolor("red")

    # Cuadrado exterior
    mi_tortuga.forward(200)
    mi_tortuga.setheading(mi_tortuga.towards(200, 200))
    mi_tortuga.forward(200)
    mi_tortuga.setheading(mi_tortuga.towards(0, 200))
    mi_tortuga.forward(200)
    mi_tortuga.setheading(mi_tortuga.towards(0, 0))
    mi_tortuga.forward(200)

    mi_tortuga.pencolor("blue")

    # ubicando a la tortuga
    mi_tortuga.penup()
    mi_tortuga.setheading(0)
    mi_tortuga.forward(50)
    mi_tortuga.setheading(mi_tortuga.towards(50, 50))
    mi_tortuga.forward(50)
    mi_tortuga.pendown()

    # Cuadrado inferior
    mi_tortuga.forward(100)
    mi_tortuga.setheading(mi_tortuga.towards(150, 150))
    mi_tortuga.forward(100)
    mi_tortuga.setheading(mi_tortuga.towards(150, 50))
    mi_tortuga.forward(100)
    mi_tortuga.setheading(mi_tortuga.towards(50, 50))
    mi_tortuga.forward(100)


def main():
    pantalla = Screen()
    ancho, alto = 425, 500
    pantalla.setup(ancho, alto)
    pantalla.screensize(ancho - 25, alto - 25)

    # tortuga = Turtle()
    # dibujaCuadradosConcentricos(tortuga)
    #
    # # Opcional prueba
    # lado = int(input("Ingrese lado: "))
    # trianguloEquilatero(tortuga, lado)
    #
    # # Posicionamiento absoluto
    # posicionamientoAbsoluto(tortuga)
    #
    # trianguloEquiSinLeftRightSeg()
    cuadradosConcentricosSinLeftRight()
    pantalla.exitonclick()
main()