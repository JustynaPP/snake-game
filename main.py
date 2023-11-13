from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
is_game_on = True

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.adding_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over_reset()
        snake.reset_snake()

    # detect collision with tail
    for segment in snake.snake_segm[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over_reset()
            snake.reset_snake()


screen.exitonclick()
