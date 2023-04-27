from queue import PriorityQueue
 
# Define the graph as an adjacency matrix
graph = {
    'A': {'B': 9, 'C': 4},
    'B': {'C': 2, 'D': 7, 'E': 3},
    'C': {'D': 1, 'E': 6},
    'D': {'E': 4, 'F': 8},
    'E': {'F': 2},
    'F': {}
}
 
def ucs(start, goal):
    # Initialize the open list with the start node and its cost
    open_list = PriorityQueue()
    open_list.put((0, start))
 
    # Initialize the closed list
    closed_list = {}
 
    # Initialize the cost and parent dictionaries
    cost = {start: 0}
    parent = {start: None}
 
    while not open_list.empty():
        # Get the node with the lowest cost from the open list
        current_cost, current_node = open_list.get()
 
        # Add the current node to the closed list
        closed_list[current_node] = current_cost
 
        # Check if the goal node has been reached
        if current_node == goal:
            # Reconstruct the path from the goal node to the start node
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path, cost[goal]
 
        # Expand the current node
        for neighbor, neighbor_cost in graph[current_node].items():
            # Compute the cost of reaching the neighbor node from the current node
            tentative_cost = current_cost + neighbor_cost
 
            # Check if the neighbor node is already in the closed list
            if neighbor in closed_list:
                continue
 
            # Check if the neighbor node is already in the open list
            if neighbor in cost and tentative_cost >= cost[neighbor]:
                continue
 
            # Add the neighbor node to the open list with its cost
            open_list.put((tentative_cost, neighbor))
 
            # Update the cost and parent dictionaries
            cost[neighbor] = tentative_cost
            parent[neighbor] = current_node
 
        # Print the current state of the algorithm
        print('--- Iteration ---')
        print('Open List:', list(open_list.queue))
        print('Closed List:', closed_list)
        print('-----------------')
 
    # If the goal node cannot be reached, return None
    return None
 
path, cost = ucs('A', 'F')
print('Path:', path)
print('Cost:', cost)