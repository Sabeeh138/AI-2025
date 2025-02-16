import heapq
from itertools import permutations

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_first_search(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = [(0, start)]
    visited = set()
    parent = {}
    while queue:
        _, current = heapq.heappop(queue)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#' and (nr, nc) not in visited:
                heapq.heappush(queue, (heuristic((nr, nc), goal), (nr, nc)))
                parent[(nr, nc)] = current
    return []

def find_shortest_path(maze, start, goals):
    shortest_path = None
    shortest_distance = float('inf')
    for perm in permutations(goals):
        path = []
        total_distance = 0
        current_pos = start
        for goal in perm:
            segment = best_first_search(maze, current_pos, goal)
            if not segment:
                break
            if path:
                path.extend(segment[1:])
            else:
                path.extend(segment)
            total_distance += len(segment) - 1
            current_pos = goal
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_path = path
    return shortest_path

maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['#', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', 'G', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '.'],
    ['.', '.', 'G', '.', '.', '.', 'G']
]

goals = [(4, 2), (6, 2), (6, 6)]
start = (0, 0)

path = find_shortest_path(maze, start, goals)
print(path)
