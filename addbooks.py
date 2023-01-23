from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector




def addbook():

    global txtid,txtname,txtauthor,txtdate,root,full,entry,tree,txtr_id

    root = Tk()
    root.title("BOOK DETAILS")
    root.minsize(width=400,height=400)
    root.geometry("1366x768+0+0")

    full=Frame(root,relief="ridge",bd=20)
    full.place(x=0,y=0,width=1360,height=740)

    Dataframe=Frame(full,bg="#0048BA",relief="ridge",bd=10)
    Dataframe.place(x=80,y=40,width=600,height=300)

    lblid=Label(Dataframe,text="Book id :",bg='#0048BA', fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblid.grid(row=4,column=0,sticky=W)
    txtid=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtid.grid(row=4,column=1)

    lblname=Label(Dataframe,text="Book Name:",bg='#0048BA', fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblname.grid(row=5,column=0,sticky=W)
    txtname=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtname.grid(row=5,column=1)

    lblauthor=Label(Dataframe,text="Author:",bg='#0048BA', fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblauthor.grid(row=6,column=0,sticky=W)
    txtauthor=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtauthor.grid(row=6,column=1)

    lbldate=Label(Dataframe,text="Date:",bg='#0048BA', fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lbldate.grid(row=7,column=0,sticky=W)
    txtdate=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtdate.grid(row=7,column=1)

    entry=Frame(full,bd=10,relief="ridge")
    entry.place(x=80,y=350,width=1220,height=246)

    right=Frame(full,bg="#007FFF",relief="ridge",bd=10)
    right.place(x=700,y=40,width=600,height=300) 

    lb = Label(right,text="Book ID : ", bg='#007FFF', fg='white')
    lb.place(relx=0.05,rely=0.5)

    txtr_id=Entry(right)
    txtr_id.place(relx=0.3,rely=0.5,relwidth=0.62)

    buttons=Frame(full,bd=10,relief="ridge")
    buttons.place(x=80,y=620,width=1220,height=66)

    add=Button(buttons,text="ADD",command=new,bg="#7BB661",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
    add.place(x=0,y=0)

    viewbutton=Button(buttons,text="VIEW",command=view,bg="#A17A74",fg="white",font=("arival",12,"bold"),width=21,padx=6,pady=10)
    viewbutton.place(x=236,y=0)

    updatebutton=Button(buttons,text="UPDATE",command=update_data,bg="#ED872D",fg="white",font=("arival",12,"bold"),width=21,padx=6,pady=10)
    updatebutton.place(x=486,y=0)

    deletebutton=Button(buttons,text=" DELETE",command=deleteBook,bg="#D70040",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
    deletebutton.place(x=736,y=0)
   

    exit=Button(buttons,text="Exit",bg="#ACE1AF",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10,command=root.destroy)
    exit.place(x=976,y=0)

        


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
    root.destroy()

def view():

    conn=mysql.connector.connect(host="localhost",user="root",password="MahendraN",database="library")

    my_cursor=conn.cursor()

    my_cursor.execute("select * from book")

    tree=ttk.Treeview(entry)
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

    

def deleteBook(): 
    
         
    conn=mysql.connector.connect(host="localhost",user="root",password="MahendraN",database="library")

    my_cursor=conn.cursor()
    
    if txtr_id.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        
        delet = "delete from book where Book_id=%s"
        
        Book_id=(txtr_id.get(),)
                    
        my_cursor.execute(delet,Book_id)

        conn.commit()
        
        messagebox.showinfo('Success',"Book Record Deleted Successfully")

        root.destroy()

def update_data():
       
        conn=mysql.connector.connect(host="localhost",username="root",password="MahendraN",database="library")
        my_cursor=conn.cursor()

        if txtid.get()=="" or txtname=="" or txtauthor=="" or txtdate=="" :
            messagebox.showerror("Error","All fields are required")
        else:
            new="update book set Book_name=%s,Author_name=%s,Issue_date=%s where Book_id=%s"
            old=(txtname.get(),txtauthor.get(),txtdate.get(),txtid.get())
            my_cursor.execute(new, old)

            conn.commit()
            
            messagebox.showinfo("Success","Record has been updated")

        root.destroy()


    
      







   



 
        

    
