import random
def fitness_function(x, y):
    return (x*2 + y*2)
num_individuals = 10
num_generations = 500
x_range = [10, 20]
y_range = [10, 80]
mutation_rate = 0.1
def roulette_wheel_selection(population):
    total_fitness = sum(fitness_function(*individual) for individual in population)
    selected = random.uniform(0, total_fitness)
    current_sum = 0
    for individual in population:
        current_sum += fitness_function(*individual)
        if current_sum > selected:
            return individual
    return population[-1]
population = [(random.uniform(*x_range), random.uniform(*y_range)) for i in range(num_individuals)]
for generation in range(num_generations):
    fitness_scores = [(individual, fitness_function(*individual)) for individual in population]
    parent1 = roulette_wheel_selection(population)
    parent2 = roulette_wheel_selection(population)
    child = ((parent1[0] + parent2[0])/2, (parent1[1] + parent2[1])/2)
    if random.random() < mutation_rate:
        child = (child[0] + random.uniform(-1, 1), child[1] + random.uniform(-1, 1))
    min_fitness = min(fitness_scores, key=lambda x: x[1])[1]
    population.remove(min(fitness_scores, key=lambda x: x[1])[0])
    population.append(child)
    best_solution = max(fitness_scores, key=lambda x: x[1])[0]
    print(f"Generation {generation}: Best solution = {best_solution}, Fitness = {fitness_function(*best_solution)}")