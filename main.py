from umda import UMDA
import numpy as np

NUM_GENERATIONS = 20
POPULATION_SIZE = 50 #400
OFFSPRING_SIZE = 10 #30
BAG_WEIGHT = 500 # 800
PARENT_SIZE = 10 #30
MAX_STRING_SIZE = 4
APLHABET = ["a", "b", "c", "d"]
PROBABILITY_VECTOR = np.full((4, 4), 0.25)

def main():
    global ITEMS
   # current_dir = os.path.dirname(__file__)
    

    umda = UMDA(
        fitness_function,
        NUM_GENERATIONS,
        POPULATION_SIZE,
        PARENT_SIZE,
        OFFSPRING_SIZE,
        MAX_STRING_SIZE,
        APLHABET
    )

    #print(PROBABILITY_VECTOR)
    umda.calculate(PROBABILITY_VECTOR)

def fitness_function():
    return

if __name__ == "__main__":
    main()