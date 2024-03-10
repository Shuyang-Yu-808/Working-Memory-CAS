import tkinter as tk
# import tkmacosx as tk
import tkinter.ttk as ttk

from random import *
import math
import time
from PIL import Image, ImageTk
# from tkmacosx import Button as macTkButton
from config import conf



class MainTaskGUI (tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg = conf.canvas_color)
        self.controller = controller
        self.label_intro = self.__label_intro(self)
        self.button = self.__start_task_button(self)
        self.canvas_w = self.winfo_screenwidth()
        self.canvas_h = self.winfo_screenheight()
        self.count = 1

        self.target_index = -1
        self.target_color = ""

        # Radius of operable circle
        self.radius = self.winfo_screenheight()/4*conf.scale

        # Radius of reference lines
        self.ref_line_radius = self.winfo_screenheight()/4*conf.scale/2

        # Mouse coordinates
        self.mouse_x = 0
        self.mouse_y = 0

        # Size of full-screen canvas
        self.canvas_w = self.winfo_screenwidth()
        self.canvas_h = self.winfo_screenheight()
        
    def __exit_button(self,parent):   
        btn = tk.Button(parent, text="退出", fg = conf.button_text_color, bg = conf.button_bg_color, takefocus=False, command = lambda : self.controller.exit())
        btn.place(relx=conf.next_button_relx,
                  rely=conf.next_button_rely,
                  relwidth=conf.next_button_relwidth,
                  relheight=conf.next_button_relheight)
        return btn
    
    def __label_intro(self,parent):
        label = tk.Label(parent,text='''目前为止你做得都很好！下面我们正式进入实验，加油！点击“开始”按钮继续。''',
                      font=conf.label_font,
                      anchor="center",fg = conf.label_text_color,bg = conf.canvas_color)
        label.place(relx=conf.instruction_relx,
                    rely=conf.instruction_rely,
                    anchor=tk.CENTER,
                    relwidth=conf.instruction_relwidth,
                    relheight=conf.instruction_relheight)
        return label
    
    def __start_task_button(self,parent):   
        btn = tk.Button(parent, text="开始", fg = conf.button_text_color, bg = conf.button_bg_color, takefocus=False, command = lambda : self.__set_up_task())
        # btn = macTkButton(parent, text="开始", fg = conf.button_text_color, bg = conf.button_bg_color, takefocus=False, command = lambda : self.__set_up_task())
       
        btn.place(relx=conf.next_button_relx,
                  rely=conf.next_button_rely,
                  relwidth=conf.next_button_relwidth,
                  relheight=conf.next_button_relheight)
        return btn


    def __set_up_task(self):
        self.label_intro.destroy()
        self.button.destroy()

        # Canvas instances
        self.canvas = self.__full_screen_canvas(self)
        
        # Reference line on canvas format(x1,y1,x2,y2)
        self.ref_line_coords = self.__generate_coor_ref_lines(self.ref_line_radius,self.canvas_w,self.canvas_h)
        random_list = sample(range(0, 5), 3)
        self.color_list = {}
        self.color_list['alpha'] = conf.color_list[random_list[0]]
        self.color_list['beta'] = conf.color_list[random_list[1]]
        self.color_list['gamma'] = conf.color_list[random_list[2]]
        self.ref_line1 = self.__draw_line(self,self.ref_line_coords[:4],self.color_list['alpha'])
        self.ref_line2 = self.__draw_line(self,self.ref_line_coords[4:8],self.color_list['beta'])
        self.ref_line3 = self.__draw_line(self,self.ref_line_coords[8:],self.color_list['gamma'])


        self.after(500,lambda: self.__show_mask())

    def __show_mask(self):
        self.canvas.delete("all")
        self.canvas.destroy()
        self.button.destroy()
        self.canvas = self.__full_screen_canvas(self)
        image1 = Image.open("visual_masking.png")
        test = ImageTk.PhotoImage(image1)
        label1 = tk.Label(image=test)
        label1.image = test
        label1.config(highlightthickness=0)
        label1.place(relx=conf.instruction_relx-(image1.size[0]/2)/self.canvas_w, rely=conf.instruction_rely-(image1.size[1]/2)/self.canvas_h)
        self.after(500,lambda: self.__show_todo(label1))

    def __show_todo(self,label1):
        label1.destroy()
        self.canvas = self.__full_screen_canvas(self)

        self.todo_coords = self.__generate_todo_coor_line(self.radius,self.canvas_w,self.canvas_h)
        self.target_index = randint(0,2)
        self.target_color = self.color_list[['alpha','beta','gamma'][self.target_index]]

        self.todo_line = self.__draw_line(self,self.todo_coords,self.target_color)
        # Center coordinates of the canvas (not screen coordinates)
        self.center_x = self.canvas_w/2
        self.center_y = self.canvas_h/2 

        # User operable area indicator
        self.canvas.create_oval(self.canvas_w/2-self.radius,
                                      self.canvas_h/2-self.radius,
                                      self.canvas_w/2+self.radius,
                                      self.canvas_h/2+self.radius,
                                      width = 2,
                                      dash=(conf.pixels_between_dash,conf.pixels_between_dash))

        self.canvas.bind("<B1-Motion>", self.__drag)
        # print(self.count)        
        # # Continue button instance
        self.button = self.__task_continue_button(self)

        self.todo_line_slope = 0
        # self.timer = self.after(ms_to_wait,self.__reset)

    def __full_screen_canvas(self,parent):
        cvs = tk.Canvas(parent,
                     width=self.winfo_screenwidth(),
                     height=self.winfo_screenheight(), bg=conf.canvas_color)
        cvs.place(x=self.winfo_screenwidth()/2,
                  y=self.winfo_screenheight()/2,
                  anchor="center")
        return cvs


    def __task_continue_button(self,parent):
        btn = tk.Button(parent, text="继续",fg = conf.button_text_color,bg = conf.button_bg_color, takefocus=False,command= lambda: self.__reset())
        # btn = macTkButton(parent, text="继续",bg = "grey", fg = "white",takefocus=False,command= lambda: self.__reset())
        btn.place(relx=conf.next_button_relx,
                  rely=conf.next_button_rely,
                  relwidth=conf.next_button_relwidth,
                  relheight=conf.next_button_relheight)
        return btn
    
    
    def __draw_line(self,parent,coords,color="black"):
        return self.canvas.create_line(coords[0],coords[1],coords[2],coords[3],width=5,fill=color)

    def __generate_coor_ref_lines(self,radius,w,h):
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
    

    def __generate_todo_coor_line(self,radius,w,h):
        center_x = w/2
        center_y = h/2
        point1_x = center_x+radius
        point1_y = center_y
        point2_x = center_x-radius
        point2_y = center_y        
        return (point1_x,point1_y,point2_x,point2_y)

    def __rotate_line(self,parent,x,y):
        if abs(x - self.center_x) <= conf.minimum_x_diff:
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
        self.todo_line = self.__draw_line(self,[new_p1_x,new_p1_y,new_p2_x,new_p2_y],self.target_color)    
    

    def __drag(self,event):
        if ((event.x-self.center_x)**2 + (event.y-self.center_y)**2) <= (self.radius**2):
            self.mouse_x = event.x
            self.mouse_y = event.y
            self.__rotate_line(self,self.mouse_x,self.mouse_y)


    def _update_result(self):
        self.target_coords = self.ref_line_coords[self.target_index*4:self.target_index*4+4]
        if abs(self.target_coords[2]-self.target_coords[0]) < conf.minimum_x_diff:
            theta1 = math.atan(float('inf'))
        else:
            theta1 = math.atan((self.target_coords[1]-self.target_coords[3])/(self.target_coords[2]-self.target_coords[0]))
        theta2 = math.atan(self.todo_line_slope)
        self.controller.subject.maintask_error.append(abs(theta1-theta2))
    

    def __reset(self):
        self._update_result()
        self.count +=1
        if self.count > conf.n_test_set_three_line:
            self.canvas.delete("all")
            self.canvas.destroy()
            self.button.destroy()
            self.label_intro = self._label_ending(self)
            self.button = self.__exit_button(self)
        elif self.count == conf.n_test_set_three_line//2 + 1:
            self.canvas.delete("all")
            self.canvas.destroy()
            self.button.destroy()
            self.label_intro = self._label_take_a_break(self)
            self.button = self.__start_task_button(self)
        else:
            self.canvas.delete("all")
            self.canvas.destroy()
            self.button.destroy()
            self.__set_up_task()


    def _label_take_a_break(self,parent):
        label = tk.Label(parent,text='''目前为止你做得很好！现在闭目或远眺休息眼睛，若感觉状态回复则可点击“开始”按钮继续。''',
                      font=conf.label_font,
                      anchor="center",bg = "grey",fg = "white")
        label.place(relx=conf.instruction_relx,
                            rely=conf.instruction_rely,
                            anchor=tk.CENTER,
                            relwidth=conf.instruction_relwidth,
                            relheight=conf.instruction_relheight)
        return label


    def _label_ending(self,parent):
        label = tk.Label(parent,text='''实验结束！再次感谢你参与本次心理学实验！。''',
                      font=conf.label_font,
                      anchor="center",bg = "grey",fg = "white")
        label.place(relx=conf.instruction_relx,
                    rely=conf.instruction_rely,
                    anchor=tk.CENTER,
                    relwidth=conf.instruction_relwidth,
                    relheight=conf.instruction_relheight)
        return label
