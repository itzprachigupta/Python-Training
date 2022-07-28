from email.mime import image
import tkinter

window =tkinter.Tk()
window.title("Day 9")

tkinter.Label(window,text='sufficient width',fg='white',bg='purple').pack()
tkinter.Label(window,text='taking all available x width ',fg='white',bg='green').pack(fill='x')
tkinter.Label(window,text='taking all available y width',fg='white',bg='blue').pack(fill='y')
tkinter.Label(window,text='taking all available y height',fg='white',bg='black').pack(side='left',fill='y')

window.mainloop()

