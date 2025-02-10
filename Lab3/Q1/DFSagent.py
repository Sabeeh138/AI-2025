class DFSAgent:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.visited = set()
        self.stack = [start]
    
    def run(self):
        while self.stack:
            current_node = self.stack.pop()
            if current_node == self.goal:
                return True  # Goal found
            if current_node not in self.visited:
                self.visited.add(current_node)
                neighbors = self.graph.get_neighbors(current_node)
                for neighbor in neighbors:
                    if neighbor not in self.visited:
                        self.stack.append(neighbor)
        return False  # Goal not found
