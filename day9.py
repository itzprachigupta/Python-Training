from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox
window=Tk()

#to set the size or geometry of our window 
window.geometry('350x200')

#to change the title of our window
window.title('Window')

#Label to print text on window and grid to place our text at position
label=Label(window,text='Hello World',font=('monotype corsiva',)).grid(row=0,column=0)
#font is used to give font style and size....font=("Font style",font_size)
l1=Label(window,text='Edureka')
l1.grid(row=1,column=0)

#textbox using Entry class
txt=Entry(window,width=20)
txt.grid(row=1,column=1)

#after clicking button and to add button click event
def clicked(): #fxn that will execute the button click event
    res="Welcome to Project"
    l1.configure(text= res)

#Button is used to create button and fg is used to change text color and bg is used to change back ground color of button
#wiring the button with fxn
bt=Button(window,text="Enter",command=clicked)
bt.grid(row=1,column=2)

#Combobox are drop down menus with options
combo=Combobox(window)
#adding the combobox items using tuple
combo['values']=['Select...',1,2,3,4,'text']
#select the selected item
combo.current(0)
combo.grid(row=2,column=1)

#to create a check button class where we can select more than one option at a time
chk_state=BooleanVar()
chk_state.set(True)
#passing the chk_state to the Checkbutton Class to set the check state
chk=Checkbutton(window,text="Choice",var=chk_state)
chk.grid(row=3,column=0)

#Radio button is used to create radio buttons where we can select only one option at a time
rad1=Radiobutton(window,text="Yes",value=1).grid(row=4,column=0)
rad2=Radiobutton(window,text="No",value=2).grid(row=4,column=1)
rad3=Radiobutton(window,text="Other",value=3).grid(row=4,column=2)

#ScrolledText is used to add scrolltext widget
txt=scrolledtext.ScrolledText(window,width=40,height=10)
txt.grid(column = 0, pady = 10, padx = 10)
txt.insert(INSERT,'''Be Happy This is a
scrolledtext 
widget to make tkinter 
text read 
only.
HiGeeks !!!
Geeks !!!
Geeks !!! 
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!''')
txt.configure(state ='disabled')
text_area = scrolledtext.ScrolledText(window,width = 40, height = 10, font = ("Times New Roman", 15)) 
text_area.grid(column = 0, pady = 10, padx = 10)
text_area.focus()
txt.focus()

#MessageBox is used to show message when button is clicked
def clicked():
    messagebox.showinfo('message title','message content')
bt1=Button(window,text="Submit",command=clicked)
bt1.grid(row=5,column=0)

#SpinBox is used to get both upper and down arrow 
spin=Spinbox(window,from_=0,to=100,width=5).grid(row=6,column=0)
window.mainloop()
