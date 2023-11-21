import tkinter as tk
from PIL import Image,ImageTk,ImageDraw
from screeninfo import get_monitors
#from subject import Subject

def initialize():
    screen_width,screen_height = get_monitors()[0].width,get_monitors()[0].height

    window = tk.Tk()
    window.geometry(str(screen_width)+'x'+str(screen_height))
    window.attributes('-fullscreen',True)
    canvas = tk.Canvas(window, width=screen_width, height=screen_height, bg='white')
    canvas.pack()
    return window