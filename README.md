# PythonMiniProjects

A collection of Python projects built while learning programming fundamentals, problem-solving, APIs, desktop applications, and software development concepts.

These projects demonstrate skills in:

* Python programming
* Object-oriented and functional concepts
* Input validation
* File handling
* API integration
* Terminal and desktop user interfaces
* Algorithmic thinking
* Performance measurement
* Exception handling
* Working with external tools

---

## Projects Included

### 1. Dice Game

A multiplayer dice game where players compete to reach 50 points. Players can choose to continue rolling or hold their score, adding an element of strategy.

**Skills Demonstrated:**

* Loops
* Functions
* Conditional statements
* NumPy
* Game logic

---

### 2. Typing Speed Test

A real-time terminal typing test built with Python's `curses` library that calculates Words Per Minute (WPM) and highlights typing accuracy.

**Skills Demonstrated:**

* Terminal UI development
* File handling
* Real-time calculations
* Event handling
* Performance tracking

---

### 3. Timed Math Quiz

A command-line math quiz that generates random arithmetic problems and measures the time taken to solve them.

**Skills Demonstrated:**

* Random number generation
* Time measurement
* User interaction
* Problem generation

---

### 4. Slot Machine Simulator

A slot machine game where users can deposit money, place bets, and win rewards based on symbol combinations.

**Skills Demonstrated:**

* Data structures (Dictionaries)
* Input validation
* Probability and randomness
* Modular programming

---

### 5. Weather Watch

A weather monitoring application that retrieves real-time weather data from the OpenWeatherMap API and allows users to compare conditions across multiple cities.

**Skills Demonstrated:**

* REST APIs
* Exception handling
* Pandas
* JSON parsing
* Data presentation
* Environment variable management

---

### 6. YouTube Video Downloader

A desktop-based application that downloads YouTube videos in high quality and automatically merges audio and video streams using FFmpeg.

**Skills Demonstrated:**

* GUI programming with Tkinter
* File management
* Subprocess handling
* FFmpeg integration
* Regular expressions
* Third-party libraries

---

## Repository Structure

```text
PythonMiniProjects/
│
├── Dice-Game/
│   ├── DiceGame.py
│   └── README.md
│
├── Typing-Test/
│   ├── TypingTest.py
│   ├── text.txt
│   └── README.md
│
├── Timed-Math-Quiz/
│   ├── TimedMath.py
│   └── README.md
│
├── Slot-Machine/
│   ├── SlotMachine.py
│   └── README.md
│
├── Weather-Watch/
│   ├── WeatherWatch.py
│   └── README.md
│
├── Youtube-Video-Downloader/
│   ├── YoutubeVideoDownloader.py
│   └── README.md
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/PythonMiniProjects.git
```

Move into the project directory:

```bash
cd PythonMiniProjects
```

Install dependencies:

```bash
pip install numpy
pip install pandas
pip install requests
pip install pytubefix
pip install windows-curses    # Windows users only
```

> Note: `WeatherWatch.py` requires an OpenWeatherMap API key, and `YoutubeVideoDownloader.py` requires FFmpeg to be installed and added to your system PATH.

---

## Running the Projects

Run any project using Python:

```bash
python DiceGame.py
python TypingTest.py
python TimedMath.py
python SlotMachine.py
python WeatherWatch.py
python YoutubeVideoDownloader.py
```





This project is open source and available under the MIT License.
