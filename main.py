from turtle import Turtle, Screen
from paddle import  Paddle


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game!")
screen.listen()
screen.tracer(0)

paddle = Paddle()

gameIsOn = True
screen.onkey(paddle.moveUp, "Up")
screen.onkey(paddle.moveDown, "Down")

while gameIsOn:
    screen.update()


screen.exitonclick()