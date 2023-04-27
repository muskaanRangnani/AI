import numpy as np

def find_neighbors(state, landscape):
    neighbors = []
    dim = landscape.shape
 
    # left
    if state[0] != 0:
        neighbors.append((state[0]-1, state[1]))
 
    # right
    if state[0] != dim[0]-1:
        neighbors.append((state[0]+1, state[1]))
 
    # top
    if state[1] != 0:
        neighbors.append((state[0], state[1]-1))
 
    # bottom
    if state[1] != dim[1]-1:
        neighbors.append((state[0], state[1]+1))
 
    # top left
    if state[0] != 0 and state[1] != 0:
        neighbors.append((state[0]-1, state[1]-1))
 
    # bottom left
    if state[0] != 0 and state[1] != dim[1]-1:
        neighbors.append((state[0]-1, state[1]+1))
 
    # top right
    if state[0] != dim[0]-1 and state[1] != 0:
        neighbors.append((state[0]+1, state[1]-1))
 
    # bottom right
    if state[0] != dim[0]-1 and state[1] != dim[1]-1:
        neighbors.append((state[0]+1, state[1]+1))
    return neighbors
 
 
def hill_climb(curr_state, landscape):
    neighbors = find_neighbors(curr_state, landscape)
    bool
    ascended = False
    next_state = curr_state
 
    for neighbor in neighbors:
        if landscape[neighbor[0]][neighbor[1]] > landscape[next_state[0]][next_state[1]]:
            next_state = neighbor
            ascended = True
    return ascended, next_state
 
 
def __main__():
    landscape = np.random.randint(1, high=50, size=(10, 10))
    print(landscape)
    start_state = (3, 6)
    current_state = start_state
    count = 1
    ascending = True
    while ascending:
        print("\nStep #", count)
        print("Current state coordinates: ", current_state)
        print("Current state value: ",
              landscape[current_state[0]][current_state[1]])
        count += 1
        ascending, current_state = hill_climb(current_state, landscape)
    print("\nStep #", count)
    print("Optimization objective reached")
    print("final state coordinates: ", current_state)
    print("Final state value:", landscape[current_state[0]][current_state[1]])
    
__main__()