from best_tour import BestPath
from read_graph import ReadMap
from Graph import *
from GraphWorld import *

def main():
    read = ReadMap()
    read.read_file('test.map')
    print read.names
    grapher = BestPath(read.names[:5])
    grapher.set_map(read.graph)
    bestTour = grapher.genrate_actualtour(Vertex(read.names[4]))
    print bestTour
    newGraph = Graph(bestTour.items)
    for i in range(len(bestTour.items)-1):
        newEdge = Edge(bestTour.items[i], bestTour.items[i+1])
        newGraph.add_edge(newEdge)
    layout = RandomLayout(newGraph)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(newGraph, layout)
    gw.mainloop()


main()