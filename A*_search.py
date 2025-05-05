from queue import PriorityQueue

# Corrected graph with neighbors and their path costs
graph = {
    'A': [('D', 3), ('E', 5)],
    'D': [('L', 3), ('M', 7)],
    'E': [('K', 11), ('T', 2)],
    'L': [('M', 2)],
    'M': [('Y', 1)],
    'K': [('Y', 2), ('T', 5)],
    'T': [('Y', 12)],
    'Y': []
}

# Heuristic values
heuristic = {
    'A': 15,
    'D': 12,
    'E': 14,
    'L': 10,
    'M': 8,
    'K': 9,
    'T': 6,
    'Y': 0
}

def a_star_search(start, goal):
    pq = PriorityQueue()
    pq.put((heuristic[start], 0, start, [start]))  # (f, g, current_node, path)
    visited = set()

    while not pq.empty():
        f, g, current, path = pq.get()
        print("Visiting:", current)

        if current == goal:
            print("Goal found!")
            print("Total cost:", g)
            print("Path:", " -> ".join(path))
            return

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                pq.put((new_f, new_g, neighbor, path + [neighbor]))

# Run the algorithm
a_star_search('A', 'Y')
