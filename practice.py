from tkinter import *
from tkinter.ttk import *
from random import *
import math
from config import *
import time
from PIL import Image, ImageTk

# Scale of user operable are
# Radisu = screen height/4*SCALE
SCALE = 0.9
# The minimum difference between mouse x and center x
# Avoids extremely large slope of line
MINIMUM_X_DIFF = 3

class Practice(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller
        # Frame.config(self,bg="white")
        # self.bg = "white"
        # Baseline task repetition counter

        self.label_intro = self.__label_intro(self)
        self.button = self.__start_task_button(self)
        self.canvas_w = self.winfo_screenwidth()
        self.canvas_h = self.winfo_screenheight()
        self.count = 1


        # Radius of operable circle
        self.radius = self.winfo_screenheight()/4*SCALE
        # Mouse coordinates
        self.mouse_x = 0
        self.mouse_y = 0

        # Size of full-screen canvas
        self.canvas_w = self.winfo_screenwidth()
        self.canvas_h = self.winfo_screenheight()
        

    def __label_intro(self,parent):
        label = Label(parent,text='''你做得很好！下面，我们来做一个实验练练手，检测一下你是否完全理解了指导
语的意思。单击鼠标右键继续。''',
                      font=("Arial", 25),
                      anchor="center")
        label.place(relx=instruction_relx, rely=instruction_rely, relwidth=instruction_relwidth, relheight=instruction_relheight,anchor = CENTER)
        return label
    
    def __start_task_button(self,parent):   
        btn = Button(parent, text="继续", takefocus=False, command = lambda : self.__set_up_task())
        btn.place(relx=next_button_relx, rely=next_button_rely, relwidth=next_button_relwidth, relheight=next_button_relheight)
        return btn


    def __set_up_task(self):
        self.label_intro.destroy()
        self.button.destroy()

        # Canvas instances
        self.canvas = self.__full_screen_canvas(self)
        
        # Reference line on canvas format(x1,y1,x2,y2)
        self.coords = self.__generate_coor_line(self.radius,self.canvas_w,self.canvas_h)
        self.line = self.__draw_line(self,self.coords)

        self.after(500)
        self.canvas.delete("all")
        self.canvas.destroy()
        self.button.destroy()
        image1 = Image.open("visual_masking.png")
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.place(relx=instruction_relx-(image1.size[0]/2)/self.canvas_w, rely=instruction_rely-(image1.size[1]/2)/self.canvas_h)
        self.after(500)
        label1.destroy()
        self.canvas = self.__full_screen_canvas(self)
        self.todo_coords = self.__generate_todo_coor_line(self.radius,self.canvas_w,self.canvas_h)
        self.todo_line = self.__draw_line(self,self.todo_coords)

        # Center coordinates of the canvas (not screen coordinates)
        self.center_x = self.canvas_w/2
        self.center_y = self.canvas_h/2 

        # User operable area indicator
        self.canvas.create_oval(self.canvas_w/2-self.radius,
                                      self.canvas_h/2-self.radius,
                                      self.canvas_w/2+self.radius,
                                      self.canvas_h/2+self.radius,
                                      width = 2,
                                      dash=(25,25),outline = 'white')

        self.canvas.bind("<B1-Motion>", self.__drag)
        
        # # Continue button instance
        self.button = self.__task_continue_button(self)

        self.todo_line_slope = 0
        # self.timer = self.after(ms_to_wait,self.__reset)

    def __full_screen_canvas(self,parent):
        cvs = Canvas(parent,
                     width=self.winfo_screenwidth(),
                     height=self.winfo_screenheight())
        cvs.place(x=self.winfo_screenwidth()/2,
                  y=self.winfo_screenheight()/2,
                  anchor="center")
        return cvs


    def __task_continue_button(self,parent):
        btn = Button(parent, text="继续", takefocus=False,command= lambda: self.__reset())
        btn.place(relx=next_button_relx, rely=next_button_rely, relwidth=next_button_relwidth, relheight=next_button_relheight)
        return btn
    
    
    def __draw_line(self,parent,coords):
            return self.canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=5)


    def __generate_coor_line(self,radius,w,h):
        theta = math.radians(randint(0,359))
        center_x = w/2
        center_y = h/2

        point1_x = center_x+math.cos(theta)*radius
        point1_y = center_y+math.sin(theta)*radius
        point2_x = center_x-math.cos(theta)*radius
        point2_y = center_y-math.sin(theta)*radius        
        return (point1_x,point1_y,point2_x,point2_y)
    
    def __generate_todo_coor_line(self,radius,w,h):
        center_x = w/2
        center_y = h/2
        point1_x = center_x+radius
        point1_y = center_y
        point2_x = center_x-radius
        point2_y = center_y        
        return (point1_x,point1_y,point2_x,point2_y)

    def __rotate_line(self,parent,x,y):
        if abs(x - self.center_x) <= MINIMUM_X_DIFF:
            # don't update the slope
            new_p1_x = self.center_x
            new_p2_x = self.center_x
            if y <= self.center_y:
                new_p1_y = self.center_y-self.radius
                new_p2_y = self.center_y+self.radius
            else:
                new_p1_y = self.center_y+self.radius
                new_p2_y = self.center_y-self.radius
            self.todo_line_slope = float('inf')
        else:
            slope = (y-self.center_y)/(x-self.center_x)
            theta = math.atan(slope)
            x_offset = math.cos(theta)*self.radius
            y_offset = math.sin(theta)*self.radius
            new_p1_x = self.center_x+x_offset
            new_p1_y = self.center_y+y_offset
            new_p2_x = self.center_x-x_offset
            new_p2_y = self.center_y-y_offset
            self.todo_line_slope = (self.center_y-y)/(x-self.center_x)
        self.canvas.delete(self.todo_line)
        self.todo_line = self.__draw_line(self,[new_p1_x,new_p1_y,new_p2_x,new_p2_y])    
    

    def __drag(self,event):
        if ((event.x-self.center_x)**2 + (event.y-self.center_y)**2) <= (self.radius**2):
            self.mouse_x = event.x
            self.mouse_y = event.y
            self.__rotate_line(self,self.mouse_x,self.mouse_y)


    def _is_good_result(self):
        if abs(self.coords[2]-self.coords[0]) < MINIMUM_X_DIFF:
            theta1 = math.atan(float('inf'))
        else:
            theta1 = math.atan((self.coords[1]-self.coords[3])/(self.coords[2]-self.coords[0]))
        theta2 = math.atan(self.todo_line_slope)
        return abs(theta1-theta2) < 10*math.pi/180
    

    def __reset(self):
        if not self._is_good_result():
            if self.count > 9:
                print("you did shit. Exit pls")
                # self.controller.show_frame("TestIntroGUI")
            else:
                self.canvas.delete("all")
                self.canvas.destroy()
                self.label_intro = self._try_again_label(self)
                self.button.destroy()
                self.button = self.__start_task_button(self)
            self.count += 1
        else:
            print("you did well")
            # self.controller.show_frame("TestIntroGUI")


    def _try_again_label(self,parent):
        label = Label(parent,text='''角度不相符，请按“继续”按钮再次尝试''',
            font=("Arial", 25),
            anchor="center")
        label.place(relx=instruction_relx, rely=instruction_rely, relwidth=instruction_relwidth, relheight=instruction_relheight,anchor = CENTER)
        return label
    

    def write_result_to_file(self,datafile):
        pass
