from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segm = []
        self.create_snake()
        self.head = self.snake_segm[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.up()
        self.snake_segm.append(snake)
        snake.setpos(position)

    def extend(self):
        self.add_segment(self.snake_segm[-1].position())  # position of the last segment in the list

    def move(self, ):
        for seg_num in range(len(self.snake_segm) - 1, 0, -1):
            previous = self.snake_segm[seg_num - 1]
            self.snake_segm[seg_num].goto(previous.pos())
        self.head.fd(MOVE_SPEED)


    def up(self):
        if self.head.heading() != DOWN:
            self.snake_segm[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
