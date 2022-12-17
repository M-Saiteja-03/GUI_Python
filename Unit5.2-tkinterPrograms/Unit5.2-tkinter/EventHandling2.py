from tkinter import *
window = Tk()
#def mouseclicked(event):
 #               print("mouse is clicked at",event.x,event.y)
def mousedoubleclick(event):
                print("mouse is double clicked at",event.x,event.y)
label = Label( window, text="Click me",bg='red' )
label.pack()
#label.bind("<Button>",mouseclicked)
label.bind("<Double-Button-1>",mousedoubleclick)
window.mainloop()
# for output click only on the label