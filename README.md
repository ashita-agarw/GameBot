# GameBot

Biulding Games in PyGame

# Custom Flappy Bird Game

## Motivation
I found the original Flappy Bird game too challenging, so I decided to create my own version where I can control the environment and make it more enjoyable and customizable. This project allowed me to tweak the difficulty, design, and overall experience to suit my preferences.

---

## Features
- **Customizable Background:** Choose between two game modes – Day or Evening.
- **Dynamic Pillars:** Randomly generated obstacles with adjustable gaps and positions.
- **Score Tracking:**
  - Real-time score display during gameplay.
  - High score tracking to challenge yourself.
- **Simplified Physics:** Controlled bird movement for a more approachable difficulty level.
- **Seamless Floor Movement:** Endless scrolling effect for immersive gameplay.
- **Game Over Screen:** Displays current score and high score for feedback.

---

## How It Works
1. **Game Environment Setup:**
   - Choose your preferred background mode (Day or Evening) when starting the game.
   - Backgrounds and other assets are loaded dynamically based on user selection.

2. **Gameplay Mechanics:**
   - The bird moves downward due to gravity and can be propelled upwards by pressing the **Spacebar**.
   - Random pillars appear periodically, moving from right to left.
   - Collisions with pillars or boundaries end the game.

3. **Score and High Score Tracking:**
   - Score increases over time while the game is active.
   - The highest score achieved is saved and displayed on the Game Over screen.

4. **Restarting the Game:**
   - Press **Spacebar** after a game over to reset and start a new round.

---

## Tools and Libraries
- **Programming Language:** Python
- **Game Development Library:** `pygame`

---

## Instructions to Run
1. Install Python and the `pygame` library.
2. Place all image assets (backgrounds, bird, pillars, floor, game over screen) in a folder named `PIX` in the same directory as the script.
3. Run the script in your Python environment.
4. Follow the on-screen prompts to select a game mode and enjoy!

---

## Future Enhancements
- Add difficulty levels (e.g., faster pillars or smaller gaps).
- Introduce power-ups and rewards.
- Implement more customization options for the environment and bird.

---

This project was a fun way to explore game design while tailoring the experience to my preferences. It demonstrates how coding can bring creative ideas to life!

