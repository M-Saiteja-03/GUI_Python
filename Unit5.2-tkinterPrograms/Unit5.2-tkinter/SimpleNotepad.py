from tkinter import *
root=Tk()
root.title("Simple Notepad")
# create menu bar
menubar=Menu(root)
#create sub menus
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
#filemenu.add_separator()
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)
# create Edit menu
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="undo")
editmenu.add_command(label="paste")
editmenu.add_command(label="copy")
editmenu.add_command(label="cut")
menubar.add_cascade(label='Edit',menu=editmenu)


root.config(menu=menubar)
root.mainloop()