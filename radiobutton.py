from tkinter import *
#importing the tkinter module.

def selection():
    #function to display the selected function.
    
    selection = "You selected the option " + str(var.get())
    label.config(text = selection)

root = Tk()     #creating the master.
variable = IntVar()  #temporary variable.

Radiobutton1 = Radiobutton(root, text="Option 1", variable=variable, value=1,   #creating radiobutton 1
                  command=selection)

Radiobutton1.pack( anchor = W )

Radiobutton2 = Radiobutton(root, text="Option 2", variable=variable, value=2,   #creating radiobutton 2 
                  command=selection)

Radiobutton2.pack( anchor = W )

Radiobutton3 = Radiobutton(root, text="Option 3", variable=variable, value=3,   #creating radiobutton 3
                  command=selection)

Radiobutton3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()
