import heapq

class UCSAgent:
    def __init__(self, graph, start, goal):
        self.graph = graph
        self.start = start
        self.goal = goal
        self.visited = set()
        self.priority_queue = []
        heapq.heappush(self.priority_queue, (0, start))  # (cost, node)
    
    def run(self):
        while self.priority_queue:
            current_cost, current_node = heapq.heappop(self.priority_queue)
            if current_node == self.goal:
                return True  # Goal found with minimum cost
            if current_node not in self.visited:
                self.visited.add(current_node)
                neighbors = self.graph.get_neighbors(current_node)
                for neighbor, cost in neighbors:
                    if neighbor not in self.visited:
                        total_cost = current_cost + cost
                        heapq.heappush(self.priority_queue, (total_cost, neighbor))
        return False  # Goal not found
