import math
import graph
#from graph import tourValue()

g1 = graph.Graph(-1,"cities25")
g2 = graph.Graph(-1, "cities50")
g3 = graph.Graph(-1,"cities75")
g4 = graph.Graph(2,"sixnodes")
#g2.swapHeuristic()
#g2.TwoOptHeuristic()
#g2.Greedy()
g3.createRoute()
g3.TwoOptHeuristic()
g3.swapHeuristic()
print(g3.tourValue())

