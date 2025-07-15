# Space Maze Rescue Game 🚀👨‍🚀

A thrilling space rescue mission game built with Python's Turtle graphics! Navigate your rocket through space to save the stranded astronaut and complete your heroic mission.

## 🌌 Game Overview

You are a skilled pilot on a rescue mission in deep space. Your objective is to navigate your rocket through the cosmic environment and reach the stranded spaceman to complete a successful rescue operation!

## 🎮 Game Features

- **Space Theme**: Beautiful space background with stars and cosmic elements
- **Rescue Mission**: Navigate to save the stranded astronaut
- **Smooth Controls**: Arrow key navigation with directional rocket movement
- **Victory Celebration**: Special "Thank You" screen when mission is completed
- **Real-time Gameplay**: Continuous collision detection and smooth movement

## 🎯 How to Play

1. **Objective**: Navigate your rocket to the stranded spaceman
2. **Controls**: Use arrow keys to move your rocket in all directions
3. **Mission Complete**: Get within close range of the spaceman to rescue him
4. **Victory**: Enjoy the thank you message for completing your heroic mission!

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Turtle graphics library (included with Python)

### Required Files

Ensure these image files are in the same directory as your Python script:

- `background.gif` - Space background scene
- `spaceman.gif` - Stranded astronaut sprite
- `rocket.gif` - Player's rocket sprite
- `Thankyou.gif` - Victory/completion screen

### Installation & Running

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/spacemaze-rescue-game.git
   cd spacemaze-rescue-game
   ```

2. **Run the game**:
   ```bash
   python macegame.py
   ```

3. **Start your mission**: Use arrow keys to navigate and rescue the spaceman!

## 🎮 Controls

| Key | Action |
|-----|--------|
| ↑ (Up Arrow) | Move rocket up |
| ↓ (Down Arrow) | Move rocket down |
| ← (Left Arrow) | Move rocket left |
| → (Right Arrow) | Move rocket right |

## 🏁 Game Mechanics

- **Starting Positions**: 
  - Spaceman: Upper left area (-103, 255)
  - Rocket: Lower right area (180, -250)
- **Movement**: Each key press moves the rocket 10 pixels in the chosen direction
- **Win Condition**: Get within 10 pixels of the spaceman to trigger rescue
- **Victory**: Special thank you screen displays upon successful rescue

## 🛠️ Technical Details

- **Language**: Python 3.x
- **Graphics Library**: Turtle
- **Game Loop**: Continuous screen updates with collision detection
- **Input System**: Real-time key press event handling
- **Collision Detection**: Distance-based rescue trigger

## 📁 Project Structure

```
spacemaze-rescue-game/
├── macegame.py          # Main game script
├── background.gif       # Space background
├── spaceman.gif         # Astronaut sprite
├── rocket.gif           # Rocket sprite
├── Thankyou.gif         # Victory screen
└── README.md           # This file
```

## 🎨 Customization Options

Enhance your game by modifying:

- **Movement Speed**: Change `forward(10)` values for faster/slower movement
- **Starting Positions**: Adjust `goto()` coordinates for different spawn points
- **Rescue Distance**: Modify the `< 10` threshold for rescue trigger sensitivity
- **Graphics**: Replace GIF files with your own custom space-themed sprites
- **Sound Effects**: Add audio feedback for movement and rescue completion

## 🐛 Troubleshooting

### Common Issues:

1. **"BadTurtleShape" Error**:
   - Verify all .gif files are in the same directory as the Python script
   - Ensure images are in proper GIF format

2. **Rocket doesn't move**:
   - Make sure the game window has focus (click on it)
   - Check that arrow keys are being pressed
   - Verify `turtle.listen()` is functioning

3. **Game doesn't detect rescue**:
   - Ensure you're getting close enough to the spaceman
   - Check that the collision detection loop is running

4. **Victory screen doesn't appear**:
   - Verify `Thankyou.gif` exists in the project directory
   - Check file name spelling and capitalization

## 🌟 Future Enhancements

Ideas for expanding the game:

- **Obstacles**: Add asteroids or space debris to avoid
- **Fuel System**: Limited fuel adds challenge
- **Multiple Levels**: Different rescue scenarios
- **Timer**: Add time pressure for more excitement
- **Score System**: Points for speed and efficiency
- **Sound Effects**: Space-themed audio feedback
- **Animations**: Smooth sprite animations
- **Power-ups**: Special abilities or speed boosts

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎉 Acknowledgments

- Built with Python's Turtle graphics library
- Inspired by classic arcade space games
- Thanks to the open-source community for inspiration and resources

---

**Ready for your space rescue mission? 🚀**

*Launch the game and save the day! If you encounter any issues or have suggestions, please open an issue on GitHub.*

## 📞 Support

If you need help or have questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the Python Turtle documentation

**Happy rescuing, space pilot! 🌌👨‍🚀**
