from tkinter import *
import tkinter.messagebox as mbox
root=Tk()
canvas_width=750
canvas_height=600
root.geometry(f"{canvas_width}x{canvas_height}")
root.minsize(750,600)
root.maxsize(750,600)
def msg():
    mbox.showinfo('INFO','''HELLO AMIGOS, WELCOME TO MY GUI
                        THIS IS MADE BY M.SAITEJA''')
    mbox.askquestion('RATING','DID U LIKE THIS GUI?')

c_widget=Canvas(root,width=canvas_width,height=canvas_height,bg='black')
c_widget.place(x=0,y=0)
c_widget.create_line(0,0,750,600,fill='blue',width=10)
c_widget.create_line(750,0,0,600,fill='green',width=10)
c_widget.create_line(375,0,375,600,fill='yellow',width=10)
c_widget.create_line(0,300,750,300,fill='aqua',width=10)
c_widget.create_oval(20,20,730,580,fill='orange red',outline='brown',width=10)
b1=Button(root,text='CLICK HERE',bg='aqua',fg='black',font='calibri 12 bold',padx=10,pady=10,command=msg)
b1.place(x=320,y=260)
b2=Button(root,text='EXIT',bg='aqua',fg='black',font='calibri 12 bold',padx=30,pady=10,command=quit)
b2.place(x=320,y=330)
root.title("Saiteja's editor" )
mainmenu=Menu(root)
filemenu=Menu(mainmenu,tearoff=0)
filemenu.add_command(label='New Project...',activebackground='black',font='calibri 12 bold',activeforeground='yellow')
filemenu.add_command(label='New...',activebackground='black',font='calibri 12 bold',activeforeground='yellow')
filemenu.add_separator()
filemenu.add_command(label='Save...      Ctrl+S',activebackground='black',font='calibri 12 bold',activeforeground='yellow')
filemenu.add_command(label='Save As...  Ctrl+Shift+S',activebackground='black',font='calibri 12 bold',activeforeground='yellow')
mainmenu.add_cascade(label='File',menu=filemenu,font='calibri 12 bold')

editmenu=Menu(mainmenu,tearoff=0)
editmenu.add_command(label='Cut',activebackground='black',activeforeground='yellow',font='calibri 12 bold')
editmenu.add_command(label='Copy',activebackground='black',font='calibri 12 bold',activeforeground='yellow')
editmenu.add_command(label='Paste',activebackground='black',font='calibri 12 bold',activeforeground='yellow')
mainmenu.add_cascade(label='Edit',menu=editmenu)


root.config(menu=mainmenu)

root.mainloop()
