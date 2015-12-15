# -------------------------------------------------------------------------------------------------------------------
# File Name: Pages.py
# Purpose: It contains the page classes that are essentially frames to change the window
#           controlled by the TicApp Class in the module TicTacToeApp.py
# Author: Ishwar Agarwal
# Last Date Modified: 12/15/2015
# Acknowledgements: * Ishwar Agarwal for the structure of Code for creating pages using Frames
#                     https://github.com/agarwali/
#                   * The code(line 113-138) for updating a list from a Tkinter selection box 
#                     was obtained from an answer in StackOverflow
# http://stackoverflow.com/questions/13828531/problems-in-python-getting-multiple-selections-from-tkinter-listbox
# --------------------------------------------------------------------------------------------------------------------

from Tkinter import *
from tkFont import Font
from best_tour import BestPath
from read_graph import ReadMap
from Graph import *
from GraphWorld import *

# the following set of text attributes are created to be reused
# throughout different pages
TITLE_FONT = ("Helvetica", 18, "bold")
SUB_TITLE_FONT = ("Helvetica", 8)
BIG_BUTTON_FONT = ("Helvetica", 12)
X_O_FONT = ("Helvetica", 32)


class StartPage(Frame):
    """Contains everything to be shown on start page
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="Tour Generator", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=0)
        label = Label(self, text="The shortest tour.", font=SUB_TITLE_FONT)
        label.pack(side="top", fill="x", pady=5)
        label = Label(self, text="", font=SUB_TITLE_FONT)
        label.pack(side="top", fill="x", pady=20)

        button1 = Button(self, text="Start", width=20, height=2, font=BIG_BUTTON_FONT,
                         command=lambda: controller.show_frame(Selection))
        button2 = Button(self, text="Instructions", width=20, height=2, font=BIG_BUTTON_FONT,
                         command=lambda: controller.show_frame(Instructions))
        button3 = Button(self, text="Quit", width=20, height=2, font=BIG_BUTTON_FONT,
                         command=lambda: self.close_window())
        button1.pack()
        button2.pack()
        button3.pack()

    def close_window(self):
        self.quit()


class Instructions(Frame):
    """Contains everything to show on Instructions page
    """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Instructions", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)
        label = Label(self, text="Welcome to the CAMPUS TOUR GUIDE!\n"
                                 "You will be able to generate the shortest tour\n"
                                 "of the campus with only the buildings you want to visit.\n"
                                 "Press Start on HOME page. Select any number of the listed \n"
                                 "buildings on campus and then hit Generate. The program\n"
                                 "generates the shortest path that you can take to visit\n"
                                 "the selected buildings. Have fun!", font=SUB_TITLE_FONT)
        label.pack(side="top", fill="x", pady=20)
        button = Button(self, text="Go to the Start page",
                        command=lambda: controller.show_frame(StartPage))
        button.pack()


class Selection(Frame):
    """Contains everything to show on Selection of buildingSelection of buildings page
    """
    def __init__(self,parent, controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.ichose = []
        self.graph = Graph()
        self.items = self.get_selection()


        self.l = Listbox(self, width=20, height=10, selectmode=MULTIPLE)
        # Selectmode can be SINGLE, BROWSE, MULTIPLE or EXTENDED. Default BROWSE
        self.l.grid(column=0, row=0, sticky=(N,W,E,S))

        s = Scrollbar(self, orient=VERTICAL, command=self.l.yview)
        s.grid(column=0, row=0, sticky=(N,S,E))
        self.l['yscrollcommand'] = s.set

        for i in self.items:
            self.l.insert(0,i)

        # Create Textbox that will display selected items from list
        self.selected_list = Text(self,width=20,height=10,wrap=WORD)
        self.selected_list.grid(row=12, column=0, sticky=W)

        # Now execute the poll() function to capture selected list items
        self.ichose = self.poll()

        button = Button(self, width=10, text='Home', command=lambda :controller.show_frame(StartPage))
        button.grid(row=13, column=0, sticky=W)
        button = Button(self, width=10, text='Generate', command=lambda :self.generate_graph())
        button.grid(row=13, column=0, sticky=E)

    def poll(self):
        items =[]
        self.ichose = []

        # Set up an automatically recurring event that repeats after 200 millisecs
        self.selected_list.after(200, self.poll)
        # curselection retrieves the selected items as a tuple of strings. These
        # strings are the list indexes ('0' to whatever) of the items selected.
        # map applies the function specified in the 1st parameter to every item
        # from the 2nd parameter and returns a list of the results. So "items"
        # is now a list of integers
        items = map(int,self.l.curselection())

        # For however many values there are in "items":
        for i in range(len(items)):
            # Use each number as an index and get from the listbox the actual
            # text strings corresponding to each index, and append each to
            # the list "ichose".
            self.ichose.append(self.l.get(items[i]))
        # Write ichose to the textbox to display it.
        self.update_list()
        return self.ichose

    def update_list(self):
        self.selected_list.delete(0.0, END)
        self.selected_list.insert(0.0, self.ichose)

    def get_selection(self):
        """Gets data to ppopulate the selection list Scrollbar
        """
        read = ReadMap()    # create an read map object
        read.read_file('test.map')  # read from the database file
        # print read.graph
        self.graph = read.graph # update the graph attribute from reading the map
        return read.names   # return a list of building names in the map

    def generate_graph(self):
        """Generates the graph using GraphWorld.
        """
        grapher = BestPath(self.ichose) # create a BestPath object, using chosen cities
        grapher.set_map(self.graph) # set the map read from the database
        # generate a Tour by calling the generate_actualtour method of BetPath Class
        Tour = grapher.genrate_actualtour(Vertex(self.ichose[0]))
        
        layout = CircleLayout(Tour)

        gw = GraphWorld()
        gw.show_graph(Tour, layout)
        gw.mainloop()