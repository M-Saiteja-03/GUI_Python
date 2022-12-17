from tkinter import *
root=Tk()
listbox=Listbox(root)
listbox.pack()
for i in range(11):
    listbox.insert(END,str(i))
root.mainloop()
