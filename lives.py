"""Lives class for managing player lives in the Breakout game."""

from turtle import Turtle

class Lives:
    """Handles the display, removal, and reset of player lives (represented as circles)."""

    def __init__(self, live):
        """
        Initialize the Lives object.

        Parameters:
        live (int): The number of lives to start with.
        """
        self.live = live
        self.lives = []  # List to hold the life indicator turtles

    def create_live(self):
        """Create and display life indicators on the screen."""
        for i in range(self.live):
            liv = Turtle(shape="circle")
            liv.color("white")
            liv.penup()
            liv.goto(-200 + (i * 30), 240)  # Position hearts spaced out at the top left
            self.lives.append(liv)

    def remove_live(self):
        """
        Remove one life (hide the last heart symbol).

        Returns:
        bool: True if a life was removed, False if no lives left.
        """
        if self.live > 0:
            self.lives[self.live - 1].hideturtle()
            self.live -= 1
            return True
        else:
            return False

    def reset_lives(self):
        """Reset lives back to full (used on game restart)."""
        for liv in self.lives:
            liv.hideturtle()
        self.lives.clear()
        self.live = 3
        self.create_live()
