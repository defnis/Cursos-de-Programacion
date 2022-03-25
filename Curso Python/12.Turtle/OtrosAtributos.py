import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.shape("turtle") #Invicar a la tortuga.  
t.begin_fill()
t.circle(100)
t.end_fill()

t.begin_fill()
t.color("white", "white")
t.circle(50)
t.end_fill()

turtle.done()