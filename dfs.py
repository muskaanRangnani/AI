# Define the DFS function
def dfs(graph, start):
    # Create a list to keep track of visited nodes
    visited = []
    # Create a stack for DFS
    stack = [start]
    # Perform DFS
    while stack:
        # Pop a vertex from the stack
        vertex = stack.pop()
        # If the vertex has not been visited yet
        if vertex not in visited:
            # Mark the vertex as visited
            visited.append(vertex)
            # Add all unvisited neighbors of the vertex to the stack
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
    # Return the visited nodes
    return visited

# Get user input for the graph
n = int(input("Enter the number of nodes: "))
graph = {}
for i in range(n):
    node = input("Enter the name of node " + str(i+1) + ": ")
    neighbors = input("Enter the neighbors of node " + node + " (comma-separated): ")
    graph[node] = neighbors.split(",")

# Test the DFS function
start_node = input("Enter the start node: ")
visited = dfs(graph, start_node)
print("Visited nodes: ", visited)