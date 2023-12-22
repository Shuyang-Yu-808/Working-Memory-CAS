from initialize import StartPageGUI
from opening_instruction import IntroGUI
from subject import Subject,IntervieweeNameError,GenderError,AgeError
from main_task import mainTask as Single #the frame for testing
import tkinter as tk
from tkinter import ttk
'''
This is a helper function that runs on a single frame
This function should be used for debugging purposes only
'''
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
  
        self.frame = Single(parent=container, controller=self)

        self.frame.grid(row = 0, column = 0, sticky ="nsew")
        self.show_frame()

    def show_frame(self):
        self.frame.tkraise()

    def __win(self):
        self.title("工作记忆精确度实验")
        geometry = '%dx%d+%d+%d' % (self.winfo_screenwidth(),self.winfo_screenheight(),0,0)
        self.geometry(geometry)
        self.attributes('-fullscreen',True)
        self.resizable(width=False, height=False)


app = tkinterApp()
app.mainloop()