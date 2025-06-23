"""Block and Blocks classes for the Breakout game."""

from turtle import Turtle
import random

# Color map with scores (higher score = rarer color)
colors = {
    "#ff6b6b": 50,   # Red - highest score
    "#4ecdc4": 40,   # Teal
    "#45b7d1": 30,   # Blue
    "#96ceb4": 20,   # Green
    "#ffeaa7": 15,   # Yellow
    "#fd79a8": 10    # Pink - lowest score
}


class Block(Turtle):
    """Represents a single block in the breakout wall."""

    def __init__(self):
        """Initialize the block with color, size, and point value."""
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2.5)  # Block is ~50px wide
        color = self.random_color()
        self.color(color)
        self.value = 60 - colors[color]  # Higher weight = lower score

    def random_color(self):
        """Choose a random color based on weighted probabilities."""
        color_names = list(colors.keys())
        weights = list(colors.values())
        return random.choices(color_names, weights=weights, k=1)[0]


class Blocks:
    """Manages the grid of all block objects in the game."""

    def __init__(self):
        """Initialize block grid size and container."""
        self.rows = 5
        self.columns = 7
        self.segments = []  # List to store all block instances

    def create_blocks(self):
        """Create a full grid of block instances and place them on screen."""
        block_width = 50    # Approximate block width
        block_height = 20   # Approximate block height
        spacing_x = 10      # Horizontal space between blocks
        spacing_y = 10      # Vertical space between rows

        total_width = self.columns * block_width + (self.columns - 1) * spacing_x
        total_height = self.rows * block_height + (self.rows - 1) * spacing_y

        start_x = -total_width / 2 + block_width / 2
        start_y = 200  # Starting Y position from top

        for row in range(self.rows):
            for col in range(self.columns):
                block = Block()
                x_pos = start_x + col * (block_width + spacing_x)
                y_pos = start_y - row * (block_height + spacing_y)
                block.goto(x_pos, y_pos)
                self.segments.append(block)

    def reset_blocks(self):
        """Clear existing blocks and recreate the block grid."""
        for block in self.segments:
            block.hideturtle()
        self.segments.clear()
        self.create_blocks()
