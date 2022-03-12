# import the in-built modules
from turtle import Screen
import time

# import all our classes(segments our program is divided into)
from food import Food
from snake_body import Snake
from scoreboard import Scoreboard
from display import Display

# create screen object to get a screen
screen = Screen()
# y-axis from -300 to 300 and x-axis is als from -300 to 300
screen.setup(width=600, height=600)
# this will set title of the window in which we see our game
screen.title("Snake Game in Python")
screen.bgcolor("black")
# turning off the animation. 0 stands for OFF
# thus if you move the turtle, it won't show on screen even tho it is happening
screen.tracer(0)
# later to see it happen, we use screen.update()
# our program will work well even without tracer and update method, but it looks a little funny, try it out


# create the objects from classes
# objects defined later will overlap objects defined earlier than them
# thus we define food at last and display object first
# display text - Snake Game, Creator Name, and additional instructions
display = Display()
display.show_creator_name("Ishan Rastogi")
display.show_freeze_option()

display2 = Display()
# Show all-time high score and current score
scoreboard = Scoreboard()
# create our snake object
snake = Snake()
# create food object
food = Food()


# variable that will run our loop, in which the snake keeps moving forward
game_is_on = True
is_game_paused = False


def pause_game():
    global is_game_paused

    # check if game is paused, then continue it
    if is_game_paused:
        is_game_paused = False

    # check if game is on, pause it
    elif not is_game_paused:
        is_game_paused = True


# make our screen be able to listen to key presses
screen.listen()
# define keys and the functions they should execute
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left_turn)
screen.onkey(key="Right", fun=snake.right_turn)
screen.onkey(key="space", fun=pause_game)

while game_is_on:

    if not is_game_paused:
        # display status whether the game is paused or not, here it is not paused, game is on.
        display2.show_status(is_game_paused)
        # this is where we turn the animation on again.
        screen.update()
        # for a slower speed, increase the value in sleep function.
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            if scoreboard.score > scoreboard.high_score:
                scoreboard.high_score = scoreboard.score
                scoreboard.update_score()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.reset_game()
            snake.reset_snake()

        # Detect collision with tail
        # for segment in snake.segments:
        #     if segment == snake.head:
        #         pass
        #     elif snake.head.distance(segment) < 10:
        #         game_is_on = False
        #         scoreboard.game_over()

        # OR we can use String slicing
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset_game()
                snake.reset_snake()

    else:
        # display status whether the game is paused or not, here it is paused
        display2.show_status(is_game_paused)


# screen should close only if we click on it or click on close button,
screen.exitonclick()
# If we don't use this function, the screen closes automatically as soon as our program ends.
