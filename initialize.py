from tkinter import *
from tkinter.ttk import *
from subject import Subject
from window import Window

class StartPageGUI(Window):
    def __init__(self):
        super().__init__()
        self.tk_label_lp8xks5k = self.__tk_label_lp8xks5k(self)
        self.tk_input_lp8xlrdu = self.__tk_input_lp8xlrdu(self)
        self.tk_label_lp8xmenj = self.__tk_label_lp8xmenj(self)
        self.tk_input_lp8xmq5r = self.__tk_input_lp8xmq5r(self)
        self.tk_label_lp8xmyvp = self.__tk_label_lp8xmyvp(self)
        self.tk_select_box_lp8xn6ia = self.__tk_select_box_lp8xn6ia(self)
        self.tk_label_lp8xnl5f = self.__tk_label_lp8xnl5f(self)
        self.tk_input_lp8xnpy1 = self.__tk_input_lp8xnpy1(self)
        #self.subject = Subject()

    def close(self):
        self.destroy()

    def __tk_label_lp8xks5k(self,parent):
        label = Label(parent,text="姓：",anchor="center", )
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2-120, width=60, height=40)
        return label
    def __tk_input_lp8xlrdu(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2-120, width=80, height=40)
        return ipt
    def __tk_label_lp8xmenj(self,parent):
        label = Label(parent,text="名：",anchor="center", )
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2-40, width=60, height=40)
        return label
    def __tk_input_lp8xmq5r(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2-40, width=80, height=40)
        return ipt
    def __tk_label_lp8xmyvp(self,parent):
        label = Label(parent,text="性别：",anchor="center", )
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2+40, width=60, height=40)
        return label
    def __tk_select_box_lp8xn6ia(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("","男","女")
        cb.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2+40, width=80, height=40)
        return cb
    def __tk_label_lp8xnl5f(self,parent):
        label = Label(parent,text="年龄：",anchor="center", )
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2+120, width=60, height=40)
        return label
    def __tk_input_lp8xnpy1(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2+120, width=80, height=40)
        return ipt