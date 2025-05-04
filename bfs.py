from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()

        if node == goal:
            print(f"Goal {goal} found! Path: {' -> '.join(path)}")
            return

        if node not in visited:
            visited.add(node)


            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    print("Goal not found.")


graph = {
    '0': ['1','2','3'],
    '1': ['4','5'],
    '2':['6'],
    '3':['7']
}
bfs(graph, '0', '7')