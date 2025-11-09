from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
sequence = bfs(graph, start)
print("BFS Traversal Sequence:", sequence)

Algorithm: Breadth First Search (BFS)

Step 1: Start from the starting node (say A).
Step 2: Create a queue and a visited list to keep track of visited nodes.
Step 3: Mark the starting node as visited and enqueue it.
Step 4: While the queue is not empty:
  a) Dequeue a node from the queue.
  b) Visit all its adjacent (connected) nodes.
  c) If an adjacent node is not visited, mark it visited and enqueue it.
Step 5: Continue until all reachable nodes are visited.
Step 6: Display the BFS traversal order.
