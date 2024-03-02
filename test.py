from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from PIL import ImageTk, Image

top = Tk()
top.geometry('1800x700')
top.title('Welcome')


def insert():
    k = E1.get()
    k2 = E2.get()
    k3 = int(E3.get())
    k4 = int(E4.get())
    k5 = p.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='mohit', db='project')
    cur = db.cursor()
    s = "insert into emp values('%s','%s','%s','%s','%s')" % (k, k2, k3, k4, k5)
    result = cur.execute(s)

    if result > 0:
        messagebox.showinfo("Result", "Record inserted successfully")
    else:
        messagebox.showinfo("Result", "Record not filled")
    db.commit()
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    E3.delete(0, 'end')
    E4.delete(0, 'end')


def show():
    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='mohit', db='project')
    cur = db.cursor()
    s = "select * from emp"
    cur.execute(s)
    result = cur.fetchall()
    for col in result:
        name = col[0]
        last = col[1]
        sal = col[2]
        age = col[3]
        gen = col[4]
        tv.insert("", 'end', values=(name, last, sal, age, gen))







def search():
    k = E5.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='mohit', db='project')
    cur = db.cursor()
    p = "select * from emp where name=%s"
    cur.execute(p, k)
    result = cur.fetchall()
    for col in result:
        name = col[0]
        lastname = col[1]
        salary = col[2]
        age = col[3]
        gen = col[4]
        tv.insert("", 'end', values=(name, lastname, salary, age, gen))





def Delete():
    k = E5.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='mohit', db='project')
    cur = db.cursor()
    p = "delete from emp where name=%s"
    result = cur.execute(p, k)
    if (result>0):
        messagebox.showinfo("Result", 'Record deleted')
    else:
        messagebox.showinfo("Result", 'Record not deleted')
    db.commit()



def Login():
    top.destroy()
    import Login


def Exit():
    top.destroy()


p = StringVar()

path = "A:/bg.jpg"
img2 = ImageTk.PhotoImage(Image.open(path))

L2 = Label(top, image=img2)
L2.pack()

tv = ttk.Treeview(top)
tv['columns'] = ('Name', 'Lastname', 'Salary', 'Age', 'Gender')
tv.column('#0', width=0, stretch=NO)
tv.column('Name', anchor=CENTER, width=110)
tv.column('Lastname', anchor=CENTER, width=110)
tv.column('Salary', anchor=CENTER, width=110)
tv.column('Age', anchor=CENTER, width=110)
tv.column('Gender', anchor=CENTER, width=110)

tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Lastname', text='Lastname', anchor=CENTER)
tv.heading('Salary', text='Salary', anchor=CENTER)
tv.heading('Age', text='Age', anchor=CENTER)
tv.heading('Gender', text='Gender', anchor=CENTER)
tv.place(x=800, y=150)

L = Label(top, text='Registration', bg='grey', fg='black', font='Arial 30 bold')
L.place(x=420, y=50)

L3 = Label(top, text='Name', bg='black', fg='white', font='Arial 20 bold')
L3.place(x=200, y=150)

E1 = Entry(top, font='Arial 20 bold')
E1.place(x=400, y=150)

L4 = Label(top, text='Lastname', bg='black', fg='white', font='Arial 20 bold')
L4.place(x=200, y=200)

E2 = Entry(top, font='Arial 20 bold')
E2.place(x=400, y=200)

L5 = Label(top, text='Salary', bg='black', fg='white', font='Arial 20 bold')
L5.place(x=200, y=250)

E3 = Entry(top, font='Arial 20 bold')
E3.place(x=400, y=250)

L6 = Label(top, text='Age', bg='black', fg='white', font='Arial 20 bold')
L6.place(x=200, y=300)

E4 = Entry(top, font='Arial 20 bold')
E4.place(x=400, y=300)

L7 = Label(top, text='Gender', bg='black', fg='white', font='Arial 20 bold')
L7.place(x=200, y=350)

r1 = Radiobutton(top, text='Male', variable=p, value='Male', font='Arial 15 bold')
r1.place(x=400, y=350)

r1 = Radiobutton(top, text='Female', variable=p, value='Female', font='Arial 15 bold')
r1.place(x=500, y=350)

B1 = Button(top, text='Exit', fg='black', bg='gray', font='Arial 15 bold', command=Exit)
B1.place(x=550, y=450)

B2 = Button(top, text='Submit', fg='black', bg='gray', font='Arial 15 bold', command=insert)
B2.place(x=400, y=450)

B3 = Button(top, text='Show', fg='black', bg='gray', font='Arial 15 bold', command=show)
B3.place(x=650, y=450)

B4 = Button(top, text='Search', fg='black', bg='gray', font='Arial 15 bold', command=search)
B4.place(x=700, y=50)

E5 = Entry(top, font='Arial 20 bold')
E5.place(x=800, y=50)

B5 = Button(top, text='Delete', fg='black', bg='gray', font='Arial 15 bold', command=Delete)
B5.place(x=900, y=500)

B6 = Button(top, text='Login', fg='black', bg='gray', font='Arial 15 bold', command=Login)
B6.place(x=1050, y=500)

top.config()
top.mainloop()
