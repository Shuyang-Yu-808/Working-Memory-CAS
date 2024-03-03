from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from subject import Subject,IntervieweeNameError,GenderError,AgeError
from config import conf
class StartPageGUI(Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg = conf.canvas_color)
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

    def __label_last(self,parent):
        label = tk.Label(parent,font=conf.label_font,text="姓：",anchor="center",fg = conf.label_text_color,bg = conf.canvas_color)
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2-120, width=100, height=40)
        return label
    
    def __input_last(self,parent):
        ipt = Entry(parent)
        ipt.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2-120, width=80, height=40)
        return ipt
    
    def __label_first(self,parent):
        label = tk.Label(parent,font=conf.label_font,text="名：",anchor="center", fg = conf.label_text_color,bg = conf.canvas_color)
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2-40, width=100, height=40)
        return label
    
    def __input_first(self,parent):
        ipt = Entry(parent)
        ipt.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2-40, width=80, height=40)
        return ipt
    
    def __label_gender(self,parent):
        label = tk.Label(parent,font=conf.label_font,text="性别：",anchor="center", fg = conf.label_text_color,bg = conf.canvas_color)
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2+40, width=100, height=40)
        return label
    
    def __select_gender(self,parent):
        cb = Combobox(parent, state="readonly",)
        cb['values'] = ("","男","女")
        cb.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2+40, width=80, height=40)
        return cb
    
    def __label_age(self,parent):
        label = tk.Label(parent,font=conf.label_font,text="年龄：",anchor="center",fg = conf.label_text_color,bg = conf.canvas_color)
        label.place(x=self.winfo_screenwidth()/2-100, y=self.winfo_screenheight()/2+120, width=100, height=40)
        return label
    
    def __input_age(self,parent):
        ipt = Entry(parent)
        ipt.place(x=self.winfo_screenwidth()/2, y=self.winfo_screenheight()/2+120, width=80, height=40)
        return ipt
    
    def __label_error(self,parent,text):
        label = tk.Label(parent,font=conf.label_font,text=text,anchor="center",justify="center",fg = 'red',bg = conf.canvas_color)
        label.place(x=self.winfo_screenwidth()/2-250, y=self.winfo_screenheight()/2-220, width=600, height=40)
        return label
    
    def __button(self,parent):
        btn = tk.Button(parent,text="继续", takefocus=False,command=lambda: self.__validation(),fg = conf.button_text_color,bg = conf.button_bg_color)
        btn.place(relx=conf.next_button_relx,
                  rely=conf.next_button_rely,
                  relwidth=conf.next_button_relwidth,
                  relheight=conf.next_button_relheight)
        return btn
    
    '''
    Examines the input values
    Catches different errors when different invalid inputs are detected
    Creats a new subject instance if all valid
    Stores the subject instance into window instance as an attribute
    Switches to the next frame
    '''
    def __validation(self):
        try:
            self.interviewee = Subject(self.input_first.get(),
                              self.input_last.get(),
                              self.input_age.get(),
                              self.select_gender.get())
            self.interviewee.examine()
        except IntervieweeNameError:
            self.label_error = self.__label_error(self, "姓名输入不正确，请重新输入。")
        except GenderError:
            self.label_error = self.__label_error(self, "性别选择不正确，请重新选择。")
        except AgeError:
            self.label_error = self.__label_error(self, "年龄输入不正确，请重新输入。")
        else:
            self.controller.subject = self.interviewee
            self.controller.show_frame("IntroGUI")