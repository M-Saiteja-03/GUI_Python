from tkinter import *
root=Tk()
def info():
    print('This is a GUI made by Marepally Saiteja')
root.geometry("530x450")
# f1=Frame(root,bg='black',relief=SUNKEN,padx=5,pady=5)
# f1.pack(anchor='nw')

b1=Button(root,text="info",bg='aqua',fg='black',font='calibri 12 bold',padx=50,command=info)
b1.pack()

root.mainloop()