from tkinter import *
from tkinter.ttk import *

class TestIntroGUI(Frame):
    def __init__(self,parent,controller):

        Frame.__init__(self,parent)
        self.controller = controller
        self.label_instruction = self.__label_instruction(self)
  
        self.button = self.__button(self)

    def __label_instruction(self,parent):
        label = Label(parent,text='''在此添加正式试验说明''',anchor="center",
        font=("Arial",25))
        label.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2, anchor=CENTER,relwidth=1, relheight=1)
        return label
    
    def __button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command= lambda: self.controller.exit())
        btn.place(relx=0.8, rely=0.7, relwidth=0.08, relheight=0.06)
        return btn