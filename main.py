import datetime as dt
import time

recipe_file = "recipe.txt"


def open_recipe():
    f = open(recipe_file, 'r')
    lines = f.readlines()
    for line in lines:
        print(line)
    f.close()
    return lines

def grower():
    """
    Reads a recipe and executes it. Recipe file should be formatted as follows:

    RECIPE: my recipe           # gives name to recipe and signals begin
    START: 22:06:2022 18:00:00  # start timestamp in dd:mm:yyyy hh:mm:ss format (24hr time)
    REPEAT: 12                  # repetition frequency in hours
    WATER: 1000                 # volume of water
    SOLUTE: 10,10,0,4,6,8,0,0   # volumes of solutes 0-7 in ml
    """
    recipe = open_recipe()


if __name__ == '__main__':
    print("Starting")
    open_recipe()
    print(dt.datetime.now())
