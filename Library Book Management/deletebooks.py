from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
 
 #----------------------------------------View books--------------------------#

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

    bottom=Frame(fullframe,bd=10,relief="ridge")
    bottom.place(x=400,y=550,width=477,height=68)

    deletebutton=Button(bottom,text=" DELETE",bg="blue",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
    deletebutton.grid(row=0,column=3)

    

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

  #-------------------------------------------Add book--------------------------------#

  from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector




def addbook():

    global txtid,txtname,txtauthor,txtdate,root

    root = Tk()
    root.title("ADD BOOK")
    root.minsize(width=400,height=400)
    root.geometry("1366x768+0+0")

    full=Frame(root,relief="ridge",bd=20)
    full.place(x=0,y=0,width=1360,height=740)

    Dataframe=Frame(full,bg="black",relief="ridge",bd=10)
    Dataframe.place(x=300,y=100,width=600,height=300)

    lblid=Label(Dataframe,text="Book id :",bg='black', fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblid.grid(row=4,column=0,sticky=W)
    txtid=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtid.grid(row=4,column=1)

    lblname=Label(Dataframe,text="Book Name:",bg='black', fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblname.grid(row=5,column=0,sticky=W)
    txtname=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtname.grid(row=5,column=1)

    lblauthor=Label(Dataframe,text="Author:",bg='black', fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblauthor.grid(row=6,column=0,sticky=W)
    txtauthor=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtauthor.grid(row=6,column=1)

    lbldate=Label(Dataframe,text="Date:",bg='black', fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lbldate.grid(row=7,column=0,sticky=W)
    txtdate=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtdate.grid(row=7,column=1)

    buttons=Frame(full,bd=10)
    buttons.place(x=0,y=450,width=1360,height=200)

    add=Button(buttons,text="ADD",command=new,bg="blue",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
    add.place(x=350,y=100)

    updatebutton=Button(buttons,text="UPDATE",bg="blue",fg="white",font=("arival",12,"bold"),width=21,padx=6,pady=10)
    updatebutton.place(x=360,y=100)

    exit=Button(buttons,text="Exit",bg="blue",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10,command=root.destroy)
    exit.place(x=650,y=100)

    root.mainloop()


def new():
        
    if txtid.get()=="" or txtname.get()=="" or txtauthor.get()=="" or txtdate.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        conn=mysql.connector.connect(host="localhost",username="root",password="MahendraN",database="library")
        my_cursor=conn.cursor()
        # my_cursor.execute("create database mydata")
        # my_cursor.execute("create table book (Book_id int,Book_name VARCHAR(45),Author_name VARCHAR(45),Issue_date date)
        sql="insert into book (Book_id,Book_name,Author_name,Issue_date) values (%s,%s,%s,%s)"
        val=(txtid.get(),txtname.get(),txtauthor.get(),txtdate.get())
        my_cursor.execute(sql,val)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record has been inserted")

    



   



 
        

    



