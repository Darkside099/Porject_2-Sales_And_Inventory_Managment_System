
import mysql.connector
from tabulate import tabulate
import datetime

class Server:

    def __init__(self):
        self.conn = None
        self.cursor = None
    
    def connection(self, uname, password):
        userName = uname.lower()
        password = password.lower()
        try:
            self.conn = mysql.connector.connect(host="localhost",user=userName,passwd=password,auth_plugin="mysql_native_password")
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS MAIN_DATA")
            self.cursor.execute("USE MAIN_DATA")
            self.cursor.execute("COMMIT")
            return True  
        except:
            return False 
        
    def add(self,pname,qty,pcost) :
        date = datetime.datetime.now()
        self.cursor.execute("create table if not exists item(item_id int auto_increment primary key ,item_name varchar(30),item_cost int,item_quantity int ,date_time datetime )")
        self.cursor.execute("alter table item auto_increment= 1001")
        self.cursor.execute("insert into item (item_name,item_cost,item_quantity,date_time) values(%s,%s,%s,%s)",(pname,pcost,qty,date))
        self.cursor.execute("select item_id from item where item_name=%s and item_cost = %s and item_quantity = %s",(pname,pcost,qty))
        self.cursor.execute("commit")
        print("Item Added")
        print(" Your Item's ID is ; ",self.cursor.fetchall())
        return self.cursor.fetchall() # item ID

    def see(self,choice,pid = None):
        if choice == '1' :
            try :
                self.cursor.execute(" select * from item ")
                self.cursor.execute("commit")
                print(tabulate(self.cursor,headers = ["ITEM_ID","ITEM_NAME","ITEM_COST(per kg)","QUANTITY(g)","DATE_TIME"],tablefmt= "pretty"))
                return self.cursor.fetchall()
            except:
                print("! No Data Found !")

        elif choice == "2":
            try :
                self.cursor.execute("select * from item where item_id=%s",(pid,))
                self.cursor.execute("commit")
                print(tabulate(self.cursor,headers = ["ITEM_ID","ITEM_NAME ","ITEM_COST(per kg)","QUANTITY(g)","DATE_TIME"],tablefmt= "pretty"))
                return self.cursor.fetchall()
            except:
                print("! No Data Found at ID ! ;",pid)

    def update(self,pid,choice,update_value):
        try :
            self.cursor.execute("update item set %s = %s where item_id =%s",(choice,update_value,pid))
            print('value updated')
        except :
            print("! No Data Found at ID ! ;",pid)
            
    def delete (self,pid):
        try :
            self.cursor.execute("delete from item where item_id =%s",pid)
            print(" Item Deleted")
        except:
            print("! No Data Found at ID ! ;",pid)
        
    def customer_billing(self,name,phone,it_name,it_qty) :
        self.cursor.execute('create table IF NOT EXISTS customer_detail(customer_name varchar(30),phone varchar(10),item_name varchar(30),item_qty int, price int ,it_id int,date datetime)')
        self.cursor.execute("select item_cost,item_quantity,item_id from item where item_name = %s",(it_name,))
        x= self.cursor.fetchall()
        data = x[0]
        if data[1]>=it_qty :
            price = data[0]*(it_qty//1000)
            it_id = data[2]
            z=data[1]-it_qty
            date = datetime.datetime.now()
            self.cursor.execute("insert into customer_detail(customer_name,phone,item_name,item_qty,price,it_id,date) value(%s,%s,%s,%s,%s,%s,%s)",(name,phone,it_name,it_qty,price,it_id,date))
            self.cursor.execute("update item set item_quantity=%s where item_id = %s",(z,it_id))
            self.cursor.execute("SELECT * FROM customer_detail where phone= %s",(phone,))
            self.cursor.execute("commit")
            print(tabulate(self.cursor,headers = ["CUSTOMER_NAME","PHONE","ITEM_NAME","ITEM_QUANTITY(grams)","ITEM_PRICE","ITEM_ID","DATETIME"],tablefmt = 'github'))
            return self.cursor.fethall()
        else:
            print(" Out of stock ")
            print(" Available stock is...,",data[1])
            return False

    def billing_details(self) :
        try :
            self.cursor.execute("SELECT * FROM customer_detail ")
            print(tabulate(self.cursor,headers = ["CUSTOMER_NAME","PHONE","ITEM_NAME","ITEM_QUANTITY(grams)","ITEM_PRICE","ITEM_ID","DATETIME"],tablefmt = 'pretty'))
            self.cursor.execute("COMMIT")
            return self.cursor.fethall()
        except:
            print("! No Data Found , Please Try Again !")
            return False
    def close(self):
        if self.cursor:
            self.self.cursor.close()
        if self.conn:
            self.conn.close()