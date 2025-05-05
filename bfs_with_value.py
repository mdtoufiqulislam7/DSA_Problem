from queue import PriorityQueue

# Graph structure as an adjacency list with heuristic values
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [],
    'G': []
}

# Heuristic values for each node
heuristic = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 6,
    'E': 2,
    'F': 6,
    'G': 0
}

def best_first_search(start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic[start], start))

    while not pq.empty():
        _, current = pq.get()
        print("Visited:", current)
        if current == goal:
            print("Goal found!")
            return
        visited.add(current)
        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                pq.put((heuristic[neighbor], neighbor))

# Run the algorithm
best_first_search('A', 'G')