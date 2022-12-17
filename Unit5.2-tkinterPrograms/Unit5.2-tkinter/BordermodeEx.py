from tkinter import *
root=Tk()
f1=Frame(root,borderwidth=10,relief=GROOVE,width=100,height=100)
f1.pack()
l1=Label(f1,text="Hi").place(x=5,y=5,bordermode="inside")
root.mainloop()