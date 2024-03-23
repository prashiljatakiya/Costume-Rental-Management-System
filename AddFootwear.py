from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def footwearRegister():
    
    fid = footwearInfo1.get()
    item_name = footwearInfo2.get()
    category = footwearInfo3.get()
    status = footwearInfo4.get()
    status = status.lower()
    
    insertCostume = "insert into "+footwearTable+" values('"+fid+"','"+item_name+"','"+category+"','"+status+"')"
    try:
        cur.execute(insertCostume)
        con.commit()
        messagebox.showinfo('Success',"Footwear added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(fid)
    print(item_name)
    print(category)
    print(status)


    root.destroy()
    
def addFootwear(): 
    
    global footwearInfo1,footwearInfo2,footwearInfo3,footwearInfo4,Canvas1,con,cur,footwearTable,root
    
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
    footwearTable = "footwear" # Book Table

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Footwear", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Costume ID
    lb1 = Label(labelFrame,text="Footwear ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    footwearInfo1 = Entry(labelFrame)
    footwearInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Item name
    lb2 = Label(labelFrame,text="Footwear Price : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    footwearInfo2 = Entry(labelFrame)
    footwearInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # costume owner
    lb3 = Label(labelFrame,text="Category : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    footwearInfo3 = Entry(labelFrame)
    footwearInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # costume Status
    lb4 = Label(labelFrame,text="Status(Available/Rented) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    footwearInfo4 = Entry(labelFrame)
    footwearInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=footwearRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()