import time
from turtle import Screen
from tim import Tim
from car import Car
from  score_board import ScoreBoard

my_screen = Screen()
my_screen.setup(height=700, width=1000)
my_screen.bgcolor("black")
my_screen.title("Turtle Crossing")
my_screen.listen()

scoreboard = ScoreBoard()
johnny = Tim()
cars = Car()
my_screen.tracer(0)

my_screen.onkey(key="Up", fun=johnny.move_up)
my_screen.onkey(key="Down", fun=johnny.move_down)
my_screen.onkey(key="Left", fun=johnny.move_left)
my_screen.onkey(key="Right", fun=johnny.move_right)

car_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    my_screen.update()

    cars.create_car()
    cars.move()

    # Collision with car
    for moving_cars in cars.cars:
        if johnny.distance(moving_cars) < 20:
            scoreboard.game_over()
            game_is_on = False

    if johnny.ycor() > 330:
        scoreboard.update_score()
        johnny.new_level()
        car_speed -= 0.01


my_screen.exitonclick()
