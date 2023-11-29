from tkinter import *
from tkinter.ttk import *

class base_instruct(Frame):
    def __init__(self,parent,controller):

        Frame.__init__(self,parent)
        self.controller = controller
        self.tk_label_lp8z7p86 = self.__instruction_label(self)
  
        self.button = self.__next_button(self)


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

    def __instruction_label(self,parent):
        label = Label(parent,text='''接下来，屏幕上半部分中央会显示某个朝向的线段，请你用鼠标调整下方的线段
直至和上方的一样，按“继续”按钮继续，这个过程会重复10次。''',
                      font=("Arial", 25),
                      anchor="center")
        label.pack()
        label.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.6,anchor = CENTER)
        
        return label
    def __next_button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command= lambda : self.controller.show_frame("base_intro"))
        btn.place(relx=0.8166666666666667, rely=0.7, relwidth=0.08333333333333333, relheight=0.06)
        return btn