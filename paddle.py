from turtle import Turtle


class Paddle:
    def __init__(self, xcoord, ycoord):
        self.paddles = []
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.createPaddle();
       
    def createPaddle(self):
        self.paddle = Turtle(shape="square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(self.xcoord,self.ycoord)

    def moveUp(self):
        newy = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), newy) 

    def moveDown(self):
        newy = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), newy) 