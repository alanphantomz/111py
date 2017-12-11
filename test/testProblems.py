## GRAFICOS DE TORTUGA
from turtle import Screen, Turtle  # para crear una tortuga y una pantalla

# creamos una pantall
pantalla = Screen()

# ancho y alto de la ventana en pixeles
pantalla.setup(425, 225)

# ancho y alto de la superficie de dibujo
# es mas pequeño que la ventana x que esta
#requiere algunos elementos adicionales, decorativos.
pantalla.screensize(400, 200)

# Creación de la tortuga
tortuga = Turtle()

# avanza 100 pasos en la dirección en la q apunta
# por defecto es a la derecha, (forward = adelante)
tortuga.forward(100)

# evita a q la ventana termine inmediatamente
#forzando a clickar en la ventana.
pantalla.exitonclick()

