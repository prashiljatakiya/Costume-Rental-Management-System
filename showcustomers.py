from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "Prashil@09"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
Table = "items_issued" 
    
def showcustomers(): 
    
    root = Tk()
    root.title("Costume Rentals")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Show Customers", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-10s%-20s%-20s%-20s%-20s%-20s"%('CID','JID','PID','FID','NAME','CONTACT'), bg='black', fg='white').place(relx=0.07, rely=0.1)

    Label(labelFrame, text="----------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getcustomers = "select * from "+Table
    try:
        cur.execute(getcustomers)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-10s%-20s%-20s%-20s%-20s%-20s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()























# from tkinter import *
# from tkinter import messagebox
# import pymysql

# # Add your own database name and password here to reflect in the code
# mypass = "Prashil@09"
# mydatabase = "db"

# con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
# cur = con.cursor()

# # Enter Table Names here
# Table = "items_issued"

# # Create the trigger
# try:
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS issued_log (
#             log_id INT AUTO_INCREMENT PRIMARY KEY,
#             item_id INT,
#             issued_to VARCHAR(100),
#             issued_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#         )
#     """)
    
#     cur.execute("""
#         CREATE TRIGGER IF NOT EXISTS after_items_issued_insert
#         AFTER INSERT ON items_issued
#         FOR EACH ROW
#         BEGIN
#             INSERT INTO issued_log (item_id, issued_to)
#             VALUES (NEW.id, NEW.issued_to);
#         END
#     """)
#     con.commit()
# except pymysql.Error as e:
#     messagebox.showinfo("Error creating trigger", str(e))

# def showcustomers(): 
#     root = Tk()
#     root.title("Costume Rentals")
#     root.minsize(width=400, height=400)
#     root.geometry("600x500")

#     Canvas1 = Canvas(root)
#     Canvas1.config(bg="#12a4d9")
#     Canvas1.pack(expand=True, fill=BOTH)

#     headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
#     headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

#     headingLabel = Label(headingFrame1, text="Show Customers", bg='black', fg='white', font=('Courier', 15))
#     headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

#     labelFrame = Frame(root, bg='black')
#     labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
#     y = 0.25

#     Label(labelFrame, text="%-10s%-20s" % ('ID', 'Issued To'), bg='black', fg='white').place(relx=0.07, rely=0.1)
#     Label(labelFrame, text="----------------------------------------------------------------------------",
#           bg='black', fg='white').place(relx=0.05, rely=0.2)
    
#     getcustomers = "SELECT * FROM " + Table
#     try:
#         cur.execute(getcustomers)
#         con.commit()
#         for i in cur:
#             Label(labelFrame, text="%-10s%-20s" % (i[0], i[1]), bg='black', fg='white').place(relx=0.07, rely=y)
#             y += 0.1
#     except pymysql.Error:
#         messagebox.showinfo("Failed to fetch files from database")

#     quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
#     quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

#     root.mainloop()

# # Call the function to display customers
# showcustomers()


