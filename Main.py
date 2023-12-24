
from frontend import Application
from Backend import Server
from tkinter import *

root = Tk()
root.geometry('1000x500')
root.title('SIMS')
root.iconbitmap(r'D:\VS_CODE\Git\Porject_2-Sales_And_Inventory_Managment_System\Other_Resources\icon.ico')

def login():
    x,y=uname_entry.get(),password_entry.get()

uname_lable = Label(root,text='Username :')
uname_lable.pack()
uname_entry = Entry(root,width=30)
uname_entry.pack()
password_lable = Label(root,text='Password :')
password_lable.pack()
password_entry = Entry(root,show='*',width = 30)
password_entry.pack()

button = Button(root,text='Login',command=login)
