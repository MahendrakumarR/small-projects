from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector




def addstudent():

    global txtid,txtname,txtbook,txtclass,txtr_date,txtp_date,root,full,entry,tree,txtr_id

    root = Tk()
    root.title("RETURN DETAILS")
    root.minsize(width=400,height=400)
    root.geometry("1366x768+0+0")

    full=Frame(root,relief="ridge",bd=20)
    full.place(x=0,y=0,width=1360,height=740)

    Dataframe=Frame(full,bg="#FF9966",relief="ridge",bd=10)
    Dataframe.place(x=80,y=40,width=600,height=400)

    lblid=Label(Dataframe,text="Student Id :",bg="#FF9966", fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblid.grid(row=4,column=0,sticky=W)
    txtid=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtid.grid(row=4,column=1)

    lblname=Label(Dataframe,text="Student Name:",bg="#FF9966", fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblname.grid(row=5,column=0,sticky=W)
    txtname=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtname.grid(row=5,column=1)

    lblclass=Label(Dataframe,text="Student Class:",bg="#FF9966", fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblclass.grid(row=6,column=0,sticky=W)
    txtclass=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtclass.grid(row=6,column=1)

    lblbook=Label(Dataframe,text="Book Name:",bg="#FF9966", fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblbook.grid(row=7,column=0,sticky=W)
    txtbook=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtbook.grid(row=7,column=1)

    lblp_date=Label(Dataframe,text="Purchase Date:",bg="#FF9966", fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblp_date.grid(row=8,column=0,sticky=W)
    txtp_date=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtp_date.grid(row=8,column=1)

    lblr_date=Label(Dataframe,text="Return Date:",bg="#FF9966", fg='white',font=("arival",12,"bold"),padx=10,pady=20)
    lblr_date.grid(row=9,column=0,sticky=W)
    txtr_date=Entry(Dataframe,font=("arival",12,"bold"),width=33)
    txtr_date.grid(row=9,column=1)

    entry=Frame(full,bd=10,bg='#E9D66B',relief="ridge")
    entry.place(x=80,y=446,width=1220,height=170)

    right=Frame(full,bg="#98817B",relief="ridge",bd=10)
    right.place(x=700,y=40,width=600,height=400) 

    lb = Label(right,text="Student Id : ", bg='#98817B', fg='white')
    lb.place(relx=0.05,rely=0.5)

    txtr_id=Entry(right)
    txtr_id.place(relx=0.3,rely=0.5,relwidth=0.62)

    buttons=Frame(full,bd=10,relief="ridge")
    buttons.place(x=80,y=620,width=1220,height=66)

    add=Button(buttons,text="ADD",command=new,bg="#3B7A57",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
    add.place(x=0,y=0)

    viewbutton=Button(buttons,text="VIEW",command=view,bg="#7CB9E8",fg="white",font=("arival",12,"bold"),width=21,padx=6,pady=10)
    viewbutton.place(x=236,y=0)

    updatebutton=Button(buttons,text="UPDATE",command=update_data,bg="#C46210",fg="white",font=("arival",12,"bold"),width=21,padx=6,pady=10)
    updatebutton.place(x=486,y=0)

    deletebutton=Button(buttons,text=" DELETE",command=deleteBook,bg="#DB2D43",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
    deletebutton.place(x=736,y=0)
   

    exit=Button(buttons,text="Exit",bg="#660000",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10,command=root.destroy)
    exit.place(x=976,y=0)

        


def new():
        
    if txtid.get()=="" or txtname.get()=="" or txtbook.get()=="" or txtr_date.get()=="" or txtp_date.get()=="" or txtclass.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        conn=mysql.connector.connect(host="localhost",username="root",password="MahendraN",database="library")
        my_cursor=conn.cursor()
        # my_cursor.execute("create database mydata")
        # my_cursor.execute("create table book (Book_id int,Book_name VARCHAR(45),Author_name VARCHAR(45),Issue_date date)
        sql="insert into student (Student_Id,Student_Name,Book_Name,Student_Class,Book_Purchase_Date,Book_Return_Date) values (%s,%s,%s,%s,%s,%s)"
        val=(txtid.get(),txtname.get(),txtbook.get(),txtclass.get(),txtp_date.get(),txtr_date.get())
        my_cursor.execute(sql,val)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record has been inserted")
    root.destroy()

def view():

    conn=mysql.connector.connect(host="localhost",user="root",password="MahendraN",database="library")

    my_cursor=conn.cursor()

    my_cursor.execute("select * from student")

    tree=ttk.Treeview(entry)
    tree["show"]="headings"

    
    # Define number of columns
    tree["columns"]=("Student_Id","Student_Name","Book_Name","Student_Class","Book_Purchase_Date","Book_Return_Date")

    # Assign the width,minwidth,anchor

    tree.column("Student_Id",width=200,anchor=CENTER)
    tree.column("Student_Name",width=200,anchor=CENTER)
    tree.column("Book_Name",width=200,anchor=CENTER)
    tree.column("Student_Class",width=200,anchor=CENTER)
    tree.column("Book_Purchase_Date",width=200,anchor=CENTER)
    tree.column("Book_Return_Date",width=200,anchor=CENTER)


    # Assign heading names to the respective columns

    tree.heading("Student_Id",text="Student Id")
    tree.heading("Student_Name",text="Student Name")
    tree.heading("Book_Name",text="Book Name")
    tree.heading("Student_Class",text="Student Class")
    tree.heading("Book_Purchase_Date",text="Book Purchase Date")
    tree.heading("Book_Return_Date",text="Book Return Date")
    

        
    i=0
    for ro in my_cursor:
        tree.insert("",i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
        i=i+1

    tree.pack()

    root.mainloop()

    

def deleteBook(): 
    
         
    conn=mysql.connector.connect(host="localhost",user="root",password="MahendraN",database="library")

    my_cursor=conn.cursor()
    
    if txtr_id.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        
        delet = "delete from student where Student_Id=%s"
        
        student_id=(txtr_id.get(),)
                    
        my_cursor.execute(delet,student_id)

        conn.commit()
        
        messagebox.showinfo('Success',"Book Record Deleted Successfully")

        root.destroy()

def update_data():
       
        conn=mysql.connector.connect(host="localhost",username="root",password="MahendraN",database="library")
        my_cursor=conn.cursor()

        if txtid.get()=="" or txtname.get()=="" or txtbook.get()=="" or txtr_date.get()=="" or txtp_date.get()=="" or txtclass.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            new="update student set Student_Name=%s,Book_Name=%s,Student_Class=%s,Book_Purchase_Date=%s,Book_Return_Date=%s where Student_Id=%s"
            old=(txtname.get(),txtbook.get(),txtclass.get(),txtp_date.get(),txtr_date.get(),txtid.get())
            my_cursor.execute(new, old)

            conn.commit()
            
            messagebox.showinfo("Success","Record has been updated")

        root.destroy()


    
      







   



 
        

    
