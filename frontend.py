import tkinter as tk
from tkinter import messagebox
from Backend import Server

global win

win = tk.Tk()
win.geometry('1000x500')
win.title('SIMS')
# win.iconbitmap(r'/home/darkstar099/Desktop/Darkside/VS Code/Git/Porject_2-Sales_And_Inventory_Managment_System/Other_Resources/icon.ico')

class Application:
    def exit_program():
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            win.destroy()
    btn_add = tk.Button(win, text="Add Item")#command=show_add)
    btn_add.pack()

    btn_see = tk.Button(win, text="See Items")#command=show_see)
    btn_see.pack()

    btn_update = tk.Button(win, text="Update Item") #command=show_update)
    btn_update.pack()

    btn_delete = tk.Button(win, text="Delete Item")#command=show_delete)
    btn_delete.pack()

    btn_customer_billing = tk.Button(win, text="Customer Billing")#command=show_customer_billing)
    btn_customer_billing.pack()

    btn_billing_details = tk.Button(win, text="Billing Details")#command=show_billing_details)
    btn_billing_details.pack()

    btn_exit = tk.Button(win, text="Exit")#command=exit_program)
    btn_exit.pack()

win.mainloop()