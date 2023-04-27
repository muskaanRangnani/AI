# Class representing a graph
class Graph:
    def __init__(self):
        self.graph = {}

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # Function to perform DFIDS on the graph
    def dfids(self, start, goal, max_depth):
        # Loop through depths from 0 to max_depth
        for depth in range(max_depth):
            # Call recursive depth-limited search function
            visited = set()
            path = self.dls(start, goal, depth, visited)
            # If a path is found, return it along with the depth
            if path is not None:
                return path, depth
        # If no path found, return None
        return None, None

    # Function to perform recursive depth-limited search
    def dls(self, node, goal, depth, visited):
        # If goal is found, return path
        if node == goal:
            return [node]
        # If depth limit reached, return None
        if depth == 0:
            return None
        # Mark node as visited
        visited.add(node)
        # Recurse through unvisited neighbor nodes
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                # Call recursive function with decreased depth
                path = self.dls(neighbor, goal, depth-1, visited)
                # If path is found, return it
                if path is not None:
                    return [node] + path
        # If no path found, return None
        return None

# Example usage
if __name__ == '__main__':
    # Initialize graph
    graph = Graph()

    # Prompt user for graph edges
    num_edges = int(input("Enter number of edges: "))
    for i in range(num_edges):
        u, v = input("Enter edge (u, v): ").split()
        graph.add_edge(u, v)

    # Prompt user for start and goal nodes
    start = input("Enter start node: ")
    goal = input("Enter goal node: ")

    # Perform DFIDS on graph
    path, depth = graph.dfids(start, goal, 10)

    # Print result
    if path is None:
        print("No path found")
    else:
        print("Path:", " -> ".join(path))
        print("Depth:", depth)
