from tkinter import *
from tkinter.ttk import *

class IntroGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_lp8z652o = self.__tk_button_lp8z652o(self)
        self.tk_label_lp8z7p86 = self.__tk_label_lp8z7p86(self)

    def _close(self):
        self.destroy()
    
    def __win(self):
        self.title("基线任务指导语")
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
    def __tk_button_lp8z652o(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command=self._close)
        btn.place(relx=0.8166666666666667, rely=0.7, relwidth=0.08333333333333333, relheight=0.06)
        return btn
    def __tk_label_lp8z7p86(self,parent):
        label = Label(parent,text='''接下来，请你完成一些小任务，帮助你更好地完成后续的正式实验。请点击“继续”按钮。''',anchor="center")
        label.place(relx=0.15, rely=0.1, relwidth=0.6566666666666666, relheight=0.522)
        return label
    

if __name__ == "__main__":
    # win = Win()
    win = IntroGUI()
    win.mainloop()