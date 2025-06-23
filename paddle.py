from turtle import Turtle


class Paddle(Turtle):
    """Paddle class for the Breakout game"""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)  # Make paddle wider
        self.penup()
        self.speed(0)
        self.goto(position)
        self.initial_position = position

        # Screen boundaries (adjusted for paddle width)
        self.left_boundary = -240 + 50  # Screen edge + half paddle width
        self.right_boundary = 240 - 50

        # Movement speed
        self.move_distance = 20

    def go_left(self):
        """Move paddle left within screen boundaries"""
        new_x = self.xcor() - self.move_distance
        if new_x >= self.left_boundary:
            self.setx(new_x)

    def go_right(self):
        """Move paddle right within screen boundaries"""
        new_x = self.xcor() + self.move_distance
        if new_x <= self.right_boundary:
            self.setx(new_x)

    def reset_position(self):
        """Reset paddle to initial position"""
        self.goto(self.initial_position)