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
issueTable = "items_issued" #Issue Table
jewelleryTable = "jewellery" #Book Table


alljid = [] #List To store all Book IDs

def returnJ():
    
    global SubmitBtn,labelFrame,lb1,jewelleryInfo1,quitBtn,root,Canvas1,status
    
    jid = jewelleryInfo1.get()

    extractjid = "select bid from "+issueTable
    try:
        cur.execute(extractjid)
        con.commit()
        for i in cur:
            alljid.append(i[0])
        
        if jid in alljid:
            checkAvail = "select j_status from "+jewelleryTable+" where jid = '"+jid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Jewellery ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Jewellery IDs")
    
    
    issueSql = "delete from items_issued where jid = '"+jid+"'"
  
    print(jid in alljid)
    print(status)
    updateStatus = "update "+jewelleryTable+" set j_status = 'avail' where jid = '"+jid+"'"
    try:
        if jid in alljid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Jewellery Returned Successfully")
        else:
            alljid.clear()
            messagebox.showinfo('Message',"Please check the jewellery ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    alljid.clear()
    root.destroy()
    
def returnJewellery(): 
    
    global jewelleryInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Costume Rentals")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Jewellery", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Jewellery ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    jewelleryInfo1 = Entry(labelFrame)
    jewelleryInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnJ)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()