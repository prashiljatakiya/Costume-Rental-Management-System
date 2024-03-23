from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def jewelleryRegister():
    
    jid = jewelleryInfo1.get()
    item_name = jewelleryInfo2.get()
    category = jewelleryInfo3.get()
    status = jewelleryInfo4.get()
    status = status.lower()
    
    insertJewellery = "insert into "+jewelleryTable+" values('"+jid+"','"+item_name+"','"+category+"','"+status+"')"
    try:
        cur.execute(insertJewellery)
        con.commit()
        messagebox.showinfo('Success',"Jewellery added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(jid)
    print(item_name)
    print(category)
    print(status)


    root.destroy()
    
def addJewellery(): 
    
    global jewelleryInfo1,jewelleryInfo2,jewelleryInfo3,jewelleryInfo4,Canvas1,con,cur,jewelleryTable,root
    
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
    jewelleryTable = "jewellery" 
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Jewellery", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Costume ID
    lb1 = Label(labelFrame,text="Jewellery ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    jewelleryInfo1 = Entry(labelFrame)
    jewelleryInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Item name
    lb2 = Label(labelFrame,text="Jewellery Price : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    jewelleryInfo2 = Entry(labelFrame)
    jewelleryInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    # costume owner
    lb3 = Label(labelFrame,text="Category : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    jewelleryInfo3 = Entry(labelFrame)
    jewelleryInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    # costume Status
    lb4 = Label(labelFrame,text="Status(Available/Rented) : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    jewelleryInfo4 = Entry(labelFrame)
    jewelleryInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=jewelleryRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()