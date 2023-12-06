
import mysql.connector
from tabulate import tabulate
import datetime

def add() :
    cursor=conn.cursor()
    cursor.execute("create table if not exists item(item_id int auto_increment primary key ,item_name varchar(30),item_cost int,item_quantity int ,date_time datetime )")
    cursor.execute("alter table item auto_increment= 1001")

    while True :
        pname = input("| Enter Item's Name : ").title()
        if (pname.replace(' ','')).isalpha() and len(pname) <= 30 : 
            break
        else:
            print("!!! INVALID INPUT !!!")

    while True :
        qty = input ("| Enter Item Quantity in Grams : ")
        if qty.isdigit() and len(qty)<=20 :
            break
        else:
            print("!!! INVALID INPUT !!!")
    qty = int(qty)

    while True:
        pcost = input ("| Enetr item's cost as per kg : ")
        if pcost.isdigit() and len(pcost) <= 20 :
            break
        else:
            print("!!! INVALID INPUT !!!")
    pcost=int(pcost)

    date = datetime.datetime.now()
    print("Item Adding...........")
    cursor.execute("insert into item (item_name,item_cost,item_quantity,date_time) values(%s,%s,%s,%s)",(pname,pcost,qty,date))
    cursor.execute("select item_id from item where item_name=%s and item_cost = %s and item_quantity = %s",(pname,pcost,qty))
    print("Item Added ...,")
    print(" Your Item's ID is ; ",cursor.fetchall())
    cursor.execute("commit")
    input ("press Entre key to continue....,")

def see() :
    cursor= conn.cursor()
    print("+----------------------+\n| 1.) DISPLAY ALL ITEMS|\n| 2.) DISPLAY ONE ITEM |\n+----------------------+")
    ch = input ("Enter : ")

    if ch == "1":
        try :
            cursor.execute(" select * from item ")
            print(tabulate(cursor,headers = ["ITEM_ID","ITEM_NAME","ITEM_COST(per kg)","QUANTITY(g)","DATE_TIME"],tablefmt= "pretty"))
            cursor.execute("commit")
        except:
            print("! No Data Found !")
        
        input ("press Entre key to continue....,")

    elif ch == "2":
        while True :
            pid = input ("Enetr Product_ID : ")
            if pid.isdigit() and len(pid) > 3 :
                break
            else:
                print("!!! INVALID INPUT !!!")
        try :
            cursor.execute("select * from item where item_id=%s",(pid,))
            print(tabulate(cursor,headers = ["ITEM_ID","ITEM_NAME ","ITEM_COST(per kg)","QUANTITY(g)","DATE_TIME"],tablefmt= "pretty"))
            cursor.execute("commit")
        except:
            print("! No Data Found at ID ! ;",pid)
        
        input ("press Entre key to continue....,")
    
    else:
        print("!!! INVALID INPUT !!!")

def update():
    cursor= conn.cursor()
    while True :
        pid = input ("Enetr Item_ID To Update item : ")
        if pid.isdigit() and len(pid) > 3 :
            break
        else:
            print("!!! INVALID INPUT !!!")
    while True :
        print("+---------------+\n|1.)Cost            |\n|2.)Quantity      \n|3.)Exit            |\n+---------------+")
        ch = input ("| Enter your choice ; ")
        if ch == "1":
            while True :
                pcost = input ("Enetr New cost as per kg : ")
                if pcost.isdigit() and len(pcost)<20 and len(pcost)>1:
                    break 
                else:
                    print("!!! INVALID INPUT !!!")
            try :
                print("Item Cost Updating...............")
                cursor.execute("update item set item_cost = %s where item_id =%s",(pcost,pid))
                print("Item cost updated...,")
            except:
                print("! No Data Found at ID ! ;",pid)
            input ("press Entre key to continue....,")
        elif ch == "2" :
            while True :
                qty = input ("| Enter Item Quantity in Grams : ")
                if qty.isdigit() and len(qty)<=20 :
                    break
                else:
                    print("!!! INVALID INPUT !!!")
            try :
                print("Item Cost Updating...............")
                cursor.execute("update item set item_quantity = %s where item_id =%s",(qty,pid))
                print("Item cost updated...,")
            except:
                print("! No Data Found at ID ! ;",pid)
            input ("press Entre key to continue....,")
        elif ch == "3" :
            break
        else:
            print("!!! INVALID INPUT !!!")
        
def delete ():
    cursor= conn.cursor()
    while True :
        pid = input ("Enetr Item_ID To Delete item : ")
        if pid.isdigit() and len(pid) > 3 :
            break
        else:
            print("!!! INVALID INPUT !!!")
    val = (pid,)
    try :
        print(" Item Deleting................")
        sql = "delete from item where item_id =%s"
        cursor.execute(sql,val)
        print(" Item Deleted ...,")
    except:
        print("! No Data Found at ID ! ;",pid)
    
    input ("press Entre key to continue....,")

def customer_billing() :
    cursor=conn.cursor()
    cursor.execute('create table IF NOT EXISTS customer_detail(customer_name varchar(30),phone varchar(10),item_name varchar(30),item_qty int, price int ,it_id int,date datetime)')
    while True :
        name = input("| Enter customer name :").title()
        if (name.replace(' ','')).isalpha() and len(name) <= 30 : 
            break
        else:
            print("----------------Wrong Input Try Agian!!!-------------")
    while True :
        phone=input('| Enter phone number :')
        if phone.isdigit() and len(phone) == 10 :
            break
        else:
            print("----------------Wrong Input Try Agian!!!-------------")
    while True :
        it_name = input ("| Enetr Item_Name : ").title()
        if it_name.isalpha() and len(it_name) <= 30 :
            break
        else:
            print("!!! INVALID INPUT !!!")
    cursor.execute("select item_cost,item_quantity,item_id from item where item_name = %s",(it_name,))
    x= cursor.fetchall()
    data = x[0]
    while True :
        it_qty= input("| Enter Quantity in(grams) To Buy : ")
        if it_qty.isdigit() and len(it_qty)<=20 :
            it_qty =int(it_qty)
            if data[1]>=it_qty :
                break
            else:
                print(" Out of stock ")
                print(" Available stock is...,",data[1])
        else:
            print("!!! INVALID INPUT !!!")
    price = data[0]*(it_qty//1000)
    it_id = data[2]
    date = datetime.datetime.now()
    cursor.execute("insert into customer_detail(customer_name,phone,item_name,item_qty,price,it_id,date) value(%s,%s,%s,%s,%s,%s,%s)",(name,phone,it_name,it_qty,price,it_id,date))
    z=data[1]-it_qty
    cursor.execute("update item set item_quantity=%s where item_id = %s",(z,it_id))
    cursor.execute("commit")
    bill(phone)

def billing_details() :
    cursor=conn.cursor()
    try :
        cursor.execute("SELECT * FROM customer_detail ")
        print(tabulate(cursor,headers = ["CUSTOMER_NAME","PHONE","ITEM_NAME","ITEM_QUANTITY(grams)","ITEM_PRICE","ITEM_ID","DATETIME"],tablefmt = 'pretty'))
        cursor.execute("""COMMIT""")
        cursor.close()
    except:
        print("! No Data Found , Please Try Again !")
        
    input(" Press Enter Key To continue ")

def bill(a) :
    cursor=conn.cursor()
    try :
        cursor.execute("SELECT * FROM customer_detail where phone= %s",(a,))
        print(tabulate(cursor,headers = ["CUSTOMER_NAME","PHONE","ITEM_NAME","ITEM_QUANTITY(grams)","ITEM_PRICE","ITEM_ID","DATETIME"],tablefmt = 'github'))
        cursor.execute("commit")
    except:
        print("! No Data Found , Please Try Again !")
        
    input(" Press Enter Key To continue ")

print("""
|--------------------------------------------------------------------------|
|                            : WELCOME TO :                                |
|                : SALES AND INVENTORY MANAGMENT SYSTEM :                  |
|--------------------------------------------------------------------------|""")
print("| MYSQL Server's Connection")
while True :
    try :
        userName = input("| Enter MYSQL Server's Name : ").lower()
        password = input("| Entre MYSQL Server's password : ").lower()
        global conn
        conn= mysql.connector.connect(host= "localhost",user = userName,passwd = password,auth_plugin = "mysql_negative_password")
        break
    except:
        print("! ERROR ESTABLISHING MYSQL CONNECTION CHECK USERNAME AND PASSWORD !")
        print("--------------------------------------------------------------------")
print("CONGRATULATIONS ! YOUR MYSQL CONNECTION HAS BEEN ESTABLISHED !")
global cursor 
cursor=conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS MAIN_DATA ")
cursor.execute("USE MAIN_DATA")
cursor.execute("COMMIT")
while True :
    print("------------------------------\n| 1.) TO ADD ITEM IN SHOP\n| 2.) TO SEE ITEM IN SHOP\n| 3.) TO UPDATE ITEM COST\n| 4.) TO DELETE ITEM\n| 5.) TO CUSTOMER BILLING \n| 6.) TO SEE BILLING DETALIS\n| 0.) TO EXIT\n------------------------------")
    ch = input("| Enter : ")
    if ch == "1":
        add()
    elif ch == "2" :
        see()
    elif ch == "3":
        update()
    elif ch == "4":
        delete()
    elif ch == "5":
        customer_billing()
    elif ch == "6":
        billing_details()
    elif ch == "0":
        break
    else:
        print("!!! INVALID INPUT !!!")