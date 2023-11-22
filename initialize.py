from tkinter import *
from tkinter.ttk import *
from subject import Subject

class StartPageGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_lp8xks5k = self.__tk_label_lp8xks5k(self)
        self.tk_input_lp8xlrdu = self.__tk_input_lp8xlrdu(self)
        self.tk_label_lp8xmenj = self.__tk_label_lp8xmenj(self)
        self.tk_input_lp8xmq5r = self.__tk_input_lp8xmq5r(self)
        self.tk_label_lp8xmyvp = self.__tk_label_lp8xmyvp(self)
        self.tk_select_box_lp8xn6ia = self.__tk_select_box_lp8xn6ia(self)
        self.tk_label_lp8xnl5f = self.__tk_label_lp8xnl5f(self)
        self.tk_input_lp8xnpy1 = self.__tk_input_lp8xnpy1(self)
        self.tk_button_lp8z652o = self.__tk_button_lp8z652o(self)
        #self.subject = Subject()

    def _close(self):
        self.destroy()

    def __win(self):
        self.title("工作记忆精确度实验")
        # 设置窗口大小、居中
        geometry = '%dx%d+%d+%d' % (self.winfo_screenwidth(),self.winfo_screenheight(),0,0)
        self.geometry(geometry)
        self.attributes('-fullscreen',True)
        
        self.resizable(width=False, height=False)
        
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
    def __tk_button_lp8z652o(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command=self._close)
        btn.place(relx=0.8166666666666667, rely=0.7, relwidth=0.08333333333333333, relheight=0.06)
        return btn