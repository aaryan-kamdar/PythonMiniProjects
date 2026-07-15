# Typing Speed Test

A terminal-based typing speed test built using Python's `curses` library. The application measures Words Per Minute (WPM) in real time and provides visual feedback for correct and incorrect characters.

## Features

* Real-time WPM calculation
* Colored character feedback
* Random text selection
* Backspace support
* ESC key to exit
* Responsive terminal interface

## Technologies Used

* Python 3
* Curses
* Time
* Random

## Requirements

### Linux/macOS

`curses` is included by default.

### Windows

```bash
pip install windows-curses
```

## How to Run

```bash
python TypingTest.py
```

## Files

```text
Typing-Test/
├── TypingTest.py
├── text.txt
└── README.md
```

## Sample Output

```text
Welcome to the Speed Typing Test!

WPM: 68
The quick brown fox jumps over the lazy dog.
```

## Future Improvements

* Add accuracy percentage.
* Add multiple difficulty levels.
* Implement a leaderboard.
* Save typing statistics.
* Add multiplayer mode.
