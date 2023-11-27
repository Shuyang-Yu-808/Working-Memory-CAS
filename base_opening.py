from tkinter import *
from tkinter.ttk import *
from window import Window

class IntroGUI(Window):
    def __init__(self):
        super().__init__()
        self.tk_label_lp8z7p86 = self.__tk_label_lp8z7p86(self)
  

    def close(self):
        self.destroy()
        

    def __tk_label_lp8z7p86(self,parent):
        label = Label(parent,text='''接下来，请你完成一些小任务，帮助你更好地完成后续的正式实验。请点击“继续”按钮。''',anchor="center")
        label.place(relx=0.15, rely=0.1, relwidth=0.6566666666666666, relheight=0.522)
        return label