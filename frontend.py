# front end
from tkinter import *
import tkinter.messagebox
import backend as db


class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Management System")
        self.root.geometry(newGeometry="1175x540")
        self.root.resizable(False, False)
        self.root.config(bg="silver")
        # ----------------------------------------------------------------------------------
        StdId = StringVar()
        Name = StringVar()
        USN = StringVar()
        Dept = StringVar()
        DOB = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Phone = StringVar()
        # --------------------------------------FUNCTIONS-------------------------------------------------------------------
        db.studentData()

        def iExit():
            iExit = tkinter.messagebox.askyesno(
                "Student Database", "Are you sure you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtStdId.delete(0, END)
            self.txtName.delete(0, END)
            self.txtUSN.delete(0, END)
            self.txtDept.delete(0, END)
            self.txtDOB.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtPhone.delete(0, END)
        db.studentData()

        def addData():
            if(len(StdId.get()) != 0):

                db.addStdRec(StdId.get(), Name.get(), USN.get(
                ), Dept.get(), DOB.get(), Gender.get(), Address.get(), Phone.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdId.get(), Name.get(), USN.get(
                ), Dept.get(), DOB.get(), Gender.get(), Address.get(), Phone.get()))

        def DisplayData():
            studentlist.delete(0, END)
            for row in db.viewData():
                studentlist.insert(END, row)

        def StudentRec(event):
            global sd
            searchstd = studentlist.curselection()[0]
            sd = studentlist.get(searchstd)
            self.txtStdId.delete(0, END)
            self.txtStdId.insert(END, sd[0])
            self.txtName.delete(0, END)
            self.txtName.insert(END, sd[1])
            self.txtUSN.delete(0, END)
            self.txtUSN.insert(END, sd[2])
            self.txtDept.delete(0, END)
            self.txtDept.insert(END, sd[3])
            self.txtDOB.delete(0, END)
            self.txtDOB.insert(END, sd[4])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[5])
            self.txtAddress.delete(0, END)
            self.txtAddress.insert(END, sd[6])
            self.txtPhone.delete(0, END)
            self.txtPhone.insert(END, sd[7])

        def DeleteData():

            if(len(StdId.get()) != 0):
                db.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0, END)
            for row in db.searchData(StdId.get(), Name.get(), USN.get(), Dept.get(), DOB.get(), Gender.get(), Address.get(), Phone.get()):
                studentlist.insert(END, row, str(""))

        def update():
            if(len(StdId.get()) != 0):
                db.deleteRec(sd[0])
            if(len(StdId.get()) != 0):
                db.addStdRec(StdId.get(), Name.get(), USN.get(
                ), Dept.get(), DOB.get(), Gender.get(), Address.get(), Phone.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (StdId.get(), Name.get(), USN.get(
                ), Dept.get(), DOB.get(), Gender.get(), Address.get(), Phone.get()))

        # --------------------------------------Frames-----------------------------------------------------------------------__________________________________________________________
        MainFrame = Frame(self.root, bg="white")
        MainFrame.grid()  # THIS IS MAIN FRAME OUR WINDOW
        TitFrame = Frame(MainFrame, bd=1, padx=45,
                         pady=8, bg="silver", relief=RIDGE)
        TitFrame.pack(side=TOP)  # THIS IS STITLE FRAME

        self.lblTit = Label(TitFrame, font=('calibri', 48, 'bold'),
                            text="Student Database Management System", bg="silver", fg="black")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=1, width=1350,
                            height=70, padx=18, pady=10, bg="silver", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=9, width=1300, height=400,
                          padx=20, pady=20, bg="#555", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, font=('calibri', 12, 'bold'), bd=1, width=450,
                                   height=300, bg="Ghost White", relief=RIDGE, text="STUDENT INFORMATION\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, font=('calibri', 12, 'bold'), bd=1, width=450,
                                    height=300, bg="Ghost White", relief=RIDGE, text="STUDENT DETAILS\n")
        DataFrameRight.pack(side=RIGHT)
# --------------------------------entries-------------------------------------------------------------------------------------------------

        self.lblStdId = Label(DataFrameLeft, font=(
            'calibri', 12, 'bold'), padx=2, pady=3, text="Student ID:", bg="ghost white")
        self.lblStdId.grid(row=0, column=0, sticky=W)

        self.txtStdId = Entry(DataFrameLeft, font=(
            'calibri', 12, 'bold'), textvariable=StdId, bg="ghost white", width=39)
        self.txtStdId.grid(row=0, column=1)  # student id

        self.lblName = Label(DataFrameLeft, font=(
            'calibri', 12, 'bold'), padx=2, pady=3, text="Name:", bg="ghost white")
        self.lblName.grid(row=1, column=0, sticky=W)

        self.txtName = Entry(DataFrameLeft, font=(
            'calibri', 12, 'bold'), textvariable=Name, bg="ghost white", width=39)
        self.txtName.grid(row=1, column=1)  # name

        self.lblUSN = Label(DataFrameLeft, font=(
            'calibri', 12, 'bold'), padx=2, pady=3, text="USN:", bg="ghost white")
        self.lblUSN.grid(row=2, column=0, sticky=W)

        self.txtUSN = Entry(DataFrameLeft, font=(
            'calibri', 12, 'bold'), textvariable=USN, bg="ghost white", width=39)
        self.txtUSN.grid(row=2, column=1)  # USN

        self.lblDept = Label(DataFrameLeft, font=(
            'calibri', 12, 'bold'), padx=2, pady=3, text="Department", bg="ghost white")
        self.lblDept.grid(row=3, column=0, sticky=W)

        self.txtDept = Entry(DataFrameLeft, font=(
            'calibri', 12, 'bold'), textvariable=Dept, bg="ghost white", width=39)
        self.txtDept.grid(row=3, column=1)  # department

        self.lblDOB = Label(DataFrameLeft, font=(
            'calibri', 12, 'bold'), padx=2, pady=3, text="Date of Birth:", bg="ghost white")
        self.lblDOB.grid(row=4, column=0, sticky=W)

        self.txtDOB = Entry(DataFrameLeft, font=(
            'calibri', 12, 'bold'), textvariable=DOB, bg="ghost white", width=39)
        self.txtDOB.grid(row=4, column=1)  # DOB

        self.lblGender = Label(DataFrameLeft, font=(
            'calibri', 12, 'bold'), padx=2, pady=3, text="Gender:", bg="ghost white")
        self.lblGender.grid(row=5, column=0, sticky=W)

        self.txtGender = Entry(DataFrameLeft, font=(
            'calibri', 12, 'bold'), textvariable=Gender, bg="ghost white", width=39)
        self.txtGender.grid(row=5, column=1)  # gender

        self.lblAddress = Label(DataFrameLeft, font=(
            'calibri', 12, 'bold'), padx=2, pady=3, text="Address:", bg="ghost white")
        self.lblAddress.grid(row=6, column=0, sticky=W)

        self.txtAddress = Entry(DataFrameLeft, font=(
            'calibri', 12, 'bold'), textvariable=Address, bg="ghost white", width=39)
        self.txtAddress.grid(row=6, column=1)  # address

        self.lblPhone = Label(DataFrameLeft, font=(
            'calibri', 12, 'bold'), padx=2, pady=3, text="Phone No:", bg="ghost white")
        self.lblPhone.grid(row=7, column=0, sticky=W)

        self.txtPhone = Entry(DataFrameLeft, font=(
            'calibri', 12, 'bold'), textvariable=Phone, bg="ghost white", width=39)
        self.txtPhone.grid(row=7, column=1)  # Phone

        # --------------------------------------scroll bar and list box----------------------------------------------------------------------------
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')  # scroll bar

        studentlist = Listbox(DataFrameRight, width=68, height=12, font=(
            'calibri', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=10)
        scrollbar.config(command=studentlist.yview)

        # --------------------------------------buttons-----------------------------------------------------------------------------------------------------------
        self.btnAddData = Button(ButtonFrame, text="Add New", font=(
            'calibri', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=addData)
        self.btnAddData.grid(row=0, column=0)  # ADD NEW

        self.btnDisplay = Button(ButtonFrame, text="Display", font=(
            'calibri', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=DisplayData)
        self.btnDisplay.grid(row=0, column=1)  # DISPLAY

        self.btnClear = Button(ButtonFrame, text="Clear", font=(
            'calibri', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=clearData)
        self.btnClear.grid(row=0, column=2)  # CLEAR

        self.btnDelete = Button(ButtonFrame, text="Delete", font=(
            'calibri', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=DeleteData)
        self.btnDelete.grid(row=0, column=3)  # DELETE

        self.btnSearch = Button(ButtonFrame, text="Search", font=(
            'calibri', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=searchDatabase)
        self.btnSearch.grid(row=0, column=4)  # SEARCH

        self.btnUpdate = Button(ButtonFrame, text="Update", font=(
            'calibri', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=update)
        self.btnUpdate.grid(row=0, column=5)  # UPDATE

        self.btnExit = Button(ButtonFrame, text="Exit", font=(
            'calibri', 20, 'bold'), height=1, width=10, bd=4, fg="#555", command=iExit)
        self.btnExit.grid(row=0, column=6)  # EXIT


if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
