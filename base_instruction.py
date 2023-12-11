from tkinter import *
from tkinter.ttk import *

class base_instruct(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.tk_label_lp8z7p86 = self.__instruction_label(self)
        self.button = self.__next_button(self)


    def __instruction_label(self,parent):
        label = Label(parent,text='''接下来，屏幕上半部分中央会显示某个朝向的线段，请你用鼠标调整下方的线段
直至和上方的一样，按“继续”按钮继续，这个过程会重复10次。''',
                      font=("Arial", 25),
                      anchor="center")
        label.pack()
        label.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.6,anchor = CENTER)
        
        return label
    


    def __next_button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command= lambda : self.controller.show_frame("base_instruct"))
        btn.place(relx=0.8, rely=0.7, relwidth=0.08, relheight=0.06)
        return btn