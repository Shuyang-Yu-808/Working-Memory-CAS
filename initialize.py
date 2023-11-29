from tkinter import *
from tkinter.ttk import *
from subject import Subject,IntervieweeNameError,GenderError,AgeError

class StartPageGUI(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller

        self.label_last = self.__label_last(self)
        self.input_last = self.__input_last(self)
        self.label_first = self.__label_first(self)
        self.input_first = self.__input_first(self)
        self.label_gender = self.__label_gender(self)
        self.select_gender = self.__select_gender(self)
        self.label_age = self.__label_age(self)
        self.input_age = self.__input_age(self)

        self.button = self.__button(self)

        
    def info(self):
        interviewee = Subject(self.input_first.get(),
                              self.input_last.get(),
                              self.input_age.get(),
                              self.select_gender.get())
        return interviewee

    def error(self,e):
        self.label_error = self.__label_error(self,e)

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

    def __label_last(self,parent):
        label = Label(parent,text="姓：",anchor="center", )
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2-120, width=60, height=40)
        return label
    def __input_last(self,parent):
        ipt = Entry(parent)
        ipt.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2-120, width=80, height=40)
        return ipt
    def __label_first(self,parent):
        label = Label(parent,text="名：",anchor="center", )
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2-40, width=60, height=40)
        return label
    def __input_first(self,parent):
        ipt = Entry(parent)
        ipt.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2-40, width=80, height=40)
        return ipt
    def __label_gender(self,parent):
        label = Label(parent,text="性别：",anchor="center", )
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2+40, width=60, height=40)
        return label
    def __select_gender(self,parent):
        cb = Combobox(parent, state="readonly")
        cb['values'] = ("","男","女")
        cb.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2+40, width=80, height=40)
        return cb
    def __label_age(self,parent):
        label = Label(parent,text="年龄：",anchor="center", )
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2+120, width=60, height=40)
        return label
    def __input_age(self,parent):
        ipt = Entry(parent)
        ipt.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2+120, width=80, height=40)
        return ipt
    def __button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command=self.controller.go_to_opening)
        btn.place(relx=0.8, rely=0.7, relwidth=0.08, relheight=0.06)
        return btn
    def __label_error(self,parent,e):
        if e==IntervieweeNameError:
            text = "姓名输入不正确，请重新输入。"
        elif e==GenderError:
            text = "性别选择不正确，请重新选择。"
        else:
            text = "年龄输入不正确，请重新输入。"
        label = Label(parent,text=text,anchor="center",justify="center")
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2-220, width=200, height=40)

        return label