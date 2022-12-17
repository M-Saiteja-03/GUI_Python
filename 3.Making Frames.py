from tkinter import *
root=Tk()

root.geometry("750x630")
f1=Frame(root,bg="green",borderwidth=10,relief=SUNKEN,padx=80)
f1.pack(side=TOP)
l=Label(f1,text="MY FRAME USING PYTHON(PYCHARM)",font="Helvetica 14 bold")
l.pack()

f2=Frame(root,bg="black",borderwidth=6,padx=50,relief= GROOVE)
f2.pack(side=LEFT,anchor='nw',fill='y')
l=Label(f2,text="MyProjects",font="calibri 12 bold",bg="orange")
l.pack(side=TOP)

f3=Frame(root,borderwidth=5,bg="teal")
f3.pack(side=TOP,anchor='nw')
l=Label(f3,text="file",font="calibri 12 bold",bg='aqua')
l.pack()

photo=PhotoImage(file="Screenshot (472).png")
HR=Label(image=photo)
HR.pack()


root.mainloop()


# from tkinter import *
# root = Tk()
# root.geometry("655x333")
# f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
# f1.pack(side=LEFT, fill="y")
#
# f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
# f2.pack(side=TOP, fill="x")
#
# l = Label(f1, text="Project Tkinter - Pycharm")
# l.pack( pady=142)
#
# l = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="red", pady=22)
# l.pack()
#
# root.mainloop()