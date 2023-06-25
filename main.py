from umda import UMDA
from bmda import BMDA
import numpy as np
from matplotlib import pyplot as plt

NUM_GENERATIONS = 30
POPULATION_SIZE = 10 #400
OFFSPRING_SIZE = 4 #30
PARENT_SIZE = 3 #30
MAX_STRING_SIZE = 8
MIN_STRING_SIZE = 6
APLHABET = ["A", "R", "N", "D", "C"]
PROBABILITY_VECTOR = np.full((MAX_STRING_SIZE, len(APLHABET)), 1/len(APLHABET))
FREQ = np.full((MAX_STRING_SIZE, len(APLHABET)), 1)

""" NUM_GENERATIONS = 50
POPULATION_SIZE = 20 #400
OFFSPRING_SIZE = 10 #30
PARENT_SIZE = 4 #30
MAX_STRING_SIZE = 50
MIN_STRING_SIZE = 20
APLHABET = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
PROBABILITY_VECTOR = np.full((MAX_STRING_SIZE, len(APLHABET)), 1/len(APLHABET))
FREQ = np.full((MAX_STRING_SIZE, len(APLHABET)), 1) """

def fitness_function(string):
    zbroj = 0
    for znak in string:
        #zbroj += ord(znak)
        if(znak == 'A'):
            zbroj += 10
        elif(znak == 'R'):
            zbroj += 5
        elif(znak == 'N'):
            zbroj += 2
        elif(znak == 'D'):
            zbroj += 1
        else:
            zbroj += 0
    return zbroj

def plot_fitness(fitness_values, title):
    plt.figure()
    x = [i for i in range(NUM_GENERATIONS)]
    plt.title(title)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.plot(fitness_values)
    plt.show()

def main():
    global ITEMS
   # current_dir = os.path.dirname(__file__)
    
    """
    umda = UMDA(
        fitness_function,
        NUM_GENERATIONS,
        POPULATION_SIZE,
        PARENT_SIZE,
        OFFSPRING_SIZE,
        MAX_STRING_SIZE,
        MIN_STRING_SIZE,
        APLHABET,
        PROBABILITY_VECTOR,
        FREQ
    )

    #print(PROBABILITY_VECTOR)
    values_umda = umda.calculate()
    umda_plot = [(solution.fitness) for solution in values_umda]
    plot_fitness(umda_plot, "UMDA")
    """
    bmda = BMDA(
        fitness_function,
        NUM_GENERATIONS,
        POPULATION_SIZE,
        PARENT_SIZE,
        OFFSPRING_SIZE,
        MAX_STRING_SIZE,
        MIN_STRING_SIZE,
        APLHABET,
        PROBABILITY_VECTOR,
        FREQ
    )

    #print(PROBABILITY_VECTOR)
    values_bmda = bmda.calculate()
    bmda_plot = [(solution.fitness) for solution in values_bmda]
    plot_fitness(bmda_plot, "BMDA")


if __name__ == "__main__":
    main()