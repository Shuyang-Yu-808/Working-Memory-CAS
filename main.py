import tkinter as tk
from tkinter import ttk

from initialize import StartPageGUI
from opening_instruction import IntroGUI
from base_opening import BaseIntroGUI
from base_body import BaseBodyGUI

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs): 
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.__win()
        # creating a containerclear
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1) 
  
  
        # initializing frames to an empty array
        self.frames = {}
        for F in (StartPageGUI, IntroGUI,BaseIntroGUI,BaseBodyGUI):
            page_name = F.__name__
            frame = F(parent=container, controller=self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
            self.frames[page_name] = frame 

            frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame("StartPageGUI")


    def __win(self):
        self.title("工作记忆精确度实验")
        geometry = '%dx%d+%d+%d' % (self.winfo_screenwidth(),self.winfo_screenheight(),0,0)
        self.geometry(geometry)
        self.attributes('-fullscreen',True)
        self.resizable(width=False, height=False)

    
    # Display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



app = tkinterApp()
app.mainloop()