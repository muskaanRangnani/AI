import math
import random
 
# Define the function to be optimized
def objective_function(x, y):
    return math.sin(x) * math.cos(0.5 * x) + math.sin(y) * math.cos(0.5 * y)
 
# Define the simulated annealing parameters
initial_temperature = 100
final_temperature = 1
alpha = 0.99
num_iterations = 1000
 
# Define the search space
x_range = (-10, 10)
y_range = (-10, 10)
 
# Define the initial solution
x_current = random.uniform(*x_range)
y_current = random.uniform(*y_range)
solution_current = objective_function(x_current, y_current)
 
# Define the best solution
x_best = x_current
y_best = y_current
solution_best = solution_current
 
# Run the simulated annealing algorithm
temperature = initial_temperature
for i in range(num_iterations):
    # Generate a candidate solution
    x_candidate = random.uniform(*x_range)
    y_candidate = random.uniform(*y_range)
    solution_candidate = objective_function(x_candidate, y_candidate)
    # Check if the candidate solution is better than the current solution
    if solution_candidate < solution_current:
        x_current = x_candidate
        y_current = y_candidate
        solution_current = solution_candidate
    else:
        delta = solution_candidate - solution_current
        probability = math.exp(-delta / temperature)
        if random.random() < probability:
            x_current = x_candidate
            y_current = y_candidate
            solution_current = solution_candidate
    # Update the best solution
    if solution_current < solution_best:
        x_best = x_current
        y_best = y_current
        solution_best = solution_current
    # Cool the temperature
    temperature = temperature * alpha
    if temperature < final_temperature:
        break
# Print the best solution
print("x = ", x_best)
print("y =  ", y_best)
print("objective function value = ", solution_best)