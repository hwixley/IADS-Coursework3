import random

import graph


# PART D - Experiments

# Creates a random Euclidean graph based on the input parameters
# (size = # of nodes, lowerX = lower bound of X values, upperX = upper bound of X values, ...and likewise for Y)
# This graph is then outputted into a text file so it can be parsed by our algorithms.
def createRandomEuclideanGraph(size, lowerX, upperX, lowerY, upperY):
    for a in range(10):
        try:
            with open("randomEuclidGraph" + str(a) + "_size" + str(size) + ".txt", "x") as file:
                for i in range(size):
                    randX = random.randint(lowerX, upperX)
                    randY = random.randint(lowerY, upperY)
                    spacesX = ""
                    spacesY = ""
                    if randX < 10:
                        spacesX = "  "
                    elif randX < 100:
                        spacesX = " "
                    if randY < 10:
                        spacesY = "  "
                    elif randY < 100:
                        spacesY = " "
                    strN = "\n"
                    if i == size - 1:
                        strN = ""

                    file.write(" " + spacesX + str(randX) + "  " + spacesY + str(randY) + strN)
                print("Random Euclidean graph created successfully. Filename: " + "randomEuclidGraph" + str(a) + "_size"
                      + str(size) + ".txt")
                break
        except IOError:
            if a == 9:
                print("All allowed file names are taken for graphs with size " + str(size))


# Creates a random Metric graph based on the input parameters
# (size = # of nodes, lowerEdge = lower bound of edge costs, upperEdge = upper bound of edge costs)
# This graph is then outputted into a text file so it can be parsed by our algorithms.
def createRandomMetricGraph(size, lowerEdge, upperEdge):
    for a in range(10):
        try:
            with open("randomMetricGraph" + str(a) + "_size" + str(size) + ".txt", "x") as file:
                nodes = []
                for i in range(size):
                    nodes.append(i)

                for n in nodes:
                    strN = "\n"
                    if n == size - 1:
                        strN = ""

                    for k in range(n + 1, size):
                        rand = random.randint(lowerEdge, upperEdge)

                        file.write(str(n) + " " + str(k) + " " + str(rand) + strN)
                print("Random Metric graph created successfully. Filename: " + "randomMetricGraph" + str(a) + "_size" +
                      str(size) + ".txt")
                break
        except IOError:
            if a == 9:
                print("All allowed file names are taken for graphs with size " + str(size))


g1 = graph.Graph(-1, "cities25")
g2 = graph.Graph(-1, "cities50")
g3 = graph.Graph(-1, "cities75")
g4 = graph.Graph(2, "sixnodes")

g3.createRoute()
g3.TwoOptHeuristic()
g3.swapHeuristic()
print(g3.tourValue())
print("\n")

# PART D: testing with randomly created graphs
# createRandomMetricGraph(10, 1, 7)
# createRandomEuclideanGraph(30, 11, 456, 34, 782)

g5 = graph.Graph(-1, "randomEuclidGraph0_size30.txt")
g6 = graph.Graph(2, "randomMetricGraph0_size10.txt")

g5.createRoute()
print(g5.tourValue())
g5.Greedy()
print(g5.tourValue())

g6.createRoute()
print(g6.tourValue())
g6.Greedy()
print(g6.tourValue())
