from constants import ROWS, COLS, TILE_SIZE, GAME_MAP, DR, DC
from collections import deque

class cell:
    def __init__(self, x = -1, y = -1):
        self.x = x
        self.y = y

class Game:
    def __init__(self):
        self.pac_man = cell(x = 1, y = 1)
        self.monster = cell(x = 10, y = 9)
        self.player_elapsed = 0
        self.monster_elapsed = 0
        self.moved = False

    def is_valid_pos(self, cell):
        return 0 <= cell.x < ROWS and 0 <= cell.y < COLS and GAME_MAP[cell.x][cell.y] == 0

    def center_calc(self, cell):
        x = cell.x * TILE_SIZE + TILE_SIZE // 2
        y = cell.y * TILE_SIZE + TILE_SIZE // 2
        return (x, y)

def draw_blocks():
    from constants import ROWS, COLS, TILE_SIZE, GAME_MAP
    import raylib as rl
    
    for row in range(ROWS):
        for col in range(COLS):
            if GAME_MAP[row][col] == 1:
                rl.DrawRectangle(row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE, rl.BLACK)
            else: 
                rl.DrawRectangle(row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE, rl.GRAY)

def bfs(start_cell, target_cell):
    from constants import ROWS, COLS, GAME_MAP, DR
    
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    parent = {} 

    queue = deque([start_cell])
    visited[start_cell.x][start_cell.y] = True
    
    found = False
    
    while queue:
        cur = queue.popleft()

        if cur.x == target_cell.x and cur.y == target_cell.y:
            found = True
            break

        for i in range(4):
            nx, ny = cur.x + DR[i], cur.y + DC[i]

            if 0 <= nx < ROWS and 0 <= ny < COLS:
                if GAME_MAP[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    parent[(nx, ny)] = (cur.x, cur.y)
                    queue.append(cell(nx, ny))

    path = []
    if found:
        curr_coords = (target_cell.x, target_cell.y)
        start_coords = (start_cell.x, start_cell.y)
        
        while curr_coords != start_coords:
            path.append(cell(curr_coords[0], curr_coords[1]))
            curr_coords = parent[curr_coords]
        
        path.append(start_cell)
        
    return path
