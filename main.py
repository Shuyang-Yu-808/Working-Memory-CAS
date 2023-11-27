from initialize import StartPageGUI
from opening_instruction import IntroGUI
from subject import Subject

import tkinter as tk
from tkinter import ttk

# startpage = StartPageGUI()
# startpage.mainloop()
# global interviewee
# startpage = StartPageGUI()
# startpage.mainloop()

# intro = IntroGUI()
# intro.mainloop()

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs): 
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.__win()
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        # container.grid_rowconfigure(0, weight = 1)
        # container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}  
        for F in (StartPageGUI, IntroGUI):

            frame = F(parent=container, controller=self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[F] = frame 

            # frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPageGUI)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def __win(self):
        self.title("工作记忆精确度实验")
        geometry = '%dx%d+%d+%d' % (self.winfo_screenwidth(),self.winfo_screenheight(),0,0)
        self.geometry(geometry)
        self.attributes('-fullscreen',True)
        self.resizable(width=False, height=False)
app = tkinterApp()
app.mainloop()