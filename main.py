
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

Screen().setup(width=600, height=600)
Screen().title('My Snake Game')
Screen().bgcolor('black')
Screen().tracer(0)
Screen().listen()

scb = Scoreboard()
snk = Snake()
food = Food()

Screen().onkey(fun=snk.up, key='Up')
Screen().onkey(fun=snk.right, key='Right')
Screen().onkey(fun=snk.down, key='Down')
Screen().onkey(fun=snk.left, key='Left')


def stop_game():
    global is_game_on
    is_game_on = False
    scb.game_over()


is_game_on = True

while is_game_on:
    Screen().update()
    time.sleep(0.3)
    snk.move()

    if snk.head.distance(food) < 15:
        food.move_food()
        snk.increase_snake_length()
        scb.increment_scores()

    if snk.head.xcor() > 280 or snk.head.xcor() < -300 or snk.head.ycor() > 280 or snk.head.ycor() < -280:
        stop_game()

    for snake in snk.turtle_arr[1:]:
        if snk.head.distance(snake) < 10:
            stop_game()


Screen().exitonclick()
