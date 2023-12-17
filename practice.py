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
        label = Label(parent,text='''目前为止你做得都很好！下面我们正式进入实验，加油！点击“开始”按钮继续。''',
                      font=("Arial", 25),
                      anchor="center")
        label.place(relx=instruction_relx, rely=instruction_rely, relwidth=instruction_relwidth, relheight=instruction_relheight,anchor = CENTER)
        return label
    
    def __start_task_button(self,parent):   
        btn = Button(parent, text="开始", takefocus=False, command = lambda : self.__set_up_task())
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
        self.canvas.delete(self.line)
        image1 = Image.open("visual_masking.png")
        test = ImageTk.PhotoImage(image1)
        label1 = Label(image=test)
        label1.image = test
        label1.place(relx=instruction_relx, rely=instruction_rely)


        # # Operable line on lower canvas
        # self.lower_coords = self.__generate_coor_lower_line(self.radius,self.canvas_w,self.canvas_h)
        # self.lower_line = self.__draw_line(self,self.lower_coords,'lower')

        # # Center coordinates of lower canvas (not screen coordinates)
        # self.lower_center_x = self.canvas_w/2
        # self.lower_center_y = self.winfo_screenheight()/4 

        # # User operable area indicator
        # self.lower_canvas.create_oval(self.canvas_w/2-self.radius,
        #                               self.canvas_h/2-self.radius,
        #                               self.canvas_w/2+self.radius,
        #                               self.canvas_h/2+self.radius,
        #                               width = 2,
        #                               dash=(10,10))

        # self.lower_canvas.bind("<B1-Motion>", self.__drag)
        
        # # Continue button instance
        # self.button = self.__task_continue_button(self)
        # self.base_result = []
        # self.lower_line_slope = 0
        # self.timer = self.after(ms_to_wait,self.__reset)

    def __full_screen_canvas(self,parent):
        cvs = Canvas(parent,
                     width=self.winfo_screenwidth(),
                     height=self.winfo_screenheight(),bg='#fff')
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
        # print("upper center x ",center_x)
        # print("upper center y ",center_y)

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
            self.lower_line_slope = float('inf')
        else:
            slope = (y-self.lower_center_y)/(x-self.lower_center_x)
            theta = math.atan(slope)
            x_offset = math.cos(theta)*self.radius
            y_offset = math.sin(theta)*self.radius
            new_p1_x = self.lower_center_x+x_offset
            new_p1_y = self.lower_center_y+y_offset
            new_p2_x = self.lower_center_x-x_offset
            new_p2_y = self.lower_center_y-y_offset
            self.lower_line_slope = (self.lower_center_y-y)/(x-self.lower_center_x)
        self.lower_canvas.delete(self.lower_line)
        self.lower_line = self.__draw_line(self,[new_p1_x,new_p1_y,new_p2_x,new_p2_y],"lower")    
    
    def __drag(self,event):
        if ((event.x-self.lower_center_x)**2 + (event.y-self.lower_center_y)**2) <= (self.radius**2):
            self.mouse_x = event.x
            self.mouse_y = event.y
            self.__rotate_lower_line(self,self.mouse_x,self.mouse_y)

    def _update_base_result(self,slope1,slope2):
        theta1 = math.atan(slope1)
        # print("theta 1",theta1)
        theta2 = math.atan(slope2)
        # print("theta 2",theta2)

        self.base_result.append(abs(theta1-theta2))


    def __reset(self):
        # print(self.count)
        # print("upper coords",self.upper_coords)
        # print("lower coords",self.lower_coords)
        self.after_cancel(self.timer)

        if abs(self.upper_coords[2]-self.upper_coords[0]) < MINIMUM_X_DIFF:
            # print("in")
            self._update_base_result(float('inf'),self.lower_line_slope)
        else:
            self._update_base_result((self.upper_coords[1]-self.upper_coords[3])/(self.upper_coords[2]-self.upper_coords[0]),self.lower_line_slope)
        
        if self.count >= 10:
            # TODO: save result to json file locally 
            print(self.base_result)
            self.controller.show_frame("TestIntroGUI")
                    
        elif self.count < 10:
            self.mouse_x = 0
            self.mouse_y = 0

            self.upper_canvas.delete(self.upper_line)
            self.upper_coords = self.__generate_coor_upper_line(self.radius,self.canvas_w,self.canvas_h)
            self.upper_line = self.__draw_line(self,self.upper_coords,'upper')

            self.lower_canvas.delete(self.lower_line)
            self.lower_coords = self.__generate_coor_lower_line(self.radius,self.canvas_w,self.canvas_h)
            self.lower_line = self.__draw_line(self,self.lower_coords,'lower')
            self.timer = self.after(ms_to_wait,self.__reset)

            # self.button = self.__end_baseline_button(self)

        self.count += 1

    def write_result_to_file(self,datafile):
        pass
