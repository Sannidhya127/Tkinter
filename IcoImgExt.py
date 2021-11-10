from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Icons, Images and Exit buttons with Python Tkinter")

root.iconbitmap("icon.ico")


Button_exit = Button(root, text="Exit", command=root.quit) # I don't know why we need to do this when we can simply write command = exit() instead. LOL


Button_exit.pack()


myImage = ImageTk.PhotoImage(Image.open("py.png"))

my_label = Label(image=myImage)
my_label.pack()

root.mainloop()