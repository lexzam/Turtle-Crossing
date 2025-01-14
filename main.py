import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
player = Player()
cars = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    # Detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect when the turtle reaches the other side
    if player.reset_position():
        player.go_to_start()
        cars.level_up()
        score_board.increase_level()

screen.exitonclick()
