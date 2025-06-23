from turtle import Turtle
import random

colors = {
        "#ff6b6b": 50,  # Red - highest score
        "#4ecdc4": 40,  # Teal
        "#45b7d1": 30,  # Blue
        "#96ceb4": 20,  # Green
        "#ffeaa7": 15,  # Yellow
        "#fd79a8": 10  # Pink - lowest score
    }

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2.5)  # Each block is ~50px wide
        color = self.random_color()
        self.color(color)
        self.value =60-colors[color]

    def random_color(self):
        color_names = list(colors.keys())
        weights = list(colors.values())
        return random.choices(color_names, weights=weights, k=1)[0]


class Blocks:
    def __init__(self):
        self.rows = 5
        self.columns = 7
        self.segments = []

    def create_blocks(self):
        block_width = 50  # Approximate block width
        block_height = 20  # Approximate block height
        spacing_x = 10     # Minimal horizontal space between blocks
        spacing_y = 10      # Minimal vertical space between rows

        total_width = self.columns * block_width + (self.columns - 1) * spacing_x
        total_height = self.rows * block_height + (self.rows - 1) * spacing_y

        start_x = -total_width / 2 + block_width / 2
        start_y = 200  # Top of the screen

        for row in range(self.rows):
            for col in range(self.columns):
                block = Block()
                x_pos = start_x + col * (block_width + spacing_x)
                y_pos = start_y - row * (block_height + spacing_y)
                block.goto(x_pos, y_pos)
                self.segments.append(block)

    def reset_blocks(self):
        for block in self.segments:
            block.hideturtle()
        self.segments.clear()
        self.create_blocks()

