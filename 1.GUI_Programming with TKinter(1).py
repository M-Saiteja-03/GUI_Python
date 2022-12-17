from tkinter import *
from PIL import Image,ImageTk
root=Tk()
#code to make a basic GUI including text
root.title("Saiteja's GUI")
root.geometry("1000x1000")
root.minsize(200,200)
root.maxsize(2000,2000)
matter=Label(text=" Saiteja is making an Awesome GUI ")
matter.pack()
#if text to be displayed along with the image then text label should be written before inserting image

#Code to attach .png images to our GUI
photo=PhotoImage(file="Screenshot (472).png")
HR=Label(image=photo)
HR.pack()

#code to attach jpeg files(install pillow package)
# store=Image.open("zeke (2).jpeg")
# photo=ImageTk.PhotoImage(store)
# Hanuman=Label(image=photo)
# Hanuman.pack()

root.mainloop()
