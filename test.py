'''# import everything from tkinter module
from tkinter import *

root = Tk()

root.geometry('430x300')

title = Label(root, text="Geeksforgeeks", bg="green", font=("bold", 30))
title.pack()
c = Canvas(root, width=330, height=200, bg="red")
c.pack()
btn = Button(root, text='Welcome to Tkinter!', width=40,
			height=5, bd='10')

btn.pack()

root.mainloop()'''
'''from tkinter import *
root=Tk()
root.geometry('750x600')
def get():
	print(e1.get())
e1=Entry(root)
e1.pack()
b1=Button(root,text='submit',command=get)
b1.pack()
root.mainloop()'''
from tkinter import *
root=Tk()
root.geometry('150x100')
v=IntVar()
v.set(-1)
r1=Radiobutton(root,text='C',variable=v,value=0)
r1.pack(anchor='nw')
r2=Radiobutton(root,text='Python',variable=v,value=1)
r2.pack(anchor='nw')
print(v.get())
print(v.get())
root.mainloop()
