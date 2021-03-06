Purpose: The sole purpose of this project is to apply the TSP problem to find the best Hamiltotnian path for Berea College campus tour guides or visitors to generate tours for tourists with an option for selecting the buildings they want to visit at Berea College. We used the branch and bound algorithm to generate optimal solutions.

Instructions:
To open the application run main.py in a Python 2.7 environment.
Libraries used: Tkinter and Swampy

Developement:
main-development.py has been left for future development, that does not deal with GUI.

Files/Modules:
best_tour.py - contains the BestPath class and methods
read_graph.py - consists the ReadMap class and methods
Graph.py - contains Vertex, Edge, and Graph Classes and methods
GraphWorld.py - contains classes to draw graphs using swampy.Gui
GraphApp.py- contains the applcation for GUI for changing frames in Tkinter
Pages.py - contains all the frames to be raised in the application.
test.map - contains a small database of buildings, vertices, and the distance betweem them.
Stack.py - a stack object implemented using Python List
test.py - contains test suites (Not fully implemented yet).

Acknowledgements:
Graph and GraphWorld modules from Allen B. Downey were obtained for free from http://greenteapress.com/complexity.
Code for switching frame in GraphApp.py was obtained from http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
Code for printing selected items in tkinter Scrollbar in a text frame in Pages.py was obtained from http://stackoverflow.com/questions/13828531/problems-in-python-getting-multiple-selections-from-tkinter-listbox
Stack Class from David M. Reed and John Zelle was obtained from https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
