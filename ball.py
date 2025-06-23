from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5  # Increased from 3
        self.y_move = 5  # Increased from 3
        self.move_speed = 0.05  # Much faster

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  # Optional: ball speeds up slightly each bounce

    def reset_position(self):
        self.goto(0, -250)
        self.move_speed = 0.05  # Reset speed to fast
        self.bounce_y()

    def reset_speed(self):
        self.move_speed = 0.05

