from tkinter import *
from tkinter.ttk import *

class BaseIntroGUI(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.label_intro = self.__label_first_intro(self)
        self.button = self.__continue_button(self)

    def __label_first_intro(self,parent):
        label = Label(parent,text='''接下来，请你完成一些小任务，帮助你更好地完成后续的正式实验。请点击“继续”按钮。''',
                      font=("Arial", 25),
                      anchor="center")
        label.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.6,anchor = CENTER)
        return label
    
    def __label_second_intro(self,parent):
        label = Label(parent,text='''接下来，屏幕上半部分中央会显示某个朝向的线段，请你用鼠标调整下方的线段
直至和上方的一样，按“继续”按钮继续，这个过程会重复10次。''',
                      font=("Arial", 25),
                      anchor="center")
        label.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.6,anchor = CENTER)
        return label
    
    def __continue_button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command= lambda : self.__change_instruction())
        btn.place(relx=0.8, rely=0.7, relwidth=0.08, relheight=0.06)
        return btn
    
    def __begin_button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command= lambda : self.controller.show_frame("BaseBodyGUI"))
        btn.place(relx=0.8, rely=0.7, relwidth=0.08, relheight=0.06)
        return btn
    
    def __change_instruction(self):
        self.label_intro.destroy()
        self.button.destroy()
        self.label_intro = self.__label_second_intro(self)
        self.button = self.__begin_button(self)
        

