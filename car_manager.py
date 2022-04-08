from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE


    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.setposition(300, random.randint(-250, 250))
        new_car.setheading(180)
        new_car.turtlesize(stretch_len=2, stretch_wid=1)
        self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def speed_up_car(self):
        self.move_distance += MOVE_INCREMENT

