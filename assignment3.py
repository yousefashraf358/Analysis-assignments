def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, end = ' ')

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Example:
graph = {0: set([1, 2]), 1: set([0, 3, 4]), 2: set([0]), 3: set([1]), 4: set([1, 5]), 5: set([4])}
dfs(graph, 0)




from collections import deque

def bfs(graph, start):
    visited, queue = set(), deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example:
bfs(graph, 0)