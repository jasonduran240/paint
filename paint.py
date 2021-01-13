from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageGrab, ImageTk
from tkinter import messagebox

root = Tk()
root.title('Paint by Jason Duran')
# root.iconbitmap('paint1.ico')
root.geometry('800x750')

brush_color = 'black'


def paint(e):
    # Brush parameters
    brush_width = '%0.0f' % float(my_slider.get())
    # brush_color = "green"
    # brush type: BUTT, ROUND, PROJECTING
    brush_type2 = brush_type.get()

    # Starting position
    x1 = e.x - 1
    y1 = e.y - 1

    # Ending position
    x2 = e.x + 1
    y2 = e.y + 1

    # Draw on the canvas
    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type2, smooth=True)


# change the size of the brush
def change_brush_size(thing):
    slider_label.config(text='%0.0f' % float(my_slider.get()))


def change_brush_color():
    global brush_color
    brush_color = 'black'
    brush_color = colorchooser.askcolor(color=brush_color)[1]


def canva_color():
    global backgroung_color
    background_color = 'black'
    backgroung_color = colorchooser.askcolor(color=background_color)[1]
    my_canvas.config(bg=backgroung_color)


# clear screen
def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg="white")


# save image
def save_as_png():
    result = filedialog.asksaveasfilename(initialdir='c:/paint/images', filetypes=(
        ('png', '*.png'), ('all files', '*.*')))

    if result.endswith('.png'):
        pass
    else:
        result += '.png'

    if result:
        x = root.winfo_rootx() + my_canvas.winfo_rootx()
        y = root.winfo_rooty() + my_canvas.winfo_rooty()
        x1 = x + my_canvas.winfo_width()
        y1 = y + my_canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(result)

        # pop up success message
        messagebox.showinfo("Image Saved", "Your image has been saved")


# create our canvas
w = 600
h = 400

my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)

# my_canvas.create_line(0, 100, 300, 100, fill="red")
# my_canvas.create_line(150, 0, 150, 200, fill="red")

# <B1-Motion> left click cursor
my_canvas.bind('<B1-Motion>', paint)

# create brush options frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=10)

# brush size
brush_size_frame = LabelFrame(brush_options_frame, text='Brush Size')
brush_size_frame.grid(row=0, column=0, padx=50)

# brush slider
my_slider = ttk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)

# Brush slider label
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=10)

# Brush Type
brush_type_frame = LabelFrame(brush_options_frame, text='Brush Type', height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set("round")

brush_type_radio1 = Radiobutton(brush_type_frame, text="Round", variable=brush_type, value="round")
brush_type_radio2 = Radiobutton(brush_type_frame, text="Slash", variable=brush_type, value="butt")
brush_type_radio3 = Radiobutton(brush_type_frame, text="Diamond", variable=brush_type, value="projecting")

brush_type_radio1.pack(anchor="w")
brush_type_radio2.pack(anchor="w")
brush_type_radio3.pack(anchor="w")

# change color
change_colors_frame = LabelFrame(brush_options_frame, text='Change colors')
change_colors_frame.grid(row=0, column=2)

# change brush color button
brush_color_button = Button(change_colors_frame, text='Brush Color', command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

# change background color
canvas_color_button = Button(change_colors_frame, text='Canva Color', command=canva_color)
canvas_color_button.pack(pady=10, padx=10)

# Program Options Frame
options_frame = LabelFrame(brush_options_frame, text='Program Options')
options_frame.grid(row=0, column=3, padx=50)

# clear screen button
clear_button = Button(options_frame, text='Clear Screen', command=clear_screen)
clear_button.pack(padx=10, pady=10)

# save image

save_image_button = Button(options_frame, text='Save To PNG', command=save_as_png)
save_image_button.pack(padx=10, pady=10)
root.mainloop()
