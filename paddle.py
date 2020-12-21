from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddles = []
        self.paddle = Turtle(shape="square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(350,0)

    def moveUp(self):
        newx = self.paddle.xcor()
        newy = self.paddle.ycor() + 20
        self.paddle.setposition(newx, newy) 

    def moveDown(self):
        newx = self.paddle.xcor()
        newy = self.paddle.ycor() - 20
        self.paddle.setposition(newx, newy) 