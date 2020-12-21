from turtle import Turtle, Screen
from paddle import  Paddle


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game!")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

gameIsOn = True
screen.onkey(r_paddle.moveUp, "Up")
screen.onkey(r_paddle.moveDown, "Down")

screen.onkey(l_paddle.moveUp, "w")
screen.onkey(l_paddle.moveDown, "s")

while gameIsOn:
    screen.update()


screen.exitonclick()