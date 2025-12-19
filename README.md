# Hand Pac-Man

Hand-gesture controlled Pac-Man maze chase with AI monster pursuit. Navigate Pac-Man using your hands—no controllers or keyboard needed. Real-time webcam hand tracking with **MediaPipe**, vision processing with **OpenCV**, and graphical rendering with **Raylib**.

---

## Overview

**Hand Pac-Man** combines computer vision with interactive gameplay. Using your webcam, the game tracks your hand gestures in real time and maps them to Pac-Man movement directions inside the classic maze while AI ghosts chase the player.

---

## Features

* Hand gesture control for Pac-Man movement
* Real-time hand tracking using MediaPipe Hands
* Webcam frame processing with OpenCV
* Smooth graphics and GUI rendering using Raylib
* Maze logic, collision detection, scoring, and AI ghost pursuit using BFS pathfinding

---
## AI Ghost Behavior (Pathfinding)
The ghost enemies in Hand Pac-Man use the Breadth-First Search (BFS) algorithm to intelligently chase Pac-Man inside the maze.

### How BFS Is Used
* The maze is treated as a grid-based graph, where each cell represents a node.
* Walls act as blocked nodes, while open paths are traversable.
* At each update cycle, a ghost:
  * Takes its current position and target position as the start node and the target.
  * Uses BFS to explore the maze level by level.
  * Finds the shortest available path to the target.
  * Moves one step along that path.

### Why BFS?
* Guarantees the shortest path in an unweighted grid.
* Predictable and efficient for maze-based games.
* Ideal for real-time AI movement without heavy computation.
* This approach gives the ghosts responsive and realistic chasing behavior, closely resembling the logic of the original Pac-Man while remaining simple and reliable.

---

## Demonstration

### Hand Gestures

* gesture_up: open your hands
* gesture_down: close your hands
* gesture_right: close the right hand and keep the left opened
* gesture_left: close the left hand and keep the right opened

---

## Demo Video

[Hand Pac-Man Demo](https://drive.google.com/file/d/1rKVaTpi0GdyrWnNlxQwOyEZ-tZoUzTXI/view?usp=drive_link)


---

## Technologies Used

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| Python     | Core programming language          |
| MediaPipe  | Real-time hand tracking            |
| OpenCV     | Video capture and image processing |
| Raylib     | Game rendering and GUI             |

---

## Requirements

* **Python 3.11.x**
* **raylib 5.5**
* **OpenCV 4.11.0**
* **mediapipe 0.10.31**
* A working webcam

---

## Installation

### 1. Install Python 3.11

Download Python **3.11.x** from the official website:
[https://www.python.org/downloads/release/python-3110/](https://www.python.org/downloads/release/python-3110/)

Make sure Python is added to your system PATH.

Verify installation:

```bash
python --version
```

---

### 2. Clone the Repository

```bash
git clone https://github.com/KyrillosHamdy/Hand_Pac_Man.git
cd Hand_Pac_Man
```

---

### 3. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```
---

### 4. Install Dependencies

Install all required libraries using the provided requirements.txt file:
```
pip install -r requirements.txt
```

---

## Usage

Run the main game file:

```bash
python main.py
```

Ensure your webcam is active and visible. Hand gestures will be detected in real time and mapped to Pac-Man movement inside the maze.

---

## Project Structure

```
Hand_Pac_Man/
├── hand_tracking/
   └── hand_tracking_module.py       # MediaPipe + OpenCV hand tracking
├── main.py                          # Game entry point       
├── game.py                          # Movement and AI logic
├── constants.py                     # Maze and constants
├── README.md
└── requirements.txt
```
---

## License

This project is licensed under the **MIT License**.
