from tkinter import *

root = Tk()

def Click():
    label = Label(root, text="Congrats! U clicked!!!", fg="yellow", bg="green")
    label.pack()

myButton = Button(root, text="Click Me!!", padx=50, pady=20, command=Click, fg="White", bg="Black")

myButton.pack()

root.mainloop()