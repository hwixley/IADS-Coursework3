import random

import graph


# PART D - Experiments

# Creates a random graph based on the input parameters
# (size = # of nodes, lowerX = lower bound of X values, upperX = upper bound of X values, ...and likewise for Y)
# This graph is then outputted into a text file so it can be parsed by our algorithms.
def createRandomGraph(size, lowerX, upperX, lowerY, upperY):
    fileID = random.randint(0, 100)

    for a in range(10):
        try:
            with open("randomGraph" + str(a) + "_size" + str(size) + ".txt", "x") as file:
                for i in range(size):
                    randX = random.randint(lowerX, upperX)
                    randY = random.randint(lowerY, upperY)
                    strX = ""
                    strY = ""
                    if randX < 10:
                        strX = "  "
                    elif randX < 100:
                        strX = " "
                    if randY < 10:
                        strY = "  "
                    elif randY < 100:
                        strY = " "

                    file.write(" " + strX + str(randX) + "  " + strY + str(randY) + "\n")
                print("Random graph created succesfully. Filename: " + "randomGraph" + str(a) + "_size" + str(size) + ".txt")
                break
        except IOError:
            if a == 9:
                print("All allowed file names are taken for graphs with size " + str(size))


createRandomGraph(30, 11, 456, 34, 782)
g1 = graph.Graph(-1, "cities25")
g2 = graph.Graph(-1, "cities50")
g3 = graph.Graph(-1, "cities75")
g4 = graph.Graph(2, "sixnodes")
g5 = graph.Graph(-1, "randomGraph0_size30.txt")

g3.createRoute()
g3.TwoOptHeuristic()
g3.swapHeuristic()
print(g3.tourValue())

g5.createRoute()
print(g5.tourValue())
