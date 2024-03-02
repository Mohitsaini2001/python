from tkinter import *
from tkinter import ttk

from PIL import ImageTk, Image
from tkinter import CHECKBUTTON


top = Tk()
top.geometry('1800x700')
top.title('Welcome')


p = StringVar()

path = "A:/bg (2).jpg"
img2 = ImageTk.PhotoImage(Image.open(path))

L2 = Label(top, image=img2)
L2.pack()


j=['Select', 'Java', 'HTML', 'CSS', 'Bootstrap', 'Recat JS', 'JQUERY']



L = Label(top, text="Hello guys this is python ERA", bg="green", fg="white", font=('Arial 20 bold'))
L.place(x=500, y=50)

cb=ttk.Combobox(top, value=j, font=('Arial 15 bold'))
cb.place(x=200, y=300)
cb.current(0)

C=Checkbutton(top, text='Java')
C.place(x=300, y=400)

C2=Checkbutton(top,text='Python')
C2.place(x=450, y=400)

C3=Checkbutton(top,text='HTML')
C3.place(x=600, y=400)




top.config()
top.mainloop()
