from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('purple')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        

    def move(self):
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        self.goto(newx,newy)
        

    def ybounce(self):
        self.y_move *= -1

    def xbounce(self):
        self.x_move *= -1