# Game constants
TILE_SIZE = 50
ROWS, COLS = 12, 12
PLAYER_SPEED = 5
MONSTER_SPEED = 2
PLAYER_TIME_STEP = 1.0 / PLAYER_SPEED
MONSTER_TIME_STEP = 1.0 / MONSTER_SPEED
GAME_OVER_TEXT = "Game Over!".encode("utf-8")
GAME_OVER_DURATION = 2.0  # seconds

# Directions: down, right, left, up
DR = [1, 0, 0, -1]
DC = [0, 1, -1, 0]

# Game map (1=wall, 0=empty)
GAME_MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
