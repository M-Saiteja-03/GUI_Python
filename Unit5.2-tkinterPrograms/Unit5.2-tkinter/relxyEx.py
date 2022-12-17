from tkinter import *
root=Tk()
root. geometry("500x500")
t1=Entry(root,text="enter name",bg='yellow')
t2=Entry(root, bg="pink")
t1.place(x=50,y=50)
t2.place(relheight=0.7,relwidth=0.3)
root.mainloop()