from turtle import Turtle, Screen
from paddle import  Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game!")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball =  Ball()

gameIsOn = True
screen.onkey(r_paddle.moveUp, "Up")
screen.onkey(r_paddle.moveDown, "Down")

screen.onkey(l_paddle.moveUp, "w")
screen.onkey(l_paddle.moveDown, "s")

while gameIsOn:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:   # if ball touches the edge
        ball.ybounce()  
    
    if ball.xcor() > 370 or ball.xcor() < -370:   # if ball touches the edge
        ball.xbounce()  

screen.exitonclick()