from tkinter import *
window = Tk()
def mousedoubleclick(event):
                print("mouse is double clicked at",event.x,event.y)
def moved(event):
                print("mouse moved at ",event.x,event.y)
label = Label( window, text="Click me",bg='red' )
label.pack()
label.bind("<Double-Button-1>",mousedoubleclick)
label.bind("<Motion>",moved)
window.mainloop()
# for output click only on the label
