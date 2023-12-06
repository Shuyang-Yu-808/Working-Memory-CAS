import tkinter as tk
from tkinter import ttk
from initialize import StartPageGUI
from opening_instruction import IntroGUI
from base_opening import BaseIntroGUI
from base_body import BaseBodyGUI
from test_instruction import TestIntroGUI

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs): 
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.__win()

        # Creats a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1) 
  
  
        # Initializes an array of frames
        self.frames = {}
        for F in (StartPageGUI, IntroGUI,BaseIntroGUI,BaseBodyGUI,TestIntroGUI):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame("StartPageGUI")

    # Window configuration
    def __win(self):
        self.title("工作记忆精确度实验")
        geometry = '%dx%d+%d+%d' % (self.winfo_screenwidth(),self.winfo_screenheight(),0,0)
        self.geometry(geometry)
        self.attributes('-fullscreen',True)
        self.resizable(width=False, height=False)

    
    # Displays the given frame
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    # Exits the program
    def exit(self):
        self.destroy()



app = tkinterApp()
app.mainloop()