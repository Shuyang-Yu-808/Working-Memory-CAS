from tkinter import *
from tkinter.ttk import *

class IntroGUI(Frame):
    def __init__(self,parent,controller):

        Frame.__init__(self,parent)
        self.controller = controller
        self.label_instruction = self.__label_instruction(self)
  
        self.button = self.__button(self)


    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __label_instruction(self,parent):
        label = Label(parent,text='''你好！欢迎你参加本次心理学实验，在完成任务前请仔细阅读以下的指导语：
本次实验是关于视觉的心理学实验，任务表现的好坏都不影响对你个人能力的评价，请尽自己最大的能力
完成即可。在接下来的任务中，你将会看到一些不同颜色、朝向的线段，请你尽可能准确地记住不同颜色
线段的朝向，之后用鼠标按照你记忆的方向调整相应颜色线段的朝向。确认调整好后单击“继续”按钮以继续实
验。如果已经理解指导语，请点击“继续”按钮''',anchor="center",
        font=("Arial",25))
        # label.config(width=50,height=100)

        
        # label.place(relx=0.15, rely=0.1, relwidth=0.6566666666666666, relheight=0.522)
        # label.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.7, anchor=CENTER,width=200, height=40)
        label.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2, anchor=CENTER,relwidth=1, relheight=1)


        return label
    def __button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command= lambda: self.controller.show_frame("base_intro"))
        btn.place(relx=0.8, rely=0.7, relwidth=0.08, relheight=0.06)

        return btn