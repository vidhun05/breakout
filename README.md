# Breakout Game

A classic arcade-style Breakout game implemented in Python using the Turtle graphics library.

## Features

- **Classic Gameplay**: Control a paddle to bounce a ball and destroy colored blocks
- **Scoring System**: Different colored blocks give different point values
- **Lives System**: Start with 3 lives, lose one when the ball goes off screen
- **High Score**: Automatically saves and loads your best score
- **Smooth Controls**: Responsive paddle movement with keyboard input
- **Progressive Difficulty**: Ball speed increases slightly with each paddle bounce

## Controls

- **A/D Keys** or **Arrow Keys**: Move paddle left/right
- **Enter** or **Space**: Start/restart the ball
- **P**: Pause/unpause the game

## Installation & Running

1. Make sure you have Python installed (3.6 or higher recommended)
2. Clone or download this repository
3. Navigate to the game directory
4. Run the main game file:

```bash
python main.py
```

## Game Files Structure

- `main.py` - Main game loop and core game logic
- `paddle.py` - Paddle class handling player movement
- `ball.py` - Ball physics and movement
- `blocks.py` - Block creation and management
- `scoreboard.py` - Score display and tracking
- `lives.py` - Lives display and management

## Gameplay

- Use the paddle to keep the ball in play
- Destroy all blocks to advance to the next level
- Different colored blocks give different points:
  - Red blocks: 50 points
  - Teal blocks: 40 points
  - Blue blocks: 30 points
  - Green blocks: 20 points
  - Yellow blocks: 15 points
  - Pink blocks: 10 points

## Technical Details

- Built with Python's built-in Turtle graphics library
- No external dependencies required
- High scores are automatically saved to `highscore.txt`
- Game runs at approximately 60 FPS

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

## License

This project is licensed under a **custom Non-Commercial License based on the MIT License**.

You are free to:
- Use the software for personal or educational purposes
- Modify and improve the code
- Contribute via pull requests

You are **not allowed** to:
- Sell or use this software for commercial purposes
- Distribute modified versions for profit

See the [LICENSE](LICENSE) file for full terms.

## Support

If you encounter any problems or have questions, please:
1. Check the [Issues](https://github.com/vidhun05/IMPRINT/issues) page
2. Create a new issue if your problem isn't already listed
3. Provide as much detail as possible about your setup and the issue

---

⭐ **If you found this project helpful, please give it a star!** ⭐
