from turtle import Turtle


class Scoreboard(Turtle):
    """Scoreboard class to display and manage game score"""

    def __init__(self, high_score=0):
        super().__init__()
        self.score = 0
        self.high_score = high_score
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display"""
        self.clear()
        score_text = f"Score: {self.score}  High Score: {self.high_score}"
        self.write(score_text, font=("Courier", 16, "normal"))

    def update_point(self, points):
        """Add points to the current score"""
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()

    def reset_score(self):
        """Reset current score to 0"""
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        """Display game over message"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))