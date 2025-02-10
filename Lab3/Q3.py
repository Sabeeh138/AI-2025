from collections import deque

# Iterative Deepening Depth-First Search (IDDFS)
def depth_limited_search(graph, node, goal, depth):
    if node == goal:
        return [node]
    if depth <= 0:
        return None
    
    for neighbor in graph.get(node, []):
        path = depth_limited_search(graph, neighbor, goal, depth - 1)
        if path:
            return [node] + path
    return None

def iterative_deepening_dfs(graph, start, goal, max_depth=10):
    for depth in range(max_depth):
        path = depth_limited_search(graph, start, goal, depth)
        if path:
            return path
    return None

# Bidirectional Search
def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]
    
    front_visited = {start: [start]}
    back_visited = {goal: [goal]}
    
    front_queue = deque([start])
    back_queue = deque([goal])
    
    while front_queue and back_queue:
        # Expand from the front
        if front_queue:
            node = front_queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor not in front_visited:
                    front_visited[neighbor] = front_visited[node] + [neighbor]
                    front_queue.append(neighbor)
                    if neighbor in back_visited:
                        return front_visited[neighbor] + back_visited[neighbor][::-1][1:]
        
        # Expand from the back
        if back_queue:
            node = back_queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor not in back_visited:
                    back_visited[neighbor] = back_visited[node] + [neighbor]
                    back_queue.append(neighbor)
                    if neighbor in front_visited:
                        return front_visited[neighbor] + back_visited[neighbor][::-1][1:]
    
    return None

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': []
}

# Testing IDDFS
print("IDDFS Path:", iterative_deepening_dfs(graph, 'A', 'I'))

# Testing Bidirectional Search
print("Bidirectional Search Path:", bidirectional_search(graph, 'A', 'I'))
