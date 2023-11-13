from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator

# Tạo tk window
root=Tk()
root.title("Google Translate")
root.geometry("500x630")
root.iconbitmap("D:\PTIT\PTIT - Source\CodePTIT-PYTHON\python_google_translate\image\logo.ico")
load=Image.open("D:\PTIT\PTIT - Source\CodePTIT-PYTHON\python_google_translate\image\\bg.png")
reder=ImageTk.PhotoImage(load)
img=Label(root,image=reder)
img.place(x=0,y=0)

root.mainloop()