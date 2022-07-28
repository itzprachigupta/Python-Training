#frame is usedto create divisions in the window, we can align frames like using side of pack() method
import tkinter
from tkinter import messagebox
window =tkinter.Tk()
window.title("Day 9 ")

#creating two frames TOP and BOTTOM
top_frame=tkinter.Frame(window).pack()
bottom_frame=tkinter.Frame(window).pack(side='bottom')

#some widgets in the top and bottom frame
btn1=tkinter.Button(top_frame,text="Button 1",fg='Red').pack()
btn2=tkinter.Button(top_frame,text="Button 2",fg='Green').pack()
btn3=tkinter.Button(bottom_frame,text="Button 3",fg='Purple').pack(side='left')
btn4=tkinter.Button(bottom_frame,text="Button 4",fg='Orange').pack(side='left')
def left(event):
    tkinter.messagebox.showinfo('Notification','Submitted')
def middle(event):
    tkinter.Label(window,text= "Middle Button").pack()
def right(event):
    tkinter.Label(window,text= "Right Button").pack()
butt=tkinter.Button(window,text="Submit")
butt.bind("<Button-1>",left)
butt.bind("<Button-2>",middle)
butt.bind("<Button-3>",right)
butt.pack()
window.mainloop()


