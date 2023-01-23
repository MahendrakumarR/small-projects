from tkinter import*
from tkinter import ttk
from PIL import ImageTk,Image
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
from addbooks import *
from addstudent import *

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("1366x768+0+0")


Dataframe=Frame(root,bd=20,bg="#B2FFFF",relief="ridge")
Dataframe.place(x=0,y=0,width=1363,height=740)

bottomframe=Frame(root,bg="#B2FFFF",bd=20)
bottomframe.place(x=270,y=360,width=900,height=80)

headingFrame1 = Frame(Dataframe,bg="#FFBB00",bd=5)
headingFrame1.place(x=300,y=150,width=640,height=100)

headingLabel = Label(Dataframe, text="Welcome to Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(x=310,y=160,width=620,height=80)

addbutton=Button(bottomframe,text="BOOK DETAILS",command=addbook,bg="blue",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
addbutton.place(x=60,y=5)

studentbutton=Button(bottomframe,text="RETURN DETAILS",command=addstudent,bg="blue",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
studentbutton.place(x=400,y=5)


root.mainloop()