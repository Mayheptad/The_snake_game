
from turtle import Turtle

SNAKE_MOVE_DISTANCE = 20

headings_map = {'up': 90, 'right': 0, 'down': 270, 'left': 180}


class Snake:
    def __init__(self):
        self.turtle_pos_cor = [(0, 0), (-20, 0), (-40, 0)]
        self.turtle_arr = []
        self.move_turtle_2_cor_arr()
        self.head = self.turtle_arr[0]

    def move_turtle_2_cor_arr(self):
        for pos in self.turtle_pos_cor:
            self.add_segment(pos)

    def add_segment(self, position):
        new_turtle_square = Turtle('square')
        new_turtle_square.color('white')
        new_turtle_square.penup()
        new_turtle_square.goto(position)
        self.turtle_arr.append(new_turtle_square)

    def increase_snake_length(self):
        x_axis = self.turtle_arr[-1].xcor()
        y_axis = self.turtle_arr[-1].ycor()
        self.turtle_pos_cor.append((x_axis, y_axis))
        self.add_segment(self.turtle_pos_cor[- 1])

    def reset_snake(self):
        for snk in self.turtle_arr:
            snk.goto(2000, 2000)
        self.turtle_arr.clear()
        self.move_turtle_2_cor_arr()
        self.head = self.turtle_arr[0]

    def up(self):
        if self.head.heading() != headings_map['down']:
            self.head.setheading(headings_map['up'])

    def right(self):
        if self.head.heading() != headings_map['left']:
            self.head.setheading(headings_map['right'])

    def down(self):
        if self.head.heading() != headings_map['up']:
            self.head.setheading(headings_map['down'])

    def left(self):
        if self.head.heading() != headings_map['right']:
            self.head.setheading(headings_map['left'])

    def move(self):
        for each_snake in range(len(self.turtle_arr) - 1, 0, -1):
            new_x = self.turtle_arr[each_snake - 1].xcor()
            new_y = self.turtle_arr[each_snake - 1].ycor()
            self.turtle_arr[each_snake].goto(new_x, new_y)
        self.turtle_arr[0].forward(SNAKE_MOVE_DISTANCE)