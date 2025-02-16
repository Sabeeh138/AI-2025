import heapq
import random
import time

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def generate_dynamic_costs(rows, cols):
    return {(r, c): random.randint(1, 10) for r in range(rows) for c in range(cols)}

def a_star_search(maze, start, goal, costs):
    rows, cols = len(maze), len(maze[0])
    open_set = [(0, start)]
    g_score = {start: 0}
    parent = {}
    visited = set()
    while open_set:
        _, current = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                new_g = g_score[current] + costs[(nr, nc)]
                if (nr, nc) not in g_score or new_g < g_score[(nr, nc)]:
                    g_score[(nr, nc)] = new_g
                    heapq.heappush(open_set, (new_g + heuristic((nr, nc), goal), (nr, nc)))
                    parent[(nr, nc)] = current
    return []

def dynamic_pathfinding(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    costs = generate_dynamic_costs(rows, cols)
    while True:
        path = a_star_search(maze, start, goal, costs)
        print("Current optimal path:", path)
        time.sleep(2)
        costs = generate_dynamic_costs(rows, cols)

maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', 'G', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '.'],
    ['.', '.', 'G', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (6, 6)
dynamic_pathfinding(maze, start, goal)
