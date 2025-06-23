# Breakout Game - Python Turtle Graphics Implementation
# Author: Your Name
# A classic arcade-style breakout game with paddle, ball, and destructible blocks

from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard
from lives import Lives
import time
import os

# Game Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
PADDLE_Y = -280
BALL_RESET_Y = -250
TOP_WALL = 280
SIDE_WALL = 240
PADDLE_BOUNCE_Y = -260
MISS_Y = -280
PADDLE_BOUNCE_DISTANCE = 40
BLOCK_HIT_DISTANCE = 30
HIGH_SCORE_FILE = "highscore.txt"


def load_high_score():
    """Load high score from file, return 0 if file doesn't exist"""
    try:
        if os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, 'r') as file:
                return int(file.read().strip())
    except (ValueError, IOError):
        pass
    return 0


def save_high_score(score):
    """Save high score to file"""
    try:
        with open(HIGH_SCORE_FILE, 'w') as file:
            file.write(str(score))
    except IOError:
        print("Could not save high score")


class GameController:
    """Handles game input and state management"""

    def __init__(self):
        self.move_left = False
        self.move_right = False
        self.ball_started = False
        self.game_paused = False

    def press_left(self):
        self.move_left = True

    def release_left(self):
        self.move_left = False

    def press_right(self):
        self.move_right = True

    def release_right(self):
        self.move_right = False

    def start_ball(self):
        self.ball_started = True

    def toggle_pause(self):
        self.game_paused = not self.game_paused


def setup_screen():
    """Initialize and configure the game screen"""
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.title("Breakout Game")
    screen.tracer(0)
    # Prevent window resizing/maximizing
    screen.cv._rootwindow.resizable(False, False)
    return screen


def setup_game_objects():
    """Create and initialize all game objects"""
    paddle = Paddle((0, PADDLE_Y))
    ball = Ball()
    blocks = Blocks()
    scoreboard = Scoreboard(load_high_score())
    lives = Lives(3)

    # Create initial game elements
    blocks.create_blocks()
    lives.create_live()
    ball.reset_position()

    return paddle, ball, blocks, scoreboard, lives


def setup_controls(screen, controller):
    """Setup keyboard controls for the game"""
    screen.listen()

    # Movement controls (both WASD and arrow keys)
    screen.onkeypress(controller.press_left, "a")
    screen.onkeyrelease(controller.release_left, "a")
    screen.onkeypress(controller.press_right, "d")
    screen.onkeyrelease(controller.release_right, "d")
    screen.onkeypress(controller.press_left, "Left")
    screen.onkeyrelease(controller.release_left, "Left")
    screen.onkeypress(controller.press_right, "Right")
    screen.onkeyrelease(controller.release_right, "Right")

    # Game controls
    screen.onkeypress(controller.start_ball, "Return")
    screen.onkeypress(controller.start_ball, "space")
    screen.onkeypress(controller.toggle_pause, "p")


def show_message(screen, message, y_pos=0, font_size=20):
    """Display a temporary message on screen"""
    from turtle import Turtle
    text_turtle = Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.color("white")
    text_turtle.goto(0, y_pos)
    text_turtle.write(message, align="center", font=("Courier", font_size, "normal"))
    return text_turtle


def wait_for_ball_start(screen, controller, paddle):
    """Wait for player to start the ball"""
    start_text = show_message(screen, "Press ENTER or SPACE to Start")

    while not controller.ball_started:
        screen.update()
        time.sleep(0.016)  # ~60 FPS

        # Allow paddle movement while waiting
        if controller.move_left:
            paddle.go_left()
        if controller.move_right:
            paddle.go_right()

    start_text.clear()


def handle_collisions(ball, paddle, blocks, scoreboard):
    """Handle all collision detection and responses"""

    # Top wall collision
    if ball.ycor() > TOP_WALL:
        ball.bounce_y()

    # Side wall collisions
    if abs(ball.xcor()) > SIDE_WALL:
        ball.bounce_x()

    # Paddle collision
    if (ball.ycor() < PADDLE_BOUNCE_Y and
            abs(ball.xcor() - paddle.xcor()) < PADDLE_BOUNCE_DISTANCE):
        ball.bounce_y()
        return False  # Ball not lost

    # Ball missed paddle
    if ball.ycor() < MISS_Y:
        return True  # Ball lost

    # Block collisions
    blocks_to_remove = []
    for block in blocks.segments:
        if ball.distance(block) < BLOCK_HIT_DISTANCE:
            scoreboard.update_point(block.value)
            ball.bounce_y()
            block.hideturtle()
            blocks_to_remove.append(block)
            break  # Only hit one block per frame

    # Remove hit blocks
    for block in blocks_to_remove:
        blocks.segments.remove(block)

    return False

def clear_game_objects(paddle, ball, blocks, lives, scoreboard, score_turtle_list):
    """Hides and clears game elements from screen"""
    paddle.hideturtle()
    ball.hideturtle()
    scoreboard.clear()
    scoreboard.hideturtle()
    for block in blocks.segments:
        block.hideturtle()
    for life in lives.lives:
        life.hideturtle()
    for msg in score_turtle_list:
        msg.clear()
        msg.hideturtle()




def handle_game_over(screen, scoreboard):
    """Handle game over sequence and restart option"""
    message_turtles = []

    if scoreboard.score > scoreboard.high_score:
        save_high_score(scoreboard.score)
        message_turtles.append(show_message(screen, "NEW HIGH SCORE!", 50, 18))

    message_turtles.append(show_message(screen, "GAME OVER", 0, 20))
    message_turtles.append(show_message(screen, f"Final Score: {scoreboard.score}", -30, 14))
    message_turtles.append(show_message(screen, "Click to restart or close window to quit", -60, 12))

    screen.update()

    restart_clicked = False

    def on_click(x, y):
        nonlocal restart_clicked
        restart_clicked = True

    screen.onclick(on_click)

    while not restart_clicked:
        screen.update()
        time.sleep(0.1)

    screen.onclick(None)
    return message_turtles


def game_loop():
    """Main game loop"""
    screen = setup_screen()
    controller = GameController()

    while True:  # Allow for game restarts
        # Reset game state
        controller.ball_started = False
        controller.game_paused = False

        # Create game objects
        paddle, ball, blocks, scoreboard, lives = setup_game_objects()

        # Setup controls
        setup_controls(screen, controller)

        # Wait for game to start
        wait_for_ball_start(screen, controller, paddle)

        # Main game loop
        game_running = True

        while game_running:
            # Handle pause
            if controller.game_paused:
                pause_text = show_message(screen, "PAUSED - Press P to continue")
                while controller.game_paused:
                    screen.update()
                    time.sleep(0.1)
                pause_text.clear()

            # Game timing
            time.sleep(ball.move_speed)
            screen.update()

            # Handle input
            if controller.move_left:
                paddle.go_left()
            if controller.move_right:
                paddle.go_right()

            # Move ball
            ball.move()

            # Handle collisions
            ball_lost = handle_collisions(ball, paddle, blocks, scoreboard)

            if ball_lost:
                # Reset ball and paddle
                ball.reset_position()
                paddle.reset_position()
                controller.ball_started = False

                # Check if player has lives left
                if lives.remove_live():
                    # Continue game - wait for ball start
                    wait_for_ball_start(screen, controller, paddle)
                else:
                    # Game over
                    game_running = False
                    message_turtles = handle_game_over(screen, scoreboard)

                    # Clean up all old game objects before restarting
                    clear_game_objects(paddle, ball, blocks, lives, scoreboard, message_turtles)
                    break

            # Check if all blocks destroyed (level complete)
            if not blocks.segments:
                blocks.create_blocks()
                ball.reset_position()
                paddle.reset_position()
                controller.ball_started = False
                wait_for_ball_start(screen, controller, paddle)


def main():
    """Main function to start the game"""
    try:
        game_loop()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            # Clean exit
            screen = Screen()
            screen.bye()
        except:
            pass


if __name__ == "__main__":
    main()