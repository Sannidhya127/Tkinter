import collections
from tkinter import *
from typing import Collection

root = Tk()

root.title("Calcultor")


entryWidget = Entry(root, width=35, borderwidth=5)
entryWidget.grid(row=0,column=0,columnspan=3, padx=10, pady=10)



def button_click(number):
    # entryWidget.delete(0, END)
    current = entryWidget.get()
    entryWidget.delete(0, END)
    entryWidget.insert(0,str(current) + str(number))
    print(f"{number} entered in field entryWidget")


def button_equal():
    param = entryWidget.get()
    nums = param.split("+")
    sum = int(nums[0]) + int(nums[1])
    entryWidget.delete(0, END)
    entryWidget.insert(0,sum)
    print(f"Calculated sum of {nums[0]} and {nums[1]} to be {sum}")

def button_clear():
    entryWidget.delete(0, END)
    print("Ran command Clear Screen")

def deleteOneChar():
    data = entryWidget.get()
    lastChar = data[-1]
    entryWidget.delete(lastChar,END)
    print("Deleted last character. Refresh required")

# Defining the buttons

button_1 = Button(root, text=1, padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text=2, padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text=3, padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text=4, padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text=5, padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text=6, padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text=7, padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text=8, padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text=9, padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text=0, padx=40, pady=20, command=lambda: button_click(0))
Button_add = Button(root, text="+", padx=39, pady=20,command=lambda: button_click("+"))
Button_equal = Button(root, text="=", padx=91, pady=20,command=lambda: button_equal())
Button_cls = Button(root, text="cls", padx=79, pady=20,command=lambda: button_clear())
# Button_ClearOneAtATime= Button(root, text="←", padx=20, pady=20, command=deleteOneChar)

# Adding buttons to screen and aligning them

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)


button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)


button_0.grid(row=4,column=0)
Button_add.grid(row=5, column=0)
Button_equal.grid(row=5,column=1, columnspan=2)
Button_cls.grid(row=4, column=1,columnspan=2)
# Button_ClearOneAtATime.grid(row=4, column=2)



root.mainloop()