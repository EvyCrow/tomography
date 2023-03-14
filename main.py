from tkinter import *
from math import *


R = 400
mmax = int(input("senior num detector ="))
M = 2*mmax+1
N = int(input("num of angles = "))
h = int(input("interval = "))

# window and canvas for drawing
size = 600
window = Tk()
canvas = Canvas(window, width=size, height=size)

x0 = 0
y0 = 0
canvas.create_oval([x0+0.5*R, y0+0.5*R], [x0+R, y0+R], fill="white", outline="red")

for n in range(0, N):
    phin = (pi*n)/N
    for m in range(-mmax, mmax):
        xs = -R*cos(phin)-m*h*sin(phin)
        ys = -R*sin(phin)+m*h*cos(phin)
        xd = R*cos(phin)-m*h*sin(phin)
        yd = R*sin(phin)+m*h*cos(phin)
        canvas.create_line(xs+300, ys+300, xd+300, yd+300, fill="yellow")

canvas.pack()
window.mainloop()
