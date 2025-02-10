class DLSAgent:
    def __init__(self, graph, start, goal, max_depth):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.max_depth = max_depth
        self.visited = set()
        self.stack = [(start, 0)]  # (node, depth)
    
    def run(self):
        while self.stack:
            current_node, depth = self.stack.pop()
            if current_node == self.goal:
                return True  # Goal found
            if depth < self.max_depth and current_node not in self.visited:
                self.visited.add(current_node)
                neighbors = self.graph.get_neighbors(current_node)
                for neighbor in neighbors:
                    if neighbor not in self.visited:
                        self.stack.append((neighbor, depth + 1))
        return False  # Goal not found
