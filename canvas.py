from tkinter import *
root=Tk()

canvas_width=750
canvas_height=600
root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(750,600)
root.maxsize(750,600)

c_widget=Canvas(root,width=canvas_width,height=canvas_height,bg='black')
c_widget.place(x=0,y=0)
# c_widget.create_line(0,0,750,600,fill='blue')
# c_widget.create_line(750,0,0,600,fill='green')
# c_widget.create_rectangle(5,5,745,595,fill='aqua')
c_widget.create_line(0,0,750,600,fill='blue',width=10)
c_widget.create_line(750,0,0,600,fill='green',width=10)
c_widget.create_line(375,0,375,600,fill='yellow',width=10)
c_widget.create_line(0,300,750,300,fill='aqua',width=10)
# b1=Button(c_widget,text="info",bg='aqua',fg='black',font='calibri 12 bold',padx=50)
# b1.pack()
# img=PhotoImage(file='Screenshot (472).png')
# c_widget.create_image(10,10,image=img)
c_widget.create_oval(20,20,730,580,fill='orange red',outline='brown',width=10)
#c_widget.create_text(375,300,text='HELLO CANVAS',font='calibri 18 bold')
b1=Button(root,text='HELLO AMIGO,Press Here To Exit',bg='aqua',fg='black',font='calibri 12 bold',padx=10,pady=10,command=quit)
b1.place(x=260,y=280)

root.mainloop()