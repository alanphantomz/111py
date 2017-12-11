from turtle import Screen, Turtle

pantalla = Screen()
# tam ventana
pantalla.setup(425, 225)
# area de dibujo
pantalla.screensize(400, 200)

tortuga = Turtle()
tortuga.forward(100)
tortuga.left(90)  # 90 grados izquierda
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

pantalla.exitonclick()