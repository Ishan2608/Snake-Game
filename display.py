from turtle import Turtle

FONT = ("Arial", 50, "normal")
ALIGN = "center"

SUB_FONT = ('Arial', 12, 'normal')


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
        self.write(f"Press 'f' to freeze the program, if you want to take screen shot", align=ALIGN, font=SUB_FONT)
