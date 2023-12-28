import tkinter as tk
from tkinter.ttk import *
from config import conf

class IntroGUI(Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg = conf.canvas_color)
        self.controller = controller
        self.label_instruction = self.__label_instruction(self)
  
        self.button = self.__button(self)

    def __label_instruction(self,parent):
        label = tk.Label(parent,text='''你好！欢迎你参加本次心理学实验，在完成任务前请仔细阅读以下的指导语：
本次实验是关于视觉的心理学实验，任务表现的好坏都不影响对你个人能力的评价，请尽自己最大的能力
完成即可。在接下来的任务中，你将会看到一些不同颜色、朝向的线段，请你尽可能准确地记住不同颜色
线段的朝向，之后用鼠标按照你记忆的方向调整相应颜色线段的朝向。
确认调整好后单击“继续”按钮以继续实验。如果已经理解指导语，请点击“继续”按钮''',anchor="center",
        font=conf.label_font,fg = conf.label_text_color,bg = conf.canvas_color)
        label.place(relx=conf.instruction_relx,
                    rely=conf.instruction_rely,
                    anchor=tk.CENTER,
                    relwidth=conf.instruction_relwidth+1,
                    relheight=conf.instruction_relheight+1)
        return label
    
    def __button(self,parent):
        btn = tk.Button(parent, text="继续", 
                        fg = conf.button_text_color,bg = conf.button_bg_color,
                        takefocus=False,command= lambda: self.controller.show_frame("BaseBodyGUI"))
        btn.place(relx=conf.next_button_relx,
                  rely=conf.next_button_rely,
                  relwidth=conf.next_button_relwidth,
                  relheight=conf.next_button_relheight)
        return btn