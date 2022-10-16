import mysql.connector


def studentData():
    con = mysql.connector.connect(
        host="localhost", user="root", password="*******", database="student")
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS student(id integer primary key AUTO_INCREMENT,StdID text,Name text,USN text,Dept text,DOB text,Gender text,Address text,Phone text)")
    con.commit()
    con.close()


def addStdRec(StdID, Name, USN, Dept, DOB, Gender, Address, Phone):
    con = mysql.connector.connect(
        host="localhost", user="root", password="root@123")
    cur = con.cursor()
    cur.execute("use student")
    cur.execute("INSERT INTO student VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)",
                (StdID, Name, USN, Dept, DOB, Gender, Address, Phone))
    con.commit()
    con.close()


def viewData():
    con = mysql.connector.connect(
        host="localhost", user="root", password="root@123")
    cur = con.cursor()
    cur.execute("use student")
    cur.execute("select * from student")
    row = cur.fetchall()
    con.close()
    return row


def deleteRec(id):
    con = mysql.connector.connect(
        host="localhost", user="root", password="root@123")
    cur = con.cursor()
    cur.execute("use student")
    cur.execute("DELETE FROM student WHERE id=%s", (id,))
    con.commit()
    con.close()


def searchData(StdID, Name, USN, Dept, DOB, Gender, Address, Phone):
    con = mysql.connector.connect(
        host="localhost", user="root", password="root@123")
    cur = con.cursor()
    cur.execute("use student")
    cur.execute("SELECT * FROM student WHERE StdID=%s or Name=%s or USN=%s or Dept=%s or DOB=%s or Gender=%s or Address=%s or Phone=%s",
                (StdID, Name, USN, Dept, DOB, Gender, Address, Phone))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, StdID="", Name="", USN="", Dept="", DOB="", Gender="", Address="", Phone=""):
    con = mysql.connector.connect(
        host="localhost", user="root", password="root@123")
    cur = con.cursor()
    cur.execute("use student")
    cur.execute("UPDATE student SET StdID=%s,Name=%s,USN=%s,Dept=%s,DOB=%s,Gender=%s,Address=%s,Phone=%s WHERE id=%s",
                (StdID, Name, USN, Dept, DOB, Gender, Address, Phone))
    con.commit()
    con.close()
