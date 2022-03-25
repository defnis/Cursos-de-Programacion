import turtle
import random

s = turtle.Screen()
s.title("Primer Proyecto")
s.bgcolor("grey")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("green", "green") 
#Primero el color del lienzo y luego de la tortuga.
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue", "blue")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

jugador1.penup() #Con esto no dibuja.
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-200, 250)
jugador1.showturtle()

jugador2.penup() #Con esto no dibuja.
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-250,-170)
jugador2.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if jugador1.pos() >= (200,200):
        print("La tortuga verde ha ganado")
    elif jugador2.pos() >= (200,200):
        print("La tortuga azul ha ganado")
        break
    else:
        turno1 = input("Precione la tecla enter para continuar")
        turno1 = random.choice(dado)
        print("Tu numero es: ",turno1, "\nAvanzas: ", turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 = input("Precione la tecla enter para continuar")
        turno2 = random.choice(dado)
        print("Tu numero es: ",turno2, "\nAvanzas: ", turno2*20)
        jugador2.pendown() #Ponemos el lapiz a pintar y luego corre. 
        jugador2.forward(20*turno2)



turtle.done()