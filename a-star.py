from queue import PriorityQueue
 
# define the graph as an adjacency matrix
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'D': 5},
    'C': {'D': 10},
    'D': {'E': 5},
    'E': {}
}
 
# define the heuristic function as the straight-line distance to the goal node
heuristic = {
    'A': 20,
    'B': 15,
    'C': 10,
    'D': 5,
    'E': 0
}
 
def a_star(start, goal):
    # initialize the open list with the start node and its cost and heuristic values
    open_list = PriorityQueue()
    open_list.put((0 + heuristic[start], start, 0))
 
    # initialize the closed list
    closed_list = {}
 
    # initialize the cost and parent dictionaries
    cost = {start: 0}
    parent = {start: None}
 
    while not open_list.empty():
        # get the node with the lowest f value from the open list
        current_f, current_node, current_cost = open_list.get()
 
        # add the current node to the closed list
        closed_list[current_node] = (current_cost, heuristic[current_node])
        print(closed_list)
        # check if the goal node has been reached
        if current_node == goal:
            # reconstruct the path from the goal node to the start node
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path, cost[goal]
 
        # expand the current node
        for neighbor, neighbor_cost in graph[current_node].items():
            # compute the cost of reaching the neighbor node from the current node
            tentative_cost = current_cost + neighbor_cost
 
            # check if the neighbor node is already in the closed list
            if neighbor in closed_list:
                continue
 
            # check if the neighbor node is already in the open list
            if neighbor in cost and tentative_cost >= cost[neighbor]:
                continue
 
            # add the neighbor node to the open list with its cost and heuristic values
            open_list.put((tentative_cost + heuristic[neighbor], neighbor, tentative_cost))
 
            # update the cost and parent dictionaries
            cost[neighbor] = tentative_cost
            parent[neighbor] = current_node
 
        # print the current state of the algorithm
        print('--- Iteration ---')
        print('Open List:', list(open_list.queue))
        print('Closed List:', closed_list)
        print('Cost:', cost)
        print('Parent:', parent)
        print('-----------------')
 
    # if the goal node cannot be reached, return None
    return None
 
# example usage with user input
start_node = input('Enter the start node: ')
goal_node = input('Enter the goal node: ')
path, cost = a_star(start_node, goal_node)
print('Path:', path)
print('Cost:', cost)
