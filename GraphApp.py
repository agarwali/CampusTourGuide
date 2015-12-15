# -----------------------------------------------------------------------------------------------------------------
# File Name: GraphApp.py
# Purpose: It contains the GraphApp class that is used to create the Graphic User Interface for Campus Tour Guide
# Author: Ishwar Agarwal
# Last Date Modified: 12/11/2015
# Acknowledgements: * Ishwar Agarwal for sharing his code from his CSC 236 final project
#                     https://github.com/agarwali/
#                   * The code for changing pages(line 32-53) in tkinter window was derived from a stackoverflow
#                     answer http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# ------------------------------------------------------------------------------------------------------------------


from Tkinter import Tk, Button, Label, Frame
from tkFont import Font
from Pages import *


class GraphApp(Frame):
    """Graph app that controls frames crated using Tkinter library.

    This API inherits from Tkinter Frame class and allows to easily create
    and control pages in the GUI. This class has a attribute which is dictionary
    that stores the pages that are to be implemented separately as classes and 
    added to the frames dictionary.

    All the pages are stored in the module Pages.py

    Parameters:
        root: A Tkinter object that has to passed into the class while creating an instance
        *args: allows to pass any argument into the class without knowing its name
        **kwards: allows to use any passed argument without knowing its name
    Attributes:
        self.app: It is a copy of the passed Tk() object
        self.frames: A dictionary that stores each page, the key is the object itself and the value it
                    maps to the the instance of the same object within a fixed container(Frame).

    """

    def __init__(self, root, *args, **kwargs):
        Frame.__init__(self, root, *args, **kwargs)

        self.app = root
        self.app.title('Campus TOur Guide v1.0')
        self.app.wm_iconbitmap('tour.ico')
        self.app.resizable(width=False, height=False)



        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(root)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Instructions,Selection):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()
