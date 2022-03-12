from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_STEP = 20
SNAKE_COLOR = 'light green'
SNAKE_SHAPE = 'square'
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape=SNAKE_SHAPE)
        new_turtle.color(SNAKE_COLOR)
        new_turtle.penup()
        new_turtle.goto(position)
        if position[0] == 0 and position[1] == 0:
            new_turtle.color("green")
        self.segments.append(new_turtle)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # make a member of list go to the position of previous member's position till we reach head(index 0)
        # only index 0 will move forward, others follow just be taking position of previous member's place.
        for cell_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[cell_num - 1].xcor()
            new_y = self.segments[cell_num - 1].ycor()
            self.segments[cell_num].goto(new_x, new_y)
        # make head move once.
        self.head.forward(MOVE_STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left_turn(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right_turn(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

