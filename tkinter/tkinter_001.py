from tkinter import *

parent = Tk()
username = Label(parent, text="Username").grid(row=0, column=0)
e1 = Entry(parent).grid(row=0, column=1)
password = Label(parent, text="Password").grid(row=1, column=0)
e1 = Entry(parent).grid(row=1, column=1)
sumit = Button(parent,  text="Submit").grid(row=4, column=1)

# Hiển thị cửa sổ
parent.mainloop()