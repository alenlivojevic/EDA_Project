from umda import UMDA
import numpy as np

NUM_GENERATIONS = 5
POPULATION_SIZE = 4 #400
OFFSPRING_SIZE = 5 #30
BAG_WEIGHT = 500 # 800
PARENT_SIZE = 2 #30
MAX_STRING_SIZE = 4
APLHABET = ["a", "b", "c", "d"]
PROBABILITY_VECTOR = np.full((MAX_STRING_SIZE, len(APLHABET)), 1/len(APLHABET))
""" PROBABILITY_VECTOR = [[1, 0, 0, 0],
                      [0.25, 0.25, 0.25, 0.25],
                      [0.25, 0.25, 0.25, 0.25],
                      [0.25, 0.25, 0.25, 0.25]] """
FREQ = np.full((MAX_STRING_SIZE, len(APLHABET)), 1)

def fitness_function(string):
    zbroj = 0
    for znak in string:
        #zbroj += ord(znak)
        if(znak == 'a'):
            zbroj += 10
        elif(znak == 'b'):
            zbroj += 5
        elif(znak == 'c'):
            zbroj += 2
        elif(znak == 'd'):
            zbroj += 1
    return zbroj

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
        APLHABET,
        PROBABILITY_VECTOR,
        FREQ
    )

    #print(PROBABILITY_VECTOR)
    umda.calculate()


if __name__ == "__main__":
    main()