import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
scoreboard = Scoreboard()
car_manager = CarManager()
counter_loop = 0
counter_cars = 0
screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if counter_loop == 6:
        car_manager.create_car()
        counter_loop = 0
    car_manager.move_car()
    counter_loop += 1

    # Check if turtle has reached the goal
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.add_point()
        car_manager.speed_up_car()

    # check if the turtle hit a car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.lost_game()






screen.exitonclick()
