import numpy as np

class UMDA:
    class Solution:
        def __init__(self, string, fitness) -> None:
            self.string = string
            self.fitness = fitness

    def __init__(self, fitness_function, num_generations, population_size, parent_size, offspring_size, max_string_size, alphabet) -> None:
        self.num_generations = num_generations
        self.fitness_function = fitness_function
        self.offspring_size = offspring_size
        self.parent_size = parent_size
        self.population_size = population_size
        self.max_string_size = max_string_size
        self.alphabet = alphabet

    def generate_single_solution(self, item_probability_vector, max_string_size, alphabet) -> Solution:
        # item_probability_vector neka bude matrica koja sadrzi u redovima poziciju u stringu, a u stupcima 
        # lokacija i,j govori kolika je vjerojatnost da se slovo i pojavi na mjestu j

        print("Generating single solution...")
        string = []
        for i in range(max_string_size):
            roulette_wheel = np.cumsum(
            item_probability_vector[i]
            )
            random_number = np.random.rand()
            for index, score in enumerate(roulette_wheel):
                if random_number <= score:
                    string.append(alphabet[index])
                    break
        print(string)
        return self.Solution(string, self.fitness_function())
    
    def calculate(self, probability_vector):
        single_solution = self.generate_single_solution(probability_vector, self.max_string_size, self.alphabet)