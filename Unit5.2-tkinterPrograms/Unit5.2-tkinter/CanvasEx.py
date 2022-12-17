from tkinter import *
root=Tk()
c=Canvas(root,width=500,height=500,bg='grey')
root.title("welcome to CBIT")
c.pack()
# draw a line
c.create_line(0, 0, 2000, 2000, fill="red",width=5,activefill="black")
#rectangle
c.create_rectangle(50, 20, 150, 80, fill="green")
# draw the text
c.create_text(80,50,text="CSE1-OOPS")
c.create_text(100,100,text="CBIT")
#draw a circle or eclipse
c.create_oval(300,300,400,400,fill="white")
# draw a arc of 300degrees
c.create_arc(140, 210, 170,170, start = 0,
                          extent = 180, outline = "green",
                          fill = "red", width = 2)
# draw a polygon
points = [150, 100, 200, 120, 240, 180,
                  210, 200, 150, 150, 100, 200]
c.create_polygon(points,outline = "blue",fill = "orange", width = 2)

root.mainloop()
