# ---------------------------------------------------------------------------------------------------------------
# File Name: best_tour.py
# Purpose: It contains the best_tour class that controls generating the best path
# Author: Ishwar Agarwal & Xhafer Rama
# Last Date Modified: 12/12/2015
# Acknowledgements:
# ----------------------------------------------------------------------------------------------------------------

from Graph import *
from Stack import Stack
import copy

class BestPath(object):
    """Generates the best Hamiltonian Path froma connected graph.
    
    This class generates a best Hamiltonian path for a Travelling Sales Person
    Problem form a connected graph for a given set of vertices that the traveller
    wants to visit only.

    Attributes:
        currentTour: A stack that records the current tour
        bestTour: A stack taht records the best tour
        currentCost: Cost of the current tour
        bestCost: Cost of the best tour. Inititally set to a very large number.
        interestCities: A list of citites that the traveller is interested to visit
        _map: A map of the city containing all the vertices and edges
        _visitedPoints: this contains all the points visited so far
        _visitedCitites: this contians all the interest cities visited so far
    """
    
    def __init__(self, cities=[]):
        self.currentTour = Stack()
        self.bestTour = Stack()
        self.currentCost = 0
        self.bestCost = 10000000000000000000000000000000
        self.interestCities = [Vertex(city) for city in cities]
        self._map = Graph()
        self._visitedPoints = []
        self._visitedCities = []

    def set_map(self, pmap):
        """Sets the passed map to the instance variable _map
        """
        self._map = pmap

    def mark_visit(self, city):
        """Marks the passed city visited by putting it in the _visitedCities 
        and/or _visitedPoints list. City should be a vertex objcet.
        """
        if city in self.interestCities: # if the city is an interest city
            self._visitedCities.append(city)    # add city to visitesCitites
            self._visitedPoints.append(city)    # add city to visitedPoints
        else:
            self._visitedPoints.append(city)    # only add to visitedPoints
        
        
    def mark_unvisit(self, city):
        """
        Marks the passed city unvisited by removing it from the _visitedCities 
        and/or _visitedPoints list. City should be a vertex objcet.
        """    
        if city in self.interestCities: # if the city is an interest city
            self._visitedCities.remove(city)
            self._visitedPoints.remove(city)
        else:
            self._visitedPoints.remove(city)
    
    def all_visited(self):
        """Returns a True bool type if all the interest cities have been visited
        """
        # if the length of interest cities list and visited cities lists are equal
        if len(self.interestCities) == len(self._visitedCities):
            return True
        else:
            return False
    
    def next_cities(self):
        """
        It generates a list of points that have not been visited that we may
        potentially want to visit
        """
        # sets the current city as the top item on currentTour stack
        currentCity = self.currentTour.top() 
        # calls Graph Class's out vertices method to get all the vertices out of currentCity in the map
        possibleMoves =  self._map.out_vertices(currentCity)    
        
        # The following line returns a list of points that we can visit next
        # that has not already been visited yet in the currentTour
        return [move for move in possibleMoves if move not in self._visitedPoints]

                
    def move_branch(self, currentCity):
        """This method generates a bestTour by starting at currentCity and explores
        all the possible vertices until it reaches a dead_end or all the interestCities
        have been visited.
        
        It does that by recursively exploring all possibilities but has a bounding algorithm
        that causes it to prune.
        """
        # base case
        if self.dead_end() or self.all_visited():
            if self.all_visited():
                if self.currentCost < self.bestCost:
                    self.bestCost = self.currentCost
                    self.bestTour = Stack() # reset bestTour stack
                    for i in self.currentTour.items[::-1]:  # add all the items in currentTour to bestTour
                        self.bestTour.push(i)

            return
        
        # recursive call
        else:
            for move in self.next_cities(): # for each available moves
                self.mark_visit(move)   # first mark it visited
                newEdge = self._map.get_edge(currentCity, move) # create an edge from the last city to the new one
                self.currentCost += newEdge.get_distance()  # add the tour cost of this new city
                self.currentTour.push(move) # add the new city to currentTour
                self.move_branch(move)  # call the function again with this new city
                
                # The following part of the code is executed during backtracking
                self.currentTour.pop()  # pop the last item in the list
                self.currentCost -= newEdge.get_distance()  # remove that from the tour cost
                self.mark_unvisit(move) # mark it unvitied
            return
                
    def genrate_actualtour(self, StartCity):
        """
        This method generates the graph of the bestTour. 
        
        It calls the move_branch method with a given StartCity. From the bestTour
        stack it filters out only the interestCities by leaving out all the 
        intersection points. It then creates an instance of graph class in the same
        order as in bestTour.
        """
        tour = Stack()  # create a new stack
        
        self.currentTour.push(StartCity)    # push the startCity in currentTour stack
        self.mark_visit(StartCity)  # mark it visited
        self.move_branch(StartCity) # call move_branch recursive function, with the given city
        
        # The following block of code removes vertices from bestTour and filters out
        # only the interest points and adds it to tour Stack
        while self.bestTour.size() != 0:    
            city = self.bestTour.pop()
            if city in self.interestCities:
                tour.push(city)
                
        # The following block of code generates a Graph object from the tour Stack
        newGraph = Graph(tour.items)    # adds only the vertices in the graph
        for i in range(len(tour.items)-1):
            newEdge = Edge(tour.items[i], tour.items[i+1])  # create an edge within two consecutive vertices
            newGraph.add_edge(newEdge)  # add the edge to the graph
        return newGraph
        
    def dead_end(self):
        """
        If there are no other options left to move it returns True otherwise it
        returns False. 
        """
        if self.next_cities() == []:    # if the returned list from next_citites method is empty
            return True
        else:
            return False    