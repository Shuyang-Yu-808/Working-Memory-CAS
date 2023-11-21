import tkinter as tk
from PIL import Image,ImageTk,ImageDraw
root = tk.Tk()
root.geometry('400x300')
cv = tk.Canvas(root, width=400, height=300, bg='white')
cv.pack()
image1 = Image.new("RGB", (400, 300), 'white')#用来保存位图，宽、高和背景和cv必须相同
img = ImageTk.PhotoImage(image=image1)
mainImage=cv.create_image(200,150,image=img)#在Canvas上显示image1
draw = ImageDraw.Draw(image1)       #将用draw在image1上画图
#cv.itemconfig(mainImage,image=img)

def StartMove(event):    #开始建立一个Canvas图形实例
    global first_x,first_y    
    first_x,first_y = event.x,event.y
    cv.create_oval(event.x,event.y,event.x+2,event.y+2,tags=('L'),fill ='red',outline='green')
    
def OnMotion(event):    #鼠标移动，拖动这个Canvas图形实例改变形状
    global first_x,first_y
    cv.coords('L',first_x,first_y,event.x,event.y)
    
def StopMove(event):    #鼠标抬起，将所画图形保存到image1位图中，并在canvas上显示
    global first_x,first_y,img
    cv.coords('L',first_x,first_y,event.x,event.y)
    if ((abs(event.x-first_x)+abs(event.y-first_y))<6):#避免在窗体点一下，出一个点
        cv.delete('L')
        return        #下句在image1位图中画图形
    draw.ellipse((first_x,first_y,event.x,event.y),fill ='red',outline='green')
    img = ImageTk.PhotoImage(image=image1)
    cv.itemconfig(mainImage,image=img)   #在Canvas上显示image1 
    cv.delete('L')                       #删除开始建立的Canvas图形实例
    #image1.show()                       #用操作系统默认显示图形软件显示位图
    
cv.bind("<ButtonPress-1>",StartMove)  #绑定鼠标左键按下事件
cv.bind("<ButtonRelease-1>",StopMove) #绑定鼠标左键松开事件
cv.bind("<B1-Motion>", OnMotion)      #绑定鼠标左键被按下时移动鼠标事件
root.mainloop()