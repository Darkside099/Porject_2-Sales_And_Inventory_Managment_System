from tkinter import *

win = Tk()
win.geometry('1000x500')
win.title('SIMS')
win.iconbitmap(r'D:\VS_CODE\Git\Porject_2-Sales_And_Inventory_Managment_System\icon.ico')
login_lable =Label(win,text ='Login Mysql Database',font='bold')
login_lable.pack()
use_name = Entry(win,width=20)
use_name.pack(pady=30)
win.mainloop()