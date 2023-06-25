import numpy as np
import random


class UMDA:

    class Solution:
        def __init__(self, string, fitness) -> None:
            self.string = string
            self.fitness = fitness

    def __init__(self, fitness_evaluator, num_generations, population_size, parent_size, offspring_size, max_string_size, min_string_size, alphabet, probability_vector, freq) -> None:
        self.fitness_evaluator = fitness_evaluator
        self.num_generations = num_generations
        self.offspring_size = offspring_size
        self.parent_size = parent_size
        self.population_size = population_size
        self.max_string_size = max_string_size
        self.min_string_size = min_string_size
        self.alphabet = alphabet
        self.probability_vector = probability_vector
        self.freq = freq



    def generate_single_solution(self) -> Solution:
        # item_probability_vector neka bude matrica koja sadrzi u redovima poziciju u stringu, a u stupcima 
        # lokacija i,j govori kolika je vjerojatnost da se slovo i pojavi na mjestu j

        string = []
        string_size = random.randint(self.min_string_size,self.max_string_size)
        for i in range(string_size):
            roulette_wheel = np.cumsum(
            self.probability_vector[i]
            )
            random_number = np.random.rand()
            for index, score in enumerate(roulette_wheel):
                if random_number <= score:
                    string.append(self.alphabet[index])
                    break
        #promjena returna
        return self.Solution(string, 0)
    
    def update_frequences(self, parents):
        for parent in parents:
            for position in range(len(parent.string)):
                self.freq[position][self.alphabet.index(parent.string[position])] += 1

    def update_fitness(self, population):
        
        population_concat = []
        # [['A', 'B', 'C'], ['A', 'B', 'C']]...
        for pop in population:
            population_concat.append(''.join(pop.string))
            #print(''.join(pop.string))
        # ['ABC', 'ABC']...
        population_fitness = self.fitness_evaluator.predict(population_concat)

        for i in range(len(population)):
            population[i].fitness = population_fitness[i]

            #print(population[i].fitness + "  -  " + population_fitness[i])

        return population


        

    def update_probability_vector(self):
        #print("PROBABILITY IDE DO:")
        #print(self.max_string_size)
        for index in range(self.max_string_size):
            self.probability_vector[index] = self.freq[index] / np.sum(self.freq[index])

    
    
    def generate_random_population(self):
 
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
        population = self.update_fitness(population)
        best_results = []
        for _ in range(self.num_generations):
            parents = self.parent_selection(population)
            self.update_frequences(parents)
            self.update_probability_vector()
            # generate offspring (and new individual)
            offspring = self.generate_offspring()
            offspring = self.update_fitness(offspring)

            population += offspring
            population.sort(key=lambda x: x.fitness, reverse=True)
            population = population[:self.population_size]
            best_results.append(population[0])
            """
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
            print(self.freq)
            
            print("Probability_vector:")
            print(self.probability_vector)
            print("-------------------------------------------")

            print("Potomstvo je:")
            for curr in offspring:
                print(curr.string)
                print(curr.fitness)"""
        
        #print("-------------------------------------------")
        #print("-------------------------------------------")

        #print("NAJBOLJI REZULTATI:")
        #for curr in best_results:
            #print(curr.string)
            #print(curr.fitness)


        print("-------------------------------------------")
        print("Probability_vector:")
        print(self.probability_vector)
        print("-------------------------------------------")

        return best_results


        