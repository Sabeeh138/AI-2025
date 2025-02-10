from itertools import permutations

def calculate_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i+1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to start
    return total_distance

def tsp_brute_force(distance_matrix):
    cities = list(distance_matrix.keys())
    min_distance = float('inf')
    best_route = None
    
    for perm in permutations(cities):
        distance = calculate_distance(perm, distance_matrix)
        if distance < min_distance:
            min_distance = distance
            best_route = perm
    
    return best_route, min_distance

distance_matrix = {
    1: {2: 20, 3: 15, 4: 10},
    2: {1: 20, 3: 35, 4: 25},
    3: {1: 15, 2: 35, 4: 30},
    4: {1: 10, 2: 25, 3: 30}
}

best_route, min_distance = tsp_brute_force(distance_matrix)
print("Shortest Route:", best_route)
print("Minimum Distance:", min_distance)
