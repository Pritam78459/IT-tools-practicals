from tkinter import *
#importing tkinter module.

root = Tk()     #creating the master.
frame = Frame(root) #creating the frame.
frame.pack()

bottomframe = Frame(root)               #creating the bottom frame.
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")     #creating the red button.
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")#creating the green button.
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")#creating the blue button.
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")#creating the black button.
blackbutton.pack( side = BOTTOM)

root.mainloop()
