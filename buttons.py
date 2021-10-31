from tkinter import *

root = Tk()

def Click():
    label = Label(root, text="Congrats! U clicked!!!", fg="yellow", bg="green")
    label.pack()

myButton = Button(root, text="Click Me!!", pady=10, command=Click, fg="White", bg="Black",activebackground="cyan", relief=GROOVE)

myButton.pack(side=LEFT)

root.mainloop()