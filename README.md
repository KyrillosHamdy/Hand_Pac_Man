# HandPac Maze 🖐️🎮

**Hand-gesture controlled Pac-Man maze chase with AI monster pursuit!**  
Real-time webcam tracking via MediaPipe + raylib rendering. No controllers needed!

## ✨ Features
- **Dual-hand gestures**: Index finger positions control up/down/left/right
- **Smart AI ghost**: BFS pathfinding chases you at 3 FPS
- **12x12 maze**: Navigate walls, collision resets to start
- **60 FPS smooth**: raylib + OpenCV pipeline

## 🛠️ Tech
```
raylib (graphics) + OpenCV (vision) + MediaPipe Hands (tracking)
```

## 🚀 Quick Start
```bash
pip install raylib opencv-python mediapipe
python handpac_maze.py
```
Point webcam at hands, extend index fingers, gesture away!

## 📄 License
[MIT](LICENSE) - Free to use anywhere!

[Demo Video](link-to-demo) | [Try it!](link-to-repo)
