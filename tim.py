from turtle import Turtle


class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(0, -330)
        self.shape("turtle")
        self.color("white")

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)

    def move_left(self):
        self.goto(self.xcor() - 20, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + 20, self.ycor())

    def new_level(self):
        self.goto(0, -330)