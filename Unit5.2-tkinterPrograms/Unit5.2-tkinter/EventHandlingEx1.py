from tkinter import *
root=Tk()
def mouseClick(event):
    print("mouse clicked at", event.x, event.y)
label=Button(text="ClickMeasdfasdfasfdasdfasdfsdf",bg="red")
label.pack()
label.bind("<Button>",mouseClick)
root.mainloop()
