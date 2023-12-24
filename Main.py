
from Backend import Server
from tkinter import *

def login():
    root = Tk()
    root.geometry('1000x500')
    root.title('SIMS')
    root.iconbitmap(r'D:\VS_CODE\Git\Porject_2-Sales_And_Inventory_Managment_System\Other_Resources\icon.ico')
    def check():
        username,password=uname_entry.get(),password_entry.get()
        if Server.connection(username,password) == True:
            login_status.config(text='Login Successfuly',fg='blue')
            root.destroy()
        else:
            login_status.config(text='Try Again',fg='red')

    login_label = Label(root, text='WELCOME TO SALES AND INVENTORY MANAGEMENT SYSTEM\nSERVER LOGIN', font=("Cascadia code bold",15))
    login_label.pack()


    uname_lable = Label(root,text='Username :',font=("Cascadia code",10))
    uname_lable.pack()
    uname_entry = Entry(root,width=30)
    uname_entry.pack()
    password_lable = Label(root,text='Password :',font=("Cascadia code",10))
    password_lable.pack()
    password_entry = Entry(root,show='*',width = 30)
    password_entry.pack()

    button = Button(root,text='Login',command=check)
    button.pack()

    login_status = Label(root, text="")
    login_status.pack()

    root.mainloop()

Server.connection('root','2005')