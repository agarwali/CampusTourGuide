#-------------------------------------------------------------------------------------------
# Name:     read_graph.py
# Purpose:  Class to read files containing buildings, points, and side walks and distances 
# Programmers: Ishwar Agarwal(Driver) & Xhafer Rama(Navigator)
# Acknowledgement: None
# Created:     12/12/15
#-------------------------------------------------------------------------------------------

from Graph import *

class ReadMap(object):
    """This class reads a database file with .map extension
    
    Attributes:
        header: a list containing the header section of the file
        filename: The name of the database
        graph: a graph object generated after reading the file, initially empty
        names: a list that only consists of the names of the buildings in the map
    """

    def __init__(self):
        self.header = []
        self.filename = ''
        self.graph = Graph()
        self.names = []

    def read_file(self, filename):
        """Reads an ASCII file with .map extension to crate the map of campus
        
        Reads an An ASCII file where each line will be an edge. 
        The first column will contain a vertex, second column a vertex, and third column
        will contain distance of the edge. All the column separated by spaces.
        
        Update self.graph and self.names by extracting the edges from the file.
        """
        f = open(filename, 'r')
        for i in range(5):
            self.header.append(f.readline())    # reads and stores the header section of the file
        
        line = f.readline()
        while line != 'EOF':
            
            
            sp_line = line.split()  # split the first line by spaces
            v1 = Vertex(sp_line[0]) # create the first vertex obj from the first column
            v2 = Vertex(sp_line[1]) # create second vertex obj from secomd column
            newEdge = Edge(v1, v2)  # create and edge between those two edges
            
            if v1 not in self.graph.vertices(): # if v1 is not already added
                self.graph.add_vertex(v1)   # add that to the graph
                
                # the following block is trick used to extrach the names of the buildings
                # all the vertex labels other than name of buildings have been stored as numbers
                # so every vertex label is first tried to convert into number
                # if the label is not a number, it raises the exception, and we know
                # that it is the name of the buiding
                try:
                    a = int(v1.label)
                except:
                    self.names.append(v1.label)
            
            if v2 not in self.graph.vertices():
                self.graph.add_vertex(v2)
                try:
                    a = int(v2.label)
                except:
                    self.names.append(v2.label)
                    
            self.graph.add_edge(newEdge)    # add the edge to the graph
            newEdge.set_distance(int(sp_line[2]))   # set the distance of the edge
            line = f.readline()
            
        self.filename = filename    # updates the filename


