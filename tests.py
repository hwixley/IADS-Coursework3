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

# For every implemented algorithm it calculates their respective average tourValues for an input amount of randomly
# generated Metric and Euclidean graphs.
# It creates these random graphs in the form of text files, and after initialization are deleted for the sake of being
# able to iterate this method repeatedly with a high number of tests without filling up the disk.
# (sizeEuclid = # nodes for Euclidean graph, this also is used to determine the upper bounds)
# (sizeMetric = # nodes for Metric graph, this also is used to determine the upper bounds)
# (numTests = # random graphs to generate)
def calculateCostDiffs(sizeEuclid, sizeMetric, numTests):
    # Initializations of all relevant tourValue lists.
    toursET, toursET_s, toursET_t, toursET_st = ([],) * 4   # tourValues of Euclidean Graphs w/ Temperate, Swap & 2-Opt
    toursEG, toursEG_s, toursEG_t, toursEG_st = ([],) * 4   # tourValues of Euclidean Graphs w/ Greedy, Swap & 2-Opt
    toursMT, toursMT_s, toursMT_t, toursMT_st = ([],) * 4   # tourValues of Metric Graphs w/ Temperate, Swap & 2-Opt
    toursMG, toursMG_s, toursMG_t, toursMG_st = ([],) * 4   # tourValues of Metric Graphs w/ Greedy, Swap & 2-Opt
    standardE, standardM = ([],) * 2    # ID tourValues of Euclidean/Metric graphs
    swapE, swapM = ([],) * 2    # Swap tourValues of Euclidean/Metric graphs
    topE, topM = ([],) * 2  # 2-Opt tourValues of Euclidean/Metric graphs
    stE, stM = ([],) * 2    # Swap & 2-Opt tourValues of Euclidean/Metric graphs
    last = -1

    # Max allowed value of parameter sizeMetric is 10, this is because our initialization for Metric graphs in the graph
    # class only accounts for single digit nodes and edge costs.
    if sizeMetric > 10:
        print("INPUT ERROR: 10 is the maximum Metric graph size allowed, so input has been set to default(10).\n")
        sizeMetric = 10

    print("Function calculateCostDiffs initialized with " + str(numTests) + " graphs to generate and test:")
    for i in range(numTests):
        # Initializations of the random graphs for a given test iteration
        createRandomMetricGraph(sizeMetric, 1, sizeMetric - int(sizeMetric / 4), numTests)
        createRandomEuclideanGraph(sizeEuclid, 10, sizeEuclid * 10, 10, sizeEuclid * 10, numTests)

        # Parsing the given Euclidean/Metric graph textfile representation into a class instance
        ge = graph.Graph(-1, path + "randomEuclidGraph" + str(i) + "_size" + str(sizeEuclid) + ".txt")
        gm = graph.Graph(2, path + "randomMetricGraph" + str(i) + "_size" + str(sizeMetric) + ".txt")

        # Class variables used to denote whether a search is being done on a random graph (to prevent infinite loops).
        ge.costDiffs = 1
        gm.costDiffs = 1

        # EUCLIDEAN GRAPH: ID, SWAP, & 2-OPT TOURVALUES
        ge1 = ge
        standardE.append(ge.tourValue())
        ge.swapHeuristic()
        swapE.append(ge.tourValue())
        ge1.indexTwoOP = 0
        ge1.TwoOptHeuristic()
        topE.append(ge1.tourValue())
        ge.indexTwoOP = 0
        ge.TwoOptHeuristic()
        stE.append(ge.tourValue())

        # EUCLIDEAN GRAPH: GREEDY TOURVALUES
        ge.Greedy()
        ge2 = ge
        toursEG.append(ge.tourValue())
        ge.swapHeuristic()
        toursEG_s.append(ge.tourValue())
        ge2.indexTwoOP = 0
        ge2.TwoOptHeuristic()
        toursEG_t.append(ge2.tourValue())
        ge.indexTwoOP = 0
        ge.TwoOptHeuristic()
        toursEG_st.append(ge.tourValue())

        # EUCLIDEAN GRAPH: TEMPERATE TOURVALUES
        ge.createRoute()
        ge2 = ge
        toursET.append(ge.tourValue())
        ge.swapHeuristic()
        toursET_s.append(ge.tourValue())
        ge2.indexTwoOP = 0
        ge2.TwoOptHeuristic()
        toursET_t.append(ge2.tourValue())
        ge.indexTwoOP = 0
        ge.TwoOptHeuristic()
        toursET_st.append(ge.tourValue())

        # METRIC GRAPH: ID, SWAP, & 2-OPT TOURVALUES
        gm1 = gm
        standardM.append(gm.tourValue())
        gm.swapHeuristic()
        swapM.append(gm.tourValue())
        gm1.indexTwoOP = 0
        gm1.TwoOptHeuristic()
        topM.append(gm1.tourValue())
        gm.indexTwoOP = 0
        gm.TwoOptHeuristic()
        stM.append(gm.tourValue())

        # METRIC GRAPH: GREEDY TOURVALUES
        gm.Greedy()
        gm2 = gm
        toursMG.append(gm.tourValue())
        gm.swapHeuristic()
        toursMG_s.append(gm.tourValue())
        gm2.indexTwoOP = 0
        gm2.TwoOptHeuristic()
        toursMG_t.append(gm2.tourValue())
        gm.indexTwoOP = 0
        gm.TwoOptHeuristic()
        toursMG_st.append(gm.tourValue())

        # METRIC GRAPH: TEMPERATE TOURVALUES
        gm.createRoute()
        gm2 = gm
        toursMT.append(gm.tourValue())
        gm.swapHeuristic()
        toursMT_s.append(gm.tourValue())
        gm2.indexTwoOP = 0
        gm2.TwoOptHeuristic()
        toursMT_t.append(gm2.tourValue())
        gm.indexTwoOP = 0
        gm.TwoOptHeuristic()
        toursMT_st.append(gm.tourValue())

        # Output used to represent the progress of calculateCostDiffs() particularly useful for large scale tests.
        new = int(((i + 1) / numTests) * 100)
        if new != last:
            print(str(int(((i + 1) / numTests) * 100)) + " % of tests complete.")
        last = new

    # Loop which deletes all randomly generated text file graphs, so calculateCostDiffs can be repeated with ease.
    for a in range(numTests):
        os.remove(path + "randomEuclidGraph" + str(a) + "_size" + str(sizeEuclid) + ".txt")
        os.remove(path + "randomMetricGraph" + str(a) + "_size" + str(sizeMetric) + ".txt")

    # Printing all outputs
    print("\nAfter generating " + str(numTests) + " random Metric (size " + str(
        sizeMetric) + ") & Euclidean (size " + str(sizeEuclid) + ") "
          + "graphs, the averages are:")
    print("-------------------------------------------------------------------------")

    # Euclidean graph stats.
    print("EUCLIDEAN:")
    print("Identity = " + str(int(sum(standardE) / len(standardE))) + " ,  Swap = " + str(int(sum(swapE) / len(swapE)))
          + " ,  2-Op = " + str(int(sum(topE) / len(topE))) + " ,  Swap & 2-Opt = " + str(int(sum(stE) / len(stE))))
    print("Temperate = " + str(int(sum(toursET) / len(toursET))) + " ,  Greedy = " +
          str(int(sum(toursEG) / len(toursEG))))
    print("Temperate w/ Swap = " + str(int(sum(toursET_s) / len(toursET_s))) + " ,  Greedy w/ Swap = " +
          str(int(sum(toursEG_s) / len(toursEG_s))))
    print("Temperate w/ 2-Opt = " + str(int(sum(toursET_t) / len(toursET_t))) + " ,  Greedy w/ 2-Opt = " +
          str(int(sum(toursEG_t) / len(toursEG_t))))
    print(
        "Temperate w/ Swap & 2-Opt = " + str(int(sum(toursET_st) / len(toursET_st))) + ",  Greedy w/ Swap & 2-Opt = " +
        str(int(sum(toursEG_st) / len(toursEG_st))) + "\n")

    # Metric graph stats.
    print("METRIC:")
    print("Identity = " + str(int(sum(standardM) / len(standardM))) + " ,  Swap = " + str(int(sum(swapM) / len(swapM)))
          + " ,  2-Op = " + str(int(sum(topM) / len(topM))) + " ,  Swap & 2-Opt = " + str(int(sum(stM) / len(stM))))
    print("Temperate = " + str(int(sum(toursMT) / len(toursMT))) + " ,  Greedy = " +
          str(int(sum(toursMG) / len(toursMG))))
    print("Temperate w/ Swap = " + str(int(sum(toursMT_s) / len(toursMT_s))) + " ,  Greedy w/ Swap = " +
          str(int(sum(toursMG_s) / len(toursMG_s))))
    print("Temperate w/ 2-Opt = " + str(int(sum(toursMT_t) / len(toursMT_t))) + " ,  Greedy w/ 2-Opt = " +
          str(int(sum(toursMG_t) / len(toursMG_t))))
    print(
        "Temperate w/ Swap & 2-Opt = " + str(int(sum(toursMT_st) / len(toursMT_st))) + ",  Greedy w/ Swap & 2-Opt = " +
        str(int(sum(toursMG_st) / len(toursMG_st))) + "\n")


# PART A -> C
# Default project graph initializations
g1 = graph.Graph(-1, "cities25")
g2 = graph.Graph(-1, "cities50")
g3 = graph.Graph(-1, "cities75")
g4 = graph.Graph(2, "sixnodes")

# Custom algorithm implemented against g3, with Swap and 2-Op refinement algorithms.
g3.createRoute()
g3.swapHeuristic()
g3.TwoOptHeuristic()
print(g3.tourValue())
print("\n")

# PART D
# Testing algorithm efficiency of Greedy VS my custom algorithm 'Temperate'
# INPUTS: size Euclid graph = 60, size Metric graph = 10, # of randomly generated graphs to test = 500.
calculateCostDiffs(25, 4, 100)
