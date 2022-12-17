from tkinter import *
root=Tk()
t1=Entry(root)
t1.pack()
t2=Entry(root,show="*")
t2.pack()
def myClick():
    label1=Label(root, text="Hello your name is "+t1.get())
    label1.pack(fill=Y,expand=1)
    label2=Label(root,text="Hello password is "+t2.get())
    label2.pack()
b1 = Button(root, text="Enter your name and password", command=myClick)
b1.pack()
root.mainloop()