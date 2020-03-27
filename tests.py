import random
import graph
import os

path = "./randomGraphs/"


# PART D - Experiments

# Creates a random Euclidean graph based on the input parameters
# (size = # of nodes, lowerX = lower bound of X values, upperX = upper bound of X values, ...and likewise for Y)
# This graph is then outputted into a text file so it can be parsed by our algorithms.
def createRandomEuclideanGraph(size, lowerX, upperX, lowerY, upperY, numTests):
    for a in range(numTests):
        try:
            with open(path + "randomEuclidGraph" + str(a) + "_size" + str(size) + ".txt", "x") as file:
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
                break
        except IOError:
            if a == numTests - 1:
                print("All allowed file names are taken for graphs with size " + str(size))


# Creates a random Metric graph based on the input parameters
# (size = # of nodes, lowerEdge = lower bound of edge costs, upperEdge = upper bound of edge costs)
# This graph is then outputted into a text file so it can be parsed by our algorithms.
def createRandomMetricGraph(size, lowerEdge, upperEdge, numTests):
    for a in range(numTests):
        try:
            with open(path + "randomMetricGraph" + str(a) + "_size" + str(size) + ".txt", "x") as file:
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
                break
        except IOError:
            if a == numTests - 1:
                print("All allowed file names are taken for graphs with size " + str(size))


# PART D: testing with randomly created graphs

# Calculates mean % cost differences between my algorithm and that of greedy, for 4 Metric and Euclidean graphs.
# It creates these random graphs in the form of text files, and after initialization are deleted for the sake of being
# able to iterate this method repeatedly with a high number of tests without filling up the disk.
# (sizeEuclid = # nodes for Euclidean graph, this also is used to determine the upper bounds)
# (sizeMetric = # nodes for Metric graph, this also is used to determine the upper bounds)
def calculateCostDiffs(sizeEuclid, sizeMetric, numTests):
    costDiffsEUCLID = []  # List of % cost differences between my custom algorithm and greedy for Euclidean graphs
    costDiffsMETRIC = []  # List of % cost differences between my custom algorithm and greedy for Metric graphs

    if sizeMetric > 10:
        print("INPUT ERROR: 10 is the maximum Metric graph size allowed, so input has been set to default(10).\n")
        sizeMetric = 10

    print("Function calculateCostDiffs initialized with " + str(numTests) + " graphs to generate and test:")
    for i in range(numTests):
        createRandomMetricGraph(sizeMetric, 1, int(sizeMetric / 2), numTests)
        createRandomEuclideanGraph(sizeEuclid, 10, sizeEuclid * 10, 10, sizeEuclid * 10, numTests)

        g1 = graph.Graph(-1, path + "randomEuclidGraph" + str(i) + "_size" + str(sizeEuclid) + ".txt")
        g2 = graph.Graph(2, path + "randomMetricGraph" + str(i) + "_size" + str(sizeMetric) + ".txt")

        #   We must use different variables for each algorithm graph input
        g1_1 = g1
        g1_2 = g1
        g2_1 = g2
        g2_2 = g2

        g1_1.createRoute()
        customVal = g1_1.tourValue()
        g1_2.Greedy()
        greedyVal = g1_2.tourValue()

        costDiff = ((customVal / greedyVal) - 1) * 100
        costDiffsEUCLID.append(costDiff)

        g2_1.createRoute()
        customVal = g2_1.tourValue()
        g2_2.Greedy()
        greedyVal = g2_2.tourValue()

        costDiff = ((customVal / greedyVal) - 1) * 100
        costDiffsMETRIC.append(costDiff)

        print(str(round(((i + 1) / numTests)*100, 2)) + " % of tests complete.")

    for a in range(
            numTests):  # Loop which deletes all randomly generated text file graphs, so this method can be repeated.
        os.remove(path + "randomEuclidGraph" + str(a) + "_size" + str(sizeEuclid) + ".txt")
        os.remove(path + "randomMetricGraph" + str(a) + "_size" + str(sizeMetric) + ".txt")

    print("\nAfter generating " + str(numTests) + " random Metric (size " + str(
        sizeMetric) + ") & Euclidean (size " + str(sizeEuclid) + ") "
          + "graphs:")

    meanDiffEUCLID = round(sum(costDiffsEUCLID) / len(costDiffsEUCLID), 2)
    if meanDiffEUCLID < 0:
        sign = "lower"
        coeff = -1
    else:
        sign = "higher"
        coeff = 1
    print("My custom algorithm has on average a " + str(
        coeff * meanDiffEUCLID) + " % " + sign + " cost to that of greedy for Euclidean "
                                                 "graphs.")

    meanDiffMETRIC = round(sum(costDiffsMETRIC) / len(costDiffsMETRIC), 2)
    if meanDiffMETRIC < 0:
        sign = "lower"
    else:
        sign = "higher"
    print("My custom algorithm has on average a " + str(
        meanDiffMETRIC) + " % " + sign + " cost to that of greedy for Metric graphs.")


# Default project graph initializations
g1 = graph.Graph(-1, "cities25")
g2 = graph.Graph(-1, "cities50")
g3 = graph.Graph(-1, "cities75")
g4 = graph.Graph(2, "sixnodes")

# Custom algorithm implemented against g3, with 2-Op and Swap refinement algorithms.
g3.createRoute()
g3.TwoOptHeuristic()
g3.swapHeuristic()
print(g3.tourValue())
print("\n")

# Testing algorithm efficiency of Greedy VS my custom algorithm 'Temperate'
# INPUTS: size Euclid graph = 60, size Metric graph = 10, # of randomly generated graphs to test = 500.
calculateCostDiffs(60, 10, 500)
