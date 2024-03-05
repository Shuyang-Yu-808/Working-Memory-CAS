import tkinter as tk
from tkinter.ttk import *
from random import *
import math

from config import conf
class BaseBodyGUI(Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg = conf.canvas_color)
        self.controller = controller
        self.target_index = -1
        self.target_color = ""
        self.label_intro = self.__label_first_intro(self)
        self.button = self.__button_change_label(self)


    def __label_first_intro(self,parent):
        label = tk.Label(parent,text='''接下来，请你完成一些小任务，帮助你更好地完成后续的正式实验。请点击“继续”按钮。''',
                      font=conf.label_font,
                      anchor="center",
                      fg = conf.label_text_color,bg = conf.canvas_color)
        label.place(relx=conf.instruction_relx,
                    rely=conf.instruction_rely,
                    anchor=tk.CENTER,
                    relwidth=conf.instruction_relwidth,
                    relheight=conf.instruction_relheight)
        return label
    

    def __label_second_intro(self,parent):
        label = tk.Label(parent,text='''接下来，屏幕上半部分中央会显示三个不同颜色、随机朝向的线段。
请你用鼠标调整下方的线段直至和上方对应的颜色的一样，按“继续”按钮继续，这个过程会重复10次。''',
                      font=conf.label_font,
                      anchor="center",
                      fg = conf.label_text_color,bg = conf.canvas_color)
        label.place(relx=conf.instruction_relx,
                    rely=conf.instruction_rely,
                    anchor=tk.CENTER,
                    relwidth=conf.instruction_relwidth,
                    relheight=conf.instruction_relheight)
        return label

    '''
    Canvas on the upper screen
    '''
    def __canvas_upper(self,parent):
        cvs = tk.Canvas(parent,
                     width=self.winfo_screenwidth(),
                     height=self.winfo_screenheight()/2,bg=conf.canvas_color)
        cvs.config(highlightthickness=0)
        cvs.place(x=self.winfo_screenwidth()/2,
                  y=self.winfo_screenheight()*(1/4),
                  anchor="center")
        return cvs

    '''
    Canvas on the lower screen
    '''
    def __canvas_lower(self,parent):
        cvs = tk.Canvas(parent,
                     width=self.winfo_screenwidth(),
                     height=self.winfo_screenheight()/2,bg=conf.canvas_color)
        cvs.config(highlightthickness=0)
        cvs.place(x=self.winfo_screenwidth()/2,
                  y=self.winfo_screenheight()*(3/4),
                  anchor="center")
        return cvs
    

    '''
    Button that sets up the baseline test
    '''
    def __button_start_task(self,parent):   
        btn = tk.Button(parent, text="开始", takefocus=False, command = lambda : self.__set_up_baseline_task(),
                        fg = conf.button_text_color,bg = conf.button_bg_color)
        btn.place(relx=conf.next_button_relx,
                  rely=conf.next_button_rely,
                  relwidth=conf.next_button_relwidth,
                  relheight=conf.next_button_relheight)
        return btn


    '''
    Button that resets the baseline test
    '''
    def __button_repeat_task(self,parent):
        btn = tk.Button(parent, text="继续", takefocus=False,command= lambda: self.__reset(),
                    fg = conf.button_text_color,bg = conf.button_bg_color)
        btn.place(relx=conf.next_button_relx,
                  rely=conf.next_button_rely,
                  relwidth=conf.next_button_relwidth,
                  relheight=conf.next_button_relheight)
        return btn
    
    '''
    Button that calls to change label text
    '''
    def __button_change_label(self,parent):
        btn = tk.Button(parent, text="继续", takefocus=False,command= lambda : self.__change_instruction(),
                        fg = conf.button_text_color,bg = conf.button_bg_color)
        btn.place(relx=conf.next_button_relx,
                  rely=conf.next_button_rely,
                  relwidth=conf.next_button_relwidth,
                  relheight=conf.next_button_relheight)
        return btn    

    '''
    Initialize a baseline test
    1. New mouse coordinates
    2. New widgets
    '''
    def __set_up_baseline_task(self):
        self.label_intro.destroy()
        self.button.destroy()
        # Baseline test repetition counter
        self.count = 1
        # Radius of operable circle
        self.radius = self.winfo_screenheight()/4*conf.scale
        self.upper_lines_radius = self.winfo_screenheight()/4*conf.scale/2
        # Mouse coordinates
        self.mouse_x = 0
        self.mouse_y = 0

        # Size of half-screen canvas
        self.canvas_w = self.winfo_screenwidth()
        self.canvas_h = self.winfo_screenheight()/2
        
        # Canvas instances
        self.upper_canvas = self.__canvas_upper(self)
        self.lower_canvas = self.__canvas_lower(self)
        
        # Reference line on upper canvas format(x1,y1,x2,y2)
        self.upper_coords = self.__generate_coor_upper_lines(self.upper_lines_radius,self.canvas_w,self.canvas_h)
        random_list = sample(range(0, 5), 3)
        color_list = {}
        color_list['alpha'] = conf.color_list[random_list[0]]
        color_list['beta'] = conf.color_list[random_list[1]]
        color_list['gamma'] = conf.color_list[random_list[2]]
        self.upper_line1 = self.__draw_line(self,self.upper_coords[:4],'upper',color_list['alpha'])
        self.upper_line2 = self.__draw_line(self,self.upper_coords[4:8],'upper',color_list['beta'])
        self.upper_line3 = self.__draw_line(self,self.upper_coords[8:],'upper',color_list['gamma'])


        # Operable line on lower canvas
        self.lower_coords = self.__generate_coor_lower_line(self.radius,self.canvas_w,self.canvas_h)
        self.target_index = randint(0,2)
        self.target_color = color_list[['alpha','beta','gamma'][self.target_index]]

        self.lower_line = self.__draw_line(self,self.lower_coords,'lower',self.target_color)

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
        self.button = self.__button_repeat_task(self)
        self.base_result = []
        self.lower_line_slope = 0
        self.timer = self.after(conf.ms_to_wait,self.__reset)
        
    '''
    Draws a line with specified:
    1. parent (this frame)
    2. widget it's in (canvas)
    3. coordinates (absolute coordinates within a canvas)
    '''
    def __draw_line(self,parent,coords,canvas,color="black"):
        if canvas == "upper":
            return self.upper_canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=5,fill=color)
        elif canvas == 'lower':
            return self.lower_canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=5,fill=color)
        
    '''
    Creates the coordinates of a random line on the upper canvas
    The line goes through the center of the upper canvas
    '''
    def __generate_coor_upper_lines(self,radius,w,h):
        # random radian number
        theta1 = math.radians(randint(0,359))
        theta2 = math.radians(randint(0,359))
        theta3 = math.radians(randint(0,359))

        # center of the upper canvas
        
        line1_center_x = w/5*1.5
        line2_center_x = w/5*2.5
        line3_center_x = w/5*3.5
        lines_center_y = h/2
        # diagonal coordiantes that specifies an oval
        line1_point1_x = line1_center_x+math.cos(theta1)*radius
        line1_point1_y = lines_center_y+math.sin(theta1)*radius
        line1_point2_x = line1_center_x-math.cos(theta1)*radius
        line1_point2_y = lines_center_y-math.sin(theta1)*radius        


        line2_point1_x = line2_center_x+math.cos(theta2)*radius
        line2_point1_y = lines_center_y+math.sin(theta2)*radius
        line2_point2_x = line2_center_x-math.cos(theta2)*radius
        line2_point2_y = lines_center_y-math.sin(theta2)*radius

        line3_point1_x = line3_center_x+math.cos(theta3)*radius
        line3_point1_y = lines_center_y+math.sin(theta3)*radius
        line3_point2_x = line3_center_x-math.cos(theta3)*radius
        line3_point2_y = lines_center_y-math.sin(theta3)*radius                
        return (line1_point1_x,line1_point1_y,line1_point2_x,line1_point2_y,
                line2_point1_x,line2_point1_y,line2_point2_x,line2_point2_y,
                line3_point1_x,line3_point1_y,line3_point2_x,line3_point2_y)
    
    
    '''
    Creates the coordinates of a horizontal line on the lower canvas
    The line goes through the center of the operable circle (and the lower canvas)
    '''
    def __generate_coor_lower_line(self,radius,w,h):
        # horizontal
        theta = math.radians(0)

        # center of the upper canvas
        center_x = w/2
        center_y = h/2
        
        # diagonal coordiantes that specifies an oval
        point1_x = center_x+radius
        point1_y = center_y
        point2_x = center_x-radius
        point2_y = center_y        
        return (point1_x,point1_y,point2_x,point2_y)
    
    '''
    Rotates the line on the lower canvas
    1. Delete the original line
    2. Draws a line to the current mouse coordinates if x is conf.minimum_x_diff pixels away from the center
        (Avoids inifinite slope)
    3. Draws a vertical line if x isn't conf.minimum_x_diff pixels away from the center
    '''
    def __rotate_lower_line(self,parent,x,y):
        if abs(x - self.lower_center_x) <= conf.minimum_x_diff:
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
        self.lower_line = self.__draw_line(self,[new_p1_x,new_p1_y,new_p2_x,new_p2_y],"lower",self.target_color)    
    
    '''
    Detects mouse drag events inside the operable circle on the lower canvas
    Updates mouse coordinates
    Calls to rotate the line on the lower canvas
    '''
    def __drag(self,event):
        if ((event.x-self.lower_center_x)**2 + (event.y-self.lower_center_y)**2) <= (self.radius**2):
            self.mouse_x = event.x
            self.mouse_y = event.y
            self.__rotate_lower_line(self,self.mouse_x,self.mouse_y)
    
    '''
    Calculates baseline test result
    Saves the result as class attribute
    '''
    def _update_base_result(self,slope1,slope2):
        theta1 = math.atan(slope1)
        theta2 = math.atan(slope2)
        self.base_result.append(abs(theta1-theta2))

    '''
    Resets the current baseline test to its initial state
    Starts a new baseline test
    1. Calls the timer and resets the current baseline time if exceeds time limit
    2. Records a vertical slope if slope is greater than minimum x coordinate difference
    3. Calculates the slope if less than minimum x coordinate difference
    4. Transits to the next frame if 10 baseline tests are completed
    5. Saves the baseline test error
    '''
    def __reset(self): 
        self.after_cancel(self.timer)
        self.target_coords = self.upper_coords[self.target_index*4:self.target_index*4+4]
        if abs(self.target_coords[2]-self.target_coords[0]) < conf.minimum_x_diff: # Global in baseline.py
            self._update_base_result(float('inf'),self.lower_line_slope)
        else:
            self._update_base_result((self.target_coords[1]-self.target_coords[3])/(self.target_coords[2]-self.target_coords[0]),self.lower_line_slope)

        if self.count >= 10:
            self.__save()
            self.controller.show_frame("PracticeGUI")
                    
        elif self.count < 10:
            self.mouse_x = 0
            self.mouse_y = 0

            self.upper_canvas.delete(self.upper_line)
            self.upper_coords = self.__generate_coor_upper_line(self.radius,self.canvas_w,self.canvas_h)
            self.upper_line = self.__draw_line(self,self.upper_coords,'upper')

            self.lower_canvas.delete(self.lower_line)
            self.lower_coords = self.__generate_coor_lower_line(self.radius,self.canvas_w,self.canvas_h)
            self.lower_line = self.__draw_line(self,self.lower_coords,'lower')
            self.timer = self.after(conf.ms_to_wait,self.__reset)
        self.count += 1

    '''
    Exports baseline data to attribute subject that is stored in the window instance
    '''
    def __save(self):
        self.controller.subject.baseline_error = self.base_result

    '''
    Switches to the second part of the intro
    Creates the button to start the tests
    '''
    def __change_instruction(self):
        self.label_intro.destroy()
        self.button.destroy()
        self.label_intro = self.__label_second_intro(self)
        self.button = self.__button_start_task(self)
        