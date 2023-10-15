import random
from turtle import Turtle


class Car():
    def __init__(self):
        self.cars = []

    def create_car(self):
        number = random.randint(1, 6)
        if number == 1:
            car_turtle = Turtle()
            car_turtle.penup()
            car_turtle.shape("square")
            car_turtle.color("white")
            car_turtle.shapesize(stretch_len=random.randint(1, 3), stretch_wid=1)
            car_turtle.goto(460, random.randint(-310, 331))
            self.cars.append(car_turtle)

    def move(self):
        for all_cars in self.cars:
            all_cars.goto(all_cars.xcor() - 5, all_cars.ycor())
