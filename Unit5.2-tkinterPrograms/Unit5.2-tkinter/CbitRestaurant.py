from tkinter import *
root=Tk()
root.title("CBIT Restaurant")
def order():
    filewin=Toplevel(root)
    button=Button(filewin,text="your order will be delivered in 10 minuntes")
    button.pack()
#create menu bar
menubar=Menu(root)
#create veg menu items
veg=Menu(menubar,tearoff=1)
veg.add_command(label="Cashew Biryani",activebackground='blue',activeforeground='red',command=order)
veg.add_command(label="Paneer Biryani",activebackground='green',activeforeground='red')
veg.add_command(label="Mashroom Biryani",activebackground='green',activeforeground='red')
menubar.add_cascade(label="VegItems",menu=veg)
# create NonVeg item
nonveg=Menu(menubar,tearoff=0)
nonveg.add_command(label="Chicken Biryani",activebackground='green',activeforeground='red')
nonveg.add_command(label="mutton biryani",activebackground='green',activeforeground='red')
menubar.add_cascade(label="Nonveg Biryanis",menu=nonveg)
root.config(menu=menubar)
root.mainloop()