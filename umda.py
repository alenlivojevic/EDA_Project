import numpy as np

class UMDA:
    class Solution:
        def __init__(self, string, fitness) -> None:
            self.string = string
            self.fitness = fitness

    def __init__(self, fitness_function, num_generations, population_size, parent_size, offspring_size, max_string_size, alphabet, probability_vector, freq) -> None:
        self.num_generations = num_generations
        self.fitness_function = fitness_function
        self.offspring_size = offspring_size
        self.parent_size = parent_size
        self.population_size = population_size
        self.max_string_size = max_string_size
        self.alphabet = alphabet
        self.probability_vector = probability_vector
        self.freq = freq

    def generate_single_solution(self) -> Solution:
        # item_probability_vector neka bude matrica koja sadrzi u redovima poziciju u stringu, a u stupcima 
        # lokacija i,j govori kolika je vjerojatnost da se slovo i pojavi na mjestu j

        string = []
        for i in range(self.max_string_size):
            roulette_wheel = np.cumsum(
            self.probability_vector[i]
            )
            random_number = np.random.rand()
            for index, score in enumerate(roulette_wheel):
                if random_number <= score:
                    string.append(self.alphabet[index])
                    break
        return self.Solution(string, self.fitness_function(string))
    
    """ def update_frequences():
    
        return """
    
    def generate_random_population(self):
        
       # probability_vector = [[1, 0, 0, 0],
        #                      [0.25, 0.25, 0.25, 0.25],
         #                     [0.25, 0.25, 0.25, 0.25],
          #                    [0.25, 0.25, 0.25, 0.25]]
 
        return [self.generate_single_solution() for _ in range(self.population_size)]
    
    def parent_selection(self, population):
        population.sort(key=lambda x: x.fitness, reverse=True)
        return population[:self.parent_size]
    
    def calculate(self):
        population = self.generate_random_population()
        
        for _ in range(self.num_generations):
            parents = self.parent_selection(population)
            
        for curr in population:
            print("Populacija je:")
            print(curr.string)
            print(curr.fitness)

        print("Roditelji su:")
        print("-------------------------------------------")

        for curr in parents:    
            print(curr.string)
            print(curr.fitness)
              
        