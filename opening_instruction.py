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
        label = Label(parent,text='''你好！欢迎你参加本次心理学实验，在完成任务前请仔细阅读以下的指导语：
本次实验是关于视觉的心理学实验，任务表现的好坏都不影响对你个人能力的评价，请尽自己最大的能力
去做即可。在接下来的任务中，你将会看到一些不同颜色、朝向的线段，请你尽可能准确地记住不同颜色
线段的朝向，之后用鼠标按照你记忆的方向调整相应颜色线段的朝向。确认调整好后单击“继续”按钮以继续实
验。如果已经理解指导语，请点击“继续”按钮''',anchor="center")
        label.place(relx=0.15, rely=0.1, relwidth=0.6566666666666666, relheight=0.522)
        return label