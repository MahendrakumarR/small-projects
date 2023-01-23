from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1366x768+0+0")

        #----------------------- Variables-------------------------------------------------#
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.IssueDate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()

        #---------------------------Heading-----------------------------------------------------#

        lbtitle=Label(self.root,bd=20,relief="ridge",text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbtitle.pack(side=TOP,fill=X)
       
        # --------------------------Data frame--------------------------------------------------#

        Dataframe=Frame(self.root,bd=20,relief="ridge")
        Dataframe.place(x=0,y=130,width=1366,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief="ridge",font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=880,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief="ridge",font=("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=880,y=5,width=440,height=350)

        #--------------------------Button frame--------------------------------------------------#
        
        Buttonframe=Frame(self.root,bd=10,relief="ridge")
        Buttonframe.place(x=0,y=530,width=1366,height=70)

        #--------------------------Details frame--------------------------------------------------#
        
        Detailsframe=Frame(self.root,bd=10,relief="ridge")
        Detailsframe.place(x=0,y=600,width=1366,height=140)

        #--------------------------Dataframeleft--------------------------------------------------#

        lblNameTablet=Label(DataframeLeft,text="Name of Tablet:",font=("arival",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataframeLeft,state="readonly",textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=35)
        comNametablet["values"]=("Acetaminophen","Adderall","Amitriptyline","Amlodipine","Amoxicillin","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,text="Reference No:",font=("arival",12,"bold"),padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("arival",12,"bold"),textvariable=self.ref,width=33)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,text="Dose:",font=("arival",12,"bold"),padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,textvariable=self.Dose,font=("arival",12,"bold"),width=33)
        txtDose.grid(row=2,column=1)

        lblNooftablets=Label(DataframeLeft,text="No of Tablets:",font=("arival",12,"bold"),padx=2,pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,textvariable=self.NumberofTablets,font=("arival",12,"bold"),width=33)
        txtDose.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,text="Lot:",font=("arival",12,"bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,textvariable=self.Lot,font=("arival",12,"bold"),width=33)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,text="Issue Date:",font=("arival",12,"bold"),padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,textvariable=self.IssueDate,font=("arival",12,"bold"),width=33)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,text="Expiry Date:",font=("arival",12,"bold"),padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,textvariable=self.ExpDate,font=("arival",12,"bold"),width=33)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,text="Daily Dose:",font=("arival",12,"bold"),padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,textvariable=self.DailyDose,font=("arival",12,"bold"),width=33)
        txtDailyDose.grid(row=7,column=1)

        lblsideEffect=Label(DataframeLeft,text="Side Effect:",font=("arival",12,"bold"),padx=2,pady=6)
        lblsideEffect.grid(row=8,column=0,sticky=W)
        txtsideEffect=Entry(DataframeLeft,textvariable=self.SideEffect,font=("arival",12,"bold"),width=33)
        txtsideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,text="Further Infomation:",font=("arival",12,"bold"),padx=2,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,textvariable=self.FurtherInformation,font=("arival",12,"bold"),width=25)
        txtFurtherinfo.grid(row=0,column=3)

        lblDrivingMachine=Label(DataframeLeft,text="Blood Pressure:",font=("arival",12,"bold"),padx=2,pady=6)
        lblDrivingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine=Entry(DataframeLeft,textvariable=self.DrivingUsingMachine,font=("arival",12,"bold"),width=25)
        txtDrivingMachine.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,text="Storage Advice:",font=("arival",12,"bold"),padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,textvariable=self.StorageAdvice,font=("arival",12,"bold"),width=25)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,text="Medication:",font=("arival",12,"bold"),padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,textvariable=self.HowToUseMedication,font=("arival",12,"bold"),width=25)
        txtMedicine.grid(row=3,column=3)

        lblPatientid=Label(DataframeLeft,text="Patient Id:",font=("arival",12,"bold"),padx=2,pady=6)
        lblPatientid.grid(row=4,column=2,sticky=W)
        txtPatientid=Entry(DataframeLeft,textvariable=self.PatientId,font=("arival",12,"bold"),width=25)
        txtPatientid.grid(row=4,column=3)

        lblNhsnumber=Label(DataframeLeft,text="NHS Number:",font=("arival",12,"bold"),padx=2,pady=6)
        lblNhsnumber.grid(row=5,column=2,sticky=W)
        txtNhsnumber=Entry(DataframeLeft,textvariable=self.nhsNumber,font=("arival",12,"bold"),width=25)
        txtNhsnumber.grid(row=5,column=3)

        lblPatientname=Label(DataframeLeft,text="Patient Name:",font=("arival",12,"bold"),padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataframeLeft,textvariable=self.PatientName,font=("arival",12,"bold"),width=25)
        txtPatientname.grid(row=6,column=3)

        lblDateofBirth=Label(DataframeLeft,text="Date of Birth:",font=("arival",12,"bold"),padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(DataframeLeft,textvariable=self.DateOfBirth,font=("arival",12,"bold"),width=25)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,text="Patient Address:",font=("arival",12,"bold"),padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,textvariable=self.PatientAddress,font=("arival",12,"bold"),width=25)
        txtPatientAddress.grid(row=8,column=3)

        #----------------------------Dataframeright--------------------------------------------#
        
        self.txtPrescription=Text(DataframeRight,font=("arival",12,"bold"),width=46,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #----------------------------Buttons----------------------------------------------------#
        
        btnPrescription=Button(Buttonframe,command=self.Prescription,text="Prescription",bg="orange",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.PrescriptionData,text="Prescription Data",bg="blue",fg="white",font=("arival",12,"bold"),width=21,padx=2,pady=10)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,command=self.update_data,text="Update",bg="skyblue",fg="white",font=("arival",12,"bold"),width=21,padx=2,pady=10)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.delete,text="Delete",bg="red",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.Clear,text="Clear",bg="yellow",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,command=self.Exit,text="Exit",bg="green",fg="white",font=("arival",12,"bold"),width=21,padx=4,pady=10)
        btnExit.grid(row=0,column=5)
        
        #-------------------------------------Table----------------------------------------------#
        #-----------------------------------Scrollbar--------------------------------------------#

        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablet","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet",text="Name of Tablet")
        self.hospital_table.heading("ref",text="Reference No")
        self.hospital_table.heading("dose",text="Dose:")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Expiry Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"


        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()
        

        #------------------------------Functionality Declaration--------------------------#
    def PrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="MahendraN",database="mydata")
            my_cursor=conn.cursor()
            # my_cursor.execute("create database mydata")
            # my_cursor.execute("create table details (nameoftablet VARCHAR(45),ref int,dose VARCHAR(45),nooftablets VARCHAR(45),lot VARCHAR(45),issuedate VARCHAR(45),expdate VARCHAR(45),dailydose VARCHAR(45),storage VARCHAR(45),nhsnumber VARCHAR(45),pname VARCHAR(45),dob VARCHAR(45),address VARCHAR(45))")
            sql="insert into details (nameoftablet,ref,dose,nooftablets,lot,issuedate,expdate,dailydose,storage,nhsnumber,pname,dob,address) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val=(self.Nameoftablets.get(),self.ref.get(),self.Dose.get(),self.NumberofTablets.get(),self.Lot.get(),self.IssueDate.get(),self.ExpDate.get(),self.DailyDose.get(),self.StorageAdvice.get(),self.nhsNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),self.PatientAddress.get())
            my_cursor.execute(sql,val)
            conn.commit()
            
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success","Record has been inserted")

    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MahendraN",database="mydata")
        my_cursor=conn.cursor()
        new="update details set nameoftablet=%s,dose=%s,nooftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,pname=%s,dob=%s,address=%s where ref=%s"
        old=(self.Nameoftablets.get(),self.Dose.get(),self.NumberofTablets.get(),self.Lot.get(),self.IssueDate.get(),self.ExpDate.get(),self.DailyDose.get(),self.StorageAdvice.get(),self.nhsNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),self.PatientAddress.get(),self.ref.get())
        my_cursor.execute(new, old)

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Record has been updated")


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MahendraN",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.IssueDate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def Prescription(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+ self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference no:\t\t\t"+ self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+ self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+ self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+ self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"IssueDate:\t\t\t"+ self.IssueDate.get()+"\n")
        self.txtPrescription.insert(END,"ExpDate:\t\t\t"+ self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"DailyDose:\t\t\t"+ self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"SideEffect:\t\t\t"+ self.SideEffect.get()+"\n")
        self.txtPrescription.insert(END,"FurtherInformation:\t\t\t"+ self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"StorageAdvice:\t\t\t"+ self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+ self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t"+ self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t"+ self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"PatientName:\t\t\t"+ self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+ self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+ self.PatientAddress.get()+"\n")

    def delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="MahendraN",database="mydata")
        my_cursor=conn.cursor()
        query="delete from details where ref=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient Details has been deleted successfully")

    def Clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def Exit(self):
        Exit=messagebox.askyesno("Hospital management","Confirm you want to exit")
        if Exit>0:
            root.destroy()
            return

        





root=Tk()
ob=Hospital(root)
root.mainloop()



