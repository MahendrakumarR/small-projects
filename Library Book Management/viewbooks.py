from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


def View():
    root=Tk()
    root.title("Book Details")
    root.geometry("1360x740")

    conn=mysql.connector.connect(host="localhost",user="root",password="MahendraN",database="library")

    my_cursor=conn.cursor()

    my_cursor.execute("select * from book")

    

    fullframe=Frame(root,bd=10,relief="ridge")
    fullframe.place(x=0,y=0,width=1360,height=740)

    headingFrame1 = Frame(fullframe,bg="orange",bd=5)
    headingFrame1.place(x=300,y=100,width=640,height=100)

    headingLabel = Label(fullframe, text="Total Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(x=310,y=110,width=620,height=80)

    Dataframe=Frame(fullframe,bd=10,relief="ridge")
    Dataframe.place(x=80,y=250,width=1200,height=246)

   

    

    tree=ttk.Treeview(Dataframe)
    tree["show"]="headings"

    
    # Define number of columns
    tree["columns"]=("Book_id","Book_name","Author_name","Issue_date")

    # Assign the width,minwidth,anchor

    tree.column("Book_id",width=300,anchor=CENTER)
    tree.column("Book_name",width=300,anchor=CENTER)
    tree.column("Author_name",width=300,anchor=CENTER)
    tree.column("Issue_date",width=300,anchor=CENTER)


    # Assign heading names to the respective columns

    tree.heading("Book_id",text="Book Id")
    tree.heading("Book_name",text="Book Name")
    tree.heading("Author_name",text="Author Name")
    tree.heading("Issue_date",text="Issue Date")

    i=0
    for ro in my_cursor:
        tree.insert("",i,text="",values=(ro[0],ro[1],ro[2],ro[3]))
        i=i+1
        

    

    tree.pack()

    root.mainloop()
View()



