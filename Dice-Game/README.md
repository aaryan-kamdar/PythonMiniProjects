# Dice Game

A multiplayer terminal-based dice game built using Python and NumPy. Players take turns rolling a dice and accumulating points. The first player to reach the target score wins the game.

## Features

* Supports 2–4 players
* Random dice rolls
* Turn-based gameplay
* Score tracking
* Win condition at 50 points

## Technologies Used

* Python 3
* NumPy

## How to Run

1. Install NumPy:

```bash
pip install numpy
```

2. Run the program:

```bash
python DiceGame.py
```

## How to Play

* Enter the number of players (2–4).
* On your turn:

  * Enter `y` to roll the dice.
  * Any other input will end your turn and save your current score.
* Rolling a `1` resets your current turn's score.
* The first player to reach 50 points wins.

## Future Improvements

* Fix dice roll to include 6 (`np.random.randint(1, 7)`).
* Add player names.
* Add difficulty levels.
* Display a leaderboard.

## Project Structure

```text
Dice-Game/
├── DiceGame.py
└── README.md
```
