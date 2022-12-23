# Project uses a Genetic Algorithm to optimize a given function with (x, y, z) variables to 0

import random
import simpleeval
from simpleeval import SimpleEval

simpleeval.POWER_MAX = 8000000  # Allows slightly more computing intense operations to be used


def inputFunction():
    global string
    return string


s = SimpleEval()
invalidCharacters = "abcdefghijklmnopqrstuvw!@#$&|\\\"][{}';:.,<>?`~="
def fitness(x, y, z):
    try:
        function = inputFunction()
        if invalidCharacters in function:
            return "Invalid characters found in input"
        if "x" not in function or "y" not in function or "z" not in function:
            return "Please enter all three variables (x, y, z)"
        function = function.replace("x", f"{x}")
        function = function.replace("y", f"{y}")
        function = function.replace("z", f"{z}")
        result = s.eval(function)
    except SyntaxError:
        return "Invalid syntax"

    if result == 0:
        return 100000
    else:
        return abs(1 / result)  # Increases as the result is closer to 0


def firstSolutions():
    # Generates random numbers for first generation
    sols = []
    for i in range(100):  # 100 pseudo-randomized solutions
        sols.append((random.uniform(-10, 500),
                     random.uniform(-10, 500),
                     random.uniform(-10, 500)))
    return sols


def geneticAlgo(inputFunc):
    global string
    string = inputFunc

    sols = firstSolutions()

    for i in range(10000):  # Up to 10,000 generations
        sortedSols = []
        for sol in sols:
            sortedSols.append((fitness(sol[0], sol[1], sol[2]), sol))
        sortedSols.sort()
        sortedSols.reverse()

        topSols = sortedSols[:3]  # Holds top 3 solutions with highest fitness

        bestFitness = sortedSols[0][0]
        bestAns = sortedSols[0][1]

        if bestFitness > 7250:
            print(f"\nFinal solution found in {i} generations.\n\n"
                  f"The solutions fitness: {bestFitness:.0f}.\n"
                  f"Solution: ({bestAns[0]:.3f}, {bestAns[1]:.3f}, {bestAns[2]:.3f})")
            return f"({bestAns[0]:.1f}, {bestAns[1]:.1f}, {bestAns[2]:.1f})"

        print(f"=== Gen {i}'s best solution ===\nFitness: {bestFitness:.0f}\n Solution: ({bestAns[0]:.4f}, {bestAns[1]:.4f}, {bestAns[2]:.4f})\n")

        newGeneration = []

        for n in range(3):  # New generation has a population of 3 with mutation rate of 20%...
            x = topSols[0][1][0] * random.uniform(0.90, 1.10)  # Mutation rate of 20%
            y = topSols[0][1][1] * random.uniform(0.90, 1.10)
            z = topSols[0][1][2] * random.uniform(0.90, 1.10)

            newGeneration.append((x, y, z))

        for n in range(97):  # ... and a population of 97 with mutation rate of 2%
            x = topSols[0][1][0] * random.uniform(0.99, 1.01)  # Mutation rate of 2%
            y = topSols[0][1][1] * random.uniform(0.99, 1.01)
            z = topSols[0][1][2] * random.uniform(0.99, 1.01)

            newGeneration.append((x, y, z))

        # Uses "elitism", where the highest fitness solution is passed directly onto the next generation
        # This makes sure that fitness only increases and never decreases over generations
        newGeneration.append(bestAns)

        sols = newGeneration