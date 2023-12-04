from tkinter import *
from tkinter.ttk import *
from random import *
import math

RADIUS = 200

class BaseBodyGUI(Frame):
    def __init__(self,parent,controller):

        Frame.__init__(self,parent)
        self.controller = controller
        self.canvas_w = self.winfo_screenwidth()
        self.canvas_h = self.winfo_screenheight()/2
        self.button = self.__button(self)
        
        self.upper_canvas = self.__upper_canvas(self)
        self.lower_canvas = self.__lower_canvas(self)
        
        self.upper_coords = self.rand_coor_on_circle(200,self.canvas_w,self.canvas_h)
        self.upper_coords = self.rand_coor_on_circle(200,self.canvas_w,self.canvas_h)
        
        
        self.lower_coords = self.h_coor_on_circle_lower(200,self.canvas_w,self.canvas_h)

        self.upper_line = self.draw_line(self,self.upper_coords,'upper')
        self.lower_line = self.draw_line(self,self.lower_coords,'lower')

        self.lower_center_x = self.canvas_w/2
        self.lower_center_y = self.winfo_screenheight()/4 # relative coordinate on lower canvas not global height
        

        #TO DO: change 200 to global variable RADIUS
        self.lower_canvas.create_oval(self.canvas_w/2-200,self.canvas_h/2-200,self.canvas_w/2+200,self.canvas_h/2+200,width = 2,
        dash=(10,10))
        
        # test rotate function
        self.lower_canvas.create_oval(self.canvas_w/2+50-5,self.canvas_h/2+60-5,self.canvas_w/2+50+5,self.canvas_h/2+60+5,fill="red")
        # print('self canvas w',self.canvas_w)
        # print('self canvas h',self.canvas_h)

        self.rotate_lower_line(self,x = self.canvas_w/2+50,y = self.canvas_h/2+60)
        
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
    
    def __button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command= lambda: self.controller.show_frame("base_intro"))
        btn.place(relx=0.8166666666666667, rely=0.7, relwidth=0.08333333333333333, relheight=0.06)
        return btn
    
    def __upper_canvas(self,parent):
        cvs = Canvas(parent,
                     width=self.winfo_screenwidth(),
                     height=self.winfo_screenheight()/2,bg='#fff')
        cvs.place(x=self.winfo_screenwidth()/2,
                  y=self.winfo_screenheight()*(1/4),
                  anchor="center")
        return cvs


    def __lower_canvas(self,parent):
        cvs = Canvas(parent,
                     width=self.winfo_screenwidth(),
                     height=self.winfo_screenheight()/2,bg='#eee')
        cvs.place(x=self.winfo_screenwidth()/2,
                  y=self.winfo_screenheight()*(3/4),
                  anchor="center")
        return cvs
    
    
    def draw_line(self,parent,coords,canvas):
        if canvas == "upper":
            return self.upper_canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=20)
        elif canvas == 'lower':
            return self.lower_canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=20)

    
    def draw_point(self,parent,coor,r,canvas):
        centerx = coor[0]
        centery = coor[1]
        if canvas == "upper":
            return self.upper_canvas.create_oval(centerx-r, centery-r, centerx+r, centery+r, width = 2)
        elif canvas == 'lower':
            return self.lower_canvas.create_oval(centerx-r, centery-r, centerx+r, centery+r, width = 2)
        #return self.canvas.create_oval(0,0,200,200, width = 2)
    
    def rand_coor(self):
        return (randint(0,self.canvas_w/2),randint(0,self.canvas_h/2))

    def rand_coor_on_circle(self,radius,w,h):
        theta = math.radians(randint(0,359))
        center_x = w/2
        center_y = h/2
        point1_x = center_x+math.cos(theta)*radius
        point1_y = center_y+math.sin(theta)*radius
        point2_x = center_x-math.cos(theta)*radius
        point2_y = center_y-math.sin(theta)*radius        
        return (point1_x,point1_y,point2_x,point2_y)
    
    def h_coor_on_circle_lower(self,radius,w,h):
        theta = math.radians(0)
        center_x = w/2
        center_y = h/2
        print(center_x,center_y)
        point1_x = center_x+radius
        point1_y = center_y
        point2_x = center_x-radius
        point2_y = center_y        
        return (point1_x,point1_y,point2_x,point2_y)

    def rotate_lower_line(self,parent,x,y):
        # print(x)
        # print(y)
        # print(self.lower_center_x)
        # print(self.lower_center_y)
        # print(RADIUS)
        # print("result",(x-self.lower_center_x)**2 + (y-self.lower_center_y)**2)
        # print("radius sq", RADIUS**2)
        if ((x-self.lower_center_x)**2 + (y-self.lower_center_y)**2) <= (RADIUS**2):
            print('1')
            slope = (y-self.lower_center_y)/(x-self.lower_center_x)
            theta = math.atan(slope)
            x_offset = math.cos(theta)*RADIUS
            y_offset = math.sin(theta)*RADIUS
            new_p1_x = self.lower_center_x+x_offset
            new_p1_y = self.lower_center_y+y_offset
            
            new_p2_x = self.lower_center_x-x_offset
            new_p2_y = self.lower_center_y-y_offset
            # print(new_p1_x,new_p1_y,new_p2_x,new_p2_y)
            self.lower_canvas.create_line(new_p1_x,new_p1_y,new_p2_x,new_p2_y,width=2)    