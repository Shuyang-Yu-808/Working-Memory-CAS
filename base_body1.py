from tkinter import *
from tkinter.ttk import *
from random import *
import math

# Scale of user operable are
# Radisu = screen height/4*SCALE
SCALE = 0.9
# The minimum difference between mouse x and center x
# Avoids extremely large slope of line
MINIMUM_X_DIFF = 3

class BaseBodyGUI(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller
        # Baseline task repetition counter

        self.label_intro = self.__label_first_intro(self)
        self.button = self.__label_continue_button(self)


    def __label_first_intro(self,parent):
        label = Label(parent,text='''接下来，请你完成一些小任务，帮助你更好地完成后续的正式实验。请点击“继续”按钮。''',
                      font=("Arial", 25),
                      anchor="center")
        label.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.6,anchor = CENTER)
        return label
    

    def __label_second_intro(self,parent):
        label = Label(parent,text='''接下来，屏幕上半部分中央会显示某个朝向的线段，请你用鼠标调整下方的线段
直至和上方的一样，按“继续”按钮继续，这个过程会重复10次。''',
                      font=("Arial", 25),
                      anchor="center")
        label.place(relx=0.5, rely=0.5, relwidth=0.7, relheight=0.6,anchor = CENTER)
        return label


    def __label_continue_button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command= lambda : self.__change_instruction())
        btn.place(relx=0.8, rely=0.7, relwidth=0.08, relheight=0.06)
        return btn    

    
    def __set_up_baseline_task(self):
        self.label_intro.destroy()
        self.button.destroy()

        self.count = 1

        # Radius of operable circle
        self.radius = self.winfo_screenheight()/4*SCALE

        # Mouse coordinates
        self.mouse_x = 0
        self.mouse_y = 0

        # Size of half-screen canvas
        self.canvas_w = self.winfo_screenwidth()
        self.canvas_h = self.winfo_screenheight()/2
        
        # Canvas instances
        self.upper_canvas = self.__upper_canvas(self)
        self.lower_canvas = self.__lower_canvas(self)
        
        # Reference line on upper canvas format(x1,y1,x2,y2)
        self.upper_coords = self.__generate_coor_upper_line(self.radius,self.canvas_w,self.canvas_h)
        self.upper_line = self.__draw_line(self,self.upper_coords,'upper')

        # Operable line on lower canvas
        self.lower_coords = self.__generate_coor_lower_line(self.radius,self.canvas_w,self.canvas_h)
        self.lower_line = self.__draw_line(self,self.lower_coords,'lower')

        # Center coordinates of lower canvas (not screen coordinates)
        self.lower_center_x = self.canvas_w/2
        self.lower_center_y = self.winfo_screenheight()/4 

        # User operable area indicator
        self.lower_canvas.create_oval(self.canvas_w/2-self.radius,
                                      self.canvas_h/2-self.radius,
                                      self.canvas_w/2+self.radius,
                                      self.canvas_h/2+self.radius,
                                      width = 2,
                                      dash=(10,10))

        self.lower_canvas.bind("<B1-Motion>", self.__drag)
        
        # Continue button instance
        self.button = self.__task_continue_button(self)
        self.base_result = []
        self.lower_line_slope = 0
        self.timer = self.after(10000,self.__reset)
        


    def __next_to_task_button(self,parent):   
        # btn = Button(parent, text="继续", takefocus=False,command= lambda : self.__change_instruction())
        btn = Button(parent, text="继续", takefocus=False, command = lambda : self.__set_up_baseline_task())
        btn.place(relx=0.8, rely=0.7, relwidth=0.08, relheight=0.06)
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
    
    def __task_continue_button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command= lambda: self.__reset())
        btn.place(relx=0.81, rely=0.7, relwidth=0.083, relheight=0.06)
        return btn
    
    
    def __draw_line(self,parent,coords,canvas):
        if canvas == "upper":
            return self.upper_canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=5)
        elif canvas == 'lower':
            return self.lower_canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=5)

    def __generate_coor_upper_line(self,radius,w,h):
        theta = math.radians(randint(0,359))
        center_x = w/2
        center_y = h/2
        point1_x = center_x+math.cos(theta)*radius
        point1_y = center_y+math.sin(theta)*radius
        point2_x = center_x-math.cos(theta)*radius
        point2_y = center_y-math.sin(theta)*radius        
        return (point1_x,point1_y,point2_x,point2_y)
    
    def __generate_coor_lower_line(self,radius,w,h):
        theta = math.radians(0)
        center_x = w/2
        center_y = h/2
        point1_x = center_x+radius
        point1_y = center_y
        point2_x = center_x-radius
        point2_y = center_y        
        return (point1_x,point1_y,point2_x,point2_y)

    def __rotate_lower_line(self,parent,x,y):
        if abs(x - self.lower_center_x) <= MINIMUM_X_DIFF:
            # don't update the slope
            new_p1_x = self.lower_center_x
            new_p2_x = self.lower_center_x
            if y <= self.lower_center_y:
                new_p1_y = self.lower_center_y-self.radius
                new_p2_y = self.lower_center_y+self.radius
            else:
                new_p1_y = self.lower_center_y+self.radius
                new_p2_y = self.lower_center_y-self.radius
        else:
            slope = (y-self.lower_center_y)/(x-self.lower_center_x)
            theta = math.atan(slope)
            x_offset = math.cos(theta)*self.radius
            y_offset = math.sin(theta)*self.radius
            new_p1_x = self.lower_center_x+x_offset
            new_p1_y = self.lower_center_y+y_offset
            new_p2_x = self.lower_center_x-x_offset
            new_p2_y = self.lower_center_y-y_offset
            self.lower_line_slope = slope
        self.lower_canvas.delete(self.lower_line)
        self.lower_line = self.__draw_line(self,[new_p1_x,new_p1_y,new_p2_x,new_p2_y],"lower")    
    
    def __drag(self,event):
        if ((event.x-self.lower_center_x)**2 + (event.y-self.lower_center_y)**2) <= (self.radius**2):
            self.mouse_x = event.x
            self.mouse_y = event.y
            self.__rotate_lower_line(self,self.mouse_x,self.mouse_y)

    def _update_base_result(self,slope1,slope2):
        theta1 = math.atan(slope1)
        theta2 = math.atan(slope2)
        self.base_result.append(abs(theta1-theta2))


    def __reset(self):
        self.after_cancel(self.timer)
        self._update_base_result((self.upper_coords[3]-self.upper_coords[1])/(self.upper_coords[2]-self.upper_coords[0]),self.lower_line_slope)
        if self.count == 10:
            self.upper_canvas.delete("all")
            self.lower_canvas.delete("all")
            self.upper_canvas.destroy()
            self.lower_canvas.destroy()
            self.button.destroy()
            print(self.base_result)
            
        elif self.count < 10:
            self.mouse_x = 0
            self.mouse_y = 0

            self.upper_canvas.delete(self.upper_line)
            self.upper_coords = self.__generate_coor_upper_line(self.radius,self.canvas_w,self.canvas_h)
            self.upper_line = self.__draw_line(self,self.upper_coords,'upper')

            self.lower_canvas.delete(self.lower_line)
            self.lower_coords = self.__generate_coor_lower_line(self.radius,self.canvas_w,self.canvas_h)
            self.lower_line = self.__draw_line(self,self.lower_coords,'lower')
            # if self.count == 9:
            #     self.button.destroy()
            #     self.button = self.__next_button(self)
            self.timer = self.after(10000,self.__reset)

        self.count += 1
        # self.timer = self.after(10000,self.__reset)

    
    def __change_instruction(self):
        self.label_intro.destroy()
        self.button.destroy()
        self.label_intro = self.__label_second_intro(self)
        self.button = self.__next_to_task_button(self)
        