from tkinter import *

root = Tk()

label1 = Label(root, text="This is label 1").grid(row=0, column=0)
label2 = Label(root, text="This is Label 2").grid(row=1, column=1)
label3 = Label(root, text="This is Label 3").grid(row=2, column=2)

# Can also use label.grid(row=0, column=0)

root.mainloop()

