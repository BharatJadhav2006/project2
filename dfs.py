def dfs(graph, start, visited):
    print(start, end=" ")
    visited[start] = True
    for i in range(len(graph[start])):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

n = int(input("Enter number of locations: "))
locations = []
for i in range(n):
    loc = input(f"Enter location name {i+1}: ")
    locations.append(loc)

graph = []
print("Enter adjacency matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start_loc = input("Enter starting location: ")
start_index = locations.index(start_loc)
visited = [False]*n

print("DFS Traversal:")
dfs(graph, start_index, visited)


Algorithm: DFS using Adjacency Matrix

1. Start with the starting node (say A).


2. Mark the starting node as visited.


3. Visit the adjacent (connected) unvisited nodes of the current node.


4. For each unvisited node, call DFS recursively.


5. Repeat the process until all nodes are visited.


6. Stop when all nodes are explored
