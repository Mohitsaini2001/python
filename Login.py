from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk

top = Tk()
top.geometry('1800x700')
top.title('Welcome')


def Login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='mohit', db='project')
    cur = db.cursor()
    cur.execute("select * from emp where name=%s and lastname=%s",(E1.get(),E2.get()))
    row = cur.fetchone()


    if row == None:
        messagebox.showerror("Error","Invalid User Name And Password")
    else:
        top.destroy()
        import L2



def Exit():
    top.destroy()

p = StringVar()

path = "A:/bg (2).jpg"
img2 = ImageTk.PhotoImage(Image.open(path))
L2 = Label(top, image=img2)
L2.pack()

B1 = Button(top, text='Exit', fg='black', bg='gray', font='Arial 15 bold', command=Exit)
B1.place(x=550, y=450)

L = Label(top, text='Login', bg='white', fg='black', font='Arial 30 bold')
L.place(x=420, y=50)

L3 = Label(top, text='Name', bg='black', fg='white', font='Arial 20 bold')
L3.place(x=200, y=150)

E1 = Entry(top, font='Arial 20 bold')
E1.place(x=400, y=150)

L4 = Label(top, text='lastname', bg='black', fg='white', font='Arial 20 bold')
L4.place(x=200, y=200)

E2 = Entry(top, font='Arial 20 bold', show="*")
E2.place(x=400, y=200)

B6 = Button(top, text='Login', fg='black', bg='gray', font='Arial 15 bold', command=Login)
B6.place(x=500, y=300)

top.mainloop()
