from tkinter import*
from tkinter import ttk
import tkinter.messagebox  # Correct import for ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("1270x680+0+0")


        # =================================================Variable=========================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()
        


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=17,relief=RIDGE,font=("times new roman",35,"bold"),padx=2,pady=10)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=8,relief=RIDGE,padx=15,bg="powder blue")
        frame.place(x=0,y=110,width=1270,height=365)

        # =======================================DataFrameLaft====================================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="green",bd=4,relief=RIDGE,font=("times new roman",15,"bold"))
        DataFrameLeft.place(x=0,y=5,width=670,height=335)
        
        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",font=("arial",12,"bold"),padx=3,pady=5)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("arial",12,"bold"),width=18,state="readonly",textvariable=self.member_var)
        comMember["value"]=("Admin staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN NO",font=("arial",12,"bold"),padx=3,pady=5)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("times new roman",15,"bold"),width=18,textvariable=self.prn_var)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID No:",font=("arial",12,"bold"),padx=3,pady=5)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.id_var)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",font=("arial",12,"bold"),padx=3,pady=5)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.firstname_var)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name",font=("arial",12,"bold"),padx=3,pady=5)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.lastname_var)
        txtLastName.grid(row=4,column=1)

        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address 1",font=("arial",12,"bold"),padx=3,pady=5)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.address1_var)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address 2",font=("arial",12,"bold"),padx=3,pady=5)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.address2_var)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code",font=("arial",12,"bold"),padx=3,pady=5)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.postcode_var)
        txtPostCode.grid(row=7,column=1)

        lblMobile_No=Label(DataFrameLeft,bg="powder blue",text="Mobile No",font=("arial",12,"bold"),padx=3,pady=5)
        lblMobile_No.grid(row=8,column=0,sticky=W)
        txtMobile_No=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.mobile_var)
        txtMobile_No.grid(row=8,column=1)

        lblBook_Id=Label(DataFrameLeft,bg="powder blue",text="Book Id",font=("arial",12,"bold"),padx=3,pady=5)
        lblBook_Id.grid(row=0,column=2,sticky=W)
        txtBook_Id=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.bookid_var)
        txtBook_Id.grid(row=0,column=3)

        lblBook_Title=Label(DataFrameLeft,bg="powder blue",text="Book Title",font=("arial",12,"bold"),padx=3,pady=5)
        lblBook_Title.grid(row=1,column=2,sticky=W)
        txtBook_Title=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.booktitle_var)
        txtBook_Title.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,bg="powder blue",text="Auther",font=("arial",12,"bold"),padx=3,pady=5)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.author_var)
        txtAuther.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed",font=("arial",12,"bold"),padx=3,pady=5)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.dateborrowed_var)
        txtDateBorrowed.grid(row=3,column=3)

        lblDate_due=Label(DataFrameLeft,bg="powder blue",text="Date Due:",font=("arial",12,"bold"),padx=3,pady=5)
        lblDate_due.grid(row=4,column=2,sticky=W)
        txtDate_due=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.datedue_var)
        txtDate_due.grid(row=4,column=3)

        lblDays_On_Book=Label(DataFrameLeft,bg="powder blue",text="Days_On_Book",font=("arial",12,"bold"),padx=3,pady=5)
        lblDays_On_Book.grid(row=5,column=2,sticky=W)
        txtDays_On_Book=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.daysonbook_var)
        txtDays_On_Book.grid(row=5,column=3)

        lblLateReturnFine=Label(DataFrameLeft,bg="powder blue",text="Late Ruturn Fine",font=("arial",12,"bold"),padx=3,pady=5)
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.latereturnfine_var)
        txtLateReturnFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due",font=("arial",12,"bold"),padx=3,pady=5)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.dateoverdue_var)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price",font=("arial",12,"bold"),padx=3,pady=5)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",13,"bold"),width=20,textvariable=self.finalprice_var)
        txtActualPrice.grid(row=8,column=3)

    
        # =======================================DataFrame Right===================================

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=4,padx=20,relief=RIDGE,font=("times new roman",12,"bold"))
        DataFrameRight.place(x=680,y=5,width=545,height=335)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=15,padx=4,pady=5)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First Book','Learn Python The Hard Way','Python Programing','Secrete Rahshy','Python CookBook','To Kill a Mockingbird',
                    'The Alchemist','Pride and Prejudice','Sapiens : A Brief History of Humankind','The Great Gatsby','Bhagavad Gita','Ramayan',
                    'SHIVA TRILOGY','Why I Am a Hindu','Vedas','Manusmriti','Yoga Sutrs of Patanjali','Ashtavakra Gita','The Gospel of Sri Ramakrishna',
                    'Vivekachudamani','The life of Swami Vivekananda']

        def SelectBook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("BKID5454")
                self.booktitle_var.set("Python Manual")
                self.author_var.set("Paul Berry")

                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")
            
            elif (x=="Learn Python The Hard Way"):
                 self.bookid_var.set("BKID5455")
                 self.booktitle_var.set("Learn Python The Hard Way")
                 self.author_var.set("Paul")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.345")

            elif (x=="Python Programing"):
                 self.bookid_var.set("BKID5456")
                 self.booktitle_var.set("Python Programing")
                 self.author_var.set("P.Berry")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.530")

            elif (x=="Secrete Rahshy"):
                 self.bookid_var.set("BKID5457")
                 self.booktitle_var.set("Secrete Rahshy")
                 self.author_var.set("P.T.Berry")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.700")

            elif (x=="Python CookBook"):
                 self.bookid_var.set("BKID5458")
                 self.booktitle_var.set("Python CookBook")
                 self.author_var.set("P.B.KALGY")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.560")


            elif (x=="To Kill a Mockingbird"):
                 self.bookid_var.set("BKID5459")
                 self.booktitle_var.set("To Kill a Mockingbird")
                 self.author_var.set("Harper Lee")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.90")

            elif (x=="The Alchemist"):
                 self.bookid_var.set("BKID5460")
                 self.booktitle_var.set("The Alchemist")
                 self.author_var.set("Paul Berry")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.788")

            elif (x=="Pride and Prejudice"):
                 self.bookid_var.set("BKID5461")
                 self.booktitle_var.set("Pride and Prejudice")
                 self.author_var.set("Jane Austen")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.180")

            elif (x=="Sapiens : A Brief History of Humankind"):
                 self.bookid_var.set("BKID5462")
                 self.booktitle_var.set("Sapiens : A Brief History of Humankind")
                 self.author_var.set("Yuval Nouah Harari")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.790")

            elif (x=="The Great Gatsby"):
                 self.bookid_var.set("BKID5463")
                 self.booktitle_var.set("The Great Gatsby")
                 self.author_var.set("F.Scott Fitgerald")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.118")

            elif (x=="Bhagavad Gita"):
                 self.bookid_var.set("BKID5464")
                 self.booktitle_var.set("Bhagavad Gita")
                 self.author_var.set("T.A.Vyasa")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.510")

            elif (x=="Ramayan"):
                 self.bookid_var.set("BKID5465")
                 self.booktitle_var.set("Ramayan")
                 self.author_var.set("valmiki")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.220")

            elif (x=="SHIVA TRILOGY"):
                 self.bookid_var.set("BKID5466")
                 self.booktitle_var.set("SHIVA TRILOGY")
                 self.author_var.set("Amish Tripathi")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.788")

            elif (x=="Why I Am a Hindu"):
                 self.bookid_var.set("BKID5467")
                 self.booktitle_var.set("Why I Am a Hindu")
                 self.author_var.set("Shashi Tharoor")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.560")

            elif (x=="Vedas"):
                 self.bookid_var.set("BKID5468")
                 self.booktitle_var.set("Vedas")
                 self.author_var.set("Rishis")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.150")

            elif (x=="Manusmriti"):
                 self.bookid_var.set("BKID5469")
                 self.booktitle_var.set("Manusmriti")
                 self.author_var.set("Sage Manu")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.170")

            elif (x=="Yoga Sutrs of Patanjali"):
                 self.bookid_var.set("BKID5470")
                 self.booktitle_var.set("Yoga Sutrs of Patanjali")
                 self.author_var.set("Patanjali")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.160")


            elif (x=="Ashtavakra Gita"):
                 self.bookid_var.set("BKID5471")
                 self.booktitle_var.set("Ashtavakra Gita")
                 self.author_var.set("Sage Astavakra")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.90")


            elif (x=="The Gospel of Sri Ramakrishna"):
                 self.bookid_var.set("BKID5472")
                 self.booktitle_var.set("The Gospel of Sri Ramakrishna")
                 self.author_var.set("M.Gupta")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.580")


            elif (x=="Vivekachudamani"):
                 self.bookid_var.set("BKID5473")
                 self.booktitle_var.set("Vivekachudamani")
                 self.author_var.set("Adi Shankaracharya")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.120")


            elif (x=="The life of Swami Vivekananda"):
                 self.bookid_var.set("BKID5474")
                 self.booktitle_var.set("The life of Swami Vivekananda")
                 self.author_var.set("Romain Rolland")

                 d1=datetime.date.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.135")



            
        listbox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=15)
        listbox.bind("<<ListboxSelect>>",SelectBook)
        listbox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listbox.yview)

        
        for item in listBooks:
            listbox.insert(END,item)


        # =====================================Buttons Frame======================================= 
        Framebutton=Frame(self.root,bd=4,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=475,width=1270,height=42)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=19,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)

        
        # =====================================Imformation Frame=================================== 
        FrameDetails=Frame(self.root,bd=8,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=517,width=1270,height=158)

        Table_frame=Frame(FrameDetails,bd=4,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1215,height=138)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)


        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2",
                                                            "postid","mobile","bookid","booktitle","author","dateborrowed","datedue",
                                                            "days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)


        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN NO")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("address1",text="Address 1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("author",text="Author")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Date of Due")
        self.library_table.heading("days",text="Days")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Due")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pass@123",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.member_var.get(),
                self.prn_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook_var.get(),
                self.latereturnfine_var.get(),
                self.dateoverdue_var.get(),
                self.finalprice_var.get()
              ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Member Has been inserted successfully")

    def update(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Pass@123", database="Mydata")
            my_cursor = conn.cursor()

            my_cursor.execute("""
               UPDATE library 
                SET 
                    membertype=%s, 
                    title=%s, 
                    firstname=%s, 
                    lastname=%s, 
                    address1=%s, 
                    address2=%s, 
                    postcode=%s, 
                    mobile=%s, 
                    bookid=%s, 
                    booktitle=%s, 
                    author=%s, 
                    dateborrowed=%s, 
                    datedue=%s, 
                    daysonbook=%s, 
                    latereturnfine=%s, 
                    dateoverdue=%s, 
                    finalprice=%s 
                WHERE prnno=%s
            """, (
                self.member_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook_var.get(),
                self.latereturnfine_var.get(),
                self.dateoverdue_var.get(),
                self.finalprice_var.get(),
                self.prn_var.get(),  # PRN is used to locate the record
         ))

            conn.commit()
            self.fatch_data()  # Refresh table data
            self.reset()  # Clear input fields
            conn.close()

            messagebox.showinfo("Success", "Member details updated successfully.")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {err}")
        except Exception as ex:
            messagebox.showerror("Error", f"Unexpected Error: {ex}")


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Pass@123",database="Mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for row in rows:
                self.library_table.insert("",END,values=row)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+ self.member_var.get() + "\n")
        self.txtBox.insert(END,"PRN_No\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"Title\t\t"+ self.id_var.get() + "\n")                                                                                                        
        self.txtBox.insert(END,"First Name\t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Last Name\t\t"+ self.lastname_var.get() + "\n")
        self.txtBox.insert(END,"Address 1\t\t"+ self.address1_var.get() + "\n")
        self.txtBox.insert(END,"Address 2\t\t"+ self.address2_var.get() + "\n")
        self.txtBox.insert(END,"Post Code\t\t"+ self.postcode_var.get() + "\n")
        self.txtBox.insert(END,"Mobile\t\t"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Book ID\t\t"+ self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Title\t\t"+ self.booktitle_var.get() + "\n")
        self.txtBox.insert(END,"Author\t\t"+ self.author_var.get() + "\n")
        self.txtBox.insert(END,"Date borrowed\t\t"+ self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END,"Date of Due\t\t"+ self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"Days On Book\t\t"+ self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END,"Late Return Fine\t\t"+ self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END,"Date Over Due\t\t"+ self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END,"Final Price\t\t"+ self.finalprice_var.get() + "\n")


    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Managenent System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return



    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select The Member")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Pass@123", database="Mydata")
            my_cursor = conn.cursor()
            query="Delete from library where prnno=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Member has been Deleted")


if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()
