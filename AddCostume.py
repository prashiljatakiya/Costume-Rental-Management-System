from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def costumeRegister():
    
    cid = costumeInfo1.get()
    item_name = costumeInfo2.get()
    category = costumeInfo3.get()
    status = costumeInfo4.get()
    status = status.lower()
    
    insertCostume = "insert into "+costumeTable+" values('"+cid+"','"+item_name+"','"+category+"','"+status+"')"
    try:
        cur.execute(insertCostume)
        con.commit()
        messagebox.showinfo('Success',"Costume added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(cid)
    print(item_name)
    print(category)
    print(status)


    root.destroy()
    
def addCostume(): 
    
    global costumeInfo1,costumeInfo2,costumeInfo3,costumeInfo4,Canvas1,con,cur,costumeTable,root
    
    root = Tk()
    root.title("Costume Rentals")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "Prashil@09"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    costumeTable = "costumes" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Costumes", bg='black', fg='white', font=('Helvetica',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Costume ID
    lb1 = Label(labelFrame,text="Costume ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    costumeInfo1 = Entry(labelFrame)
    costumeInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Item name
    lb2 = Label(labelFrame,text="Item Name : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    costumeInfo2 = Entry(labelFrame)
    costumeInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # costume owner
    lb3 = Label(labelFrame,text="Category : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    costumeInfo3 = Entry(labelFrame)
    costumeInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # costume Status
    lb4 = Label(labelFrame,text="Status(Available/Rented) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    costumeInfo4 = Entry(labelFrame)
    costumeInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=costumeRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()