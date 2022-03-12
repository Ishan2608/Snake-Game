from turtle import Turtle
import random
import time

FONT = ("Arial", 54, "normal")
ALIGN = "center"

SUB_FONT = ('Arial', 12, 'normal')
COLOR_LIST = ['light blue', 'royal blue', 'light steel blue', 'steel blue',
              'light cyan', 'light sky blue', 'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink', 'medium sea green', 'khaki']


class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("dim gray")
        self.pensize(8)
        self.write(f"Snake Game", align=ALIGN, font=FONT)

    def show_creator_name(self, name):
        self.goto(0, -40)
        self.write(f"Created by {name}", align=ALIGN, font=("Arial", 18, 'italic'))

    def show_freeze_option(self):
        self.goto(0, -70)
        self.write(f"Press 'space' to pause or resume the game", align=ALIGN, font=SUB_FONT)

    def show_status(self, paused):
        self.goto(0, -120)
        self.clear()
        self.color(random.choice(COLOR_LIST))
        if paused:
            status = "Game is Paused"
            self.write(f"{status}", align=ALIGN, font=("Arial", 24, "italic"))
            time.sleep(0.5)



