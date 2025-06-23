"""Ball class for the Breakout game"""

from turtle import Turtle

class Ball(Turtle):
    """Manages the ball's movement, bouncing, and resetting behavior."""

    def __init__(self):
        """Initialize the ball with shape, color, movement variables."""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5   # Horizontal speed
        self.y_move = 5   # Vertical speed
        self.move_speed = 0.05  # Initial delay between frames (fast)

    def move(self):
        """Update the ball's position based on current direction."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Invert vertical direction (used for top wall and paddle collisions)."""
        self.y_move *= -1

    def bounce_x(self):
        """Invert horizontal direction and slightly increase speed."""
        self.x_move *= -1
        self.move_speed *= 0.9  # Makes the game progressively harder

    def reset_position(self):
        """Reset the ball to the starting position and bounce downward."""
        self.goto(0, -250)
        self.move_speed = 0.05  # Reset speed
        self.bounce_y()         # Send ball downward again

    def reset_speed(self):
        """Reset the movement speed to initial value."""
        self.move_speed = 0.05
