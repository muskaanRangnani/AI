from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start_node):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(start_node)
        visited[start_node] = True
        
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

g = Graph()

# User input for number of edges
n = int(input("Enter the number of edges: "))

# User input for edges
for i in range(n):
    u, v = map(int, input("Enter edge {} (u v): ".format(i+1)).split())
    g.add_edge(u, v)

# User input for starting node
start_node = int(input("Enter the start node: "))

print("BFS Traversal from node {}: ".format(start_node), end="")
g.bfs(start_node)
