from tkinter import *

root = Tk()


entryWidget = Entry(root, width=50, bg="yellow", fg="red", borderwidth=5)

entryWidget.insert(0, "Enter name here")

entryWidget.pack()


def Click():
    label = Label(root, text=f"Hello {entryWidget.get()}!", fg="yellow", bg="green")
    label.pack()
    print("Clicked button")

myButton = Button(root, text="Click Me!!", padx=50, pady=20, command=Click, fg="White", bg="Black")

myButton.pack() 

root.mainloop()