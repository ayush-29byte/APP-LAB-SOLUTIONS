#SPIRAL HELIX PATTERN
import turtle

loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
    turtle.circle(5 * i)
    turtle.circle(-5 * i)
    turtle.left(i)

turtle.exitonclick()

#CODE BY AYUSH SAXENA