import numpy as np
import random

class BMDA:
    class Solution:
        def __init__(self, string, fitness) -> None:
            self.string = string
            self.fitness = fitness

    def __init__(self, fitness_function, num_generations, population_size, parent_size, offspring_size, max_string_size, min_string_size, alphabet, probability_vector, freq) -> None:
        self.num_generations = num_generations
        self.fitness_function = fitness_function
        self.offspring_size = offspring_size
        self.parent_size = parent_size
        self.population_size = population_size
        self.max_string_size = max_string_size
        self.min_string_size = min_string_size
        self.alphabet = alphabet
        self.probability_vector = probability_vector
        self.freq = freq
        self.probability_vector_array = np.empty((len(alphabet)+1, self.max_string_size, len(alphabet)))
        self.freq_array = np.empty((len(alphabet)+1, self.max_string_size, len(alphabet)))

    def generate_single_solution(self) -> Solution:
        # item_probability_vector neka bude matrica koja sadrzi u redovima poziciju u stringu, a u stupcima 
        # lokacija i,j govori kolika je vjerojatnost da se slovo i pojavi na mjestu j

        string = []
        string_size = random.randint(self.min_string_size,self.max_string_size)
        for i in range(string_size):
            #što ako se generira prvo slovo?
            if (i == 0):
                first_dimension = len(self.alphabet)
            else:
                first_dimension = self.alphabet.index(string[i-1])
            roulette_wheel = np.cumsum(
            self.probability_vector_array[first_dimension][i]
            )
            random_number = np.random.rand()
            for index, score in enumerate(roulette_wheel):
                if random_number <= score:
                    string.append(self.alphabet[index])
                    break
        return self.Solution(string, self.fitness_function(string))
    
    def update_frequences(self, parents):
        #što ako nema prethodnog slova?
        #uvedi varijablu first_dimension ili u slucaju prvog slova neka prethodno bude isto to
        for parent in parents:
            for position in range(len(parent.string)):
                if (position == 0):
                    first_dimension = len(self.alphabet)
                else:
                    first_dimension = self.alphabet.index(parent.string[position-1])
                self.freq_array[first_dimension][position][self.alphabet.index(parent.string[position])] += 1
                

    def update_probability_vector(self):
        #print("PROBABILITY IDE DO:")
        #print(self.max_string_size)
        for previous in range(len(self.alphabet)+1):
            for index in range(self.max_string_size):
                self.probability_vector_array[previous][index] = self.freq_array[previous][index] / np.sum(self.freq_array[previous][index])

    
    
    def generate_random_population(self):
        #stvaranje polja matrica vjerojatnosti i frekvencija
        for i in range (len(self.alphabet) + 1):
            self.probability_vector_array[i] = self.probability_vector
            self.freq_array[i] = self.freq
 
        return [self.generate_single_solution() for _ in range(self.population_size)]
    
    def parent_selection(self, population):
        population.sort(key=lambda x: x.fitness, reverse=True)
        return population[:self.parent_size]
    
    def generate_offspring(self):
        offspring = []
        for _ in range(self.offspring_size):
            new_individual = self.generate_single_solution()
            offspring.append(new_individual)
            

        return offspring
    
    def calculate(self):
        population = self.generate_random_population()
        best_results = []
        for _ in range(self.num_generations):
            parents = self.parent_selection(population)
            self.update_frequences(parents)
            self.update_probability_vector()
            # generate offspring (and new individual)
            offspring = self.generate_offspring()
            population += offspring
            population.sort(key=lambda x: x.fitness, reverse=True)
            population = population[:self.population_size]
            best_results.append(population[0])
            
            print("Populacija je:")
            for curr in population:
                print(curr.string)
                print(curr.fitness)

            print("-------------------------------------------")
            print("Roditelji su:")  

            for curr in parents:    
                print(curr.string)
                print(curr.fitness)
            
            print("Freq:")
            for matrix in self.freq_array:
                print(matrix)
            
            print("Probability_vector_array:")
            for matrix in self.probability_vector_array:
                print(matrix)
            print("-------------------------------------------")

            print("Potomstvo je:")
            for curr in offspring:
                print(curr.string)
                print(curr.fitness)
        
        print("-------------------------------------------")
        print("-------------------------------------------")

        print("NAJBOLJI REZULTATI:")
        for curr in best_results:
            print(curr.string)
            print(curr.fitness)

        return best_results


        