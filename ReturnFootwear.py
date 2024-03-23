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
footwearTable = "footwear" #Book Table


allFid = [] #List To store all Book IDs

def returnF():
    
    global SubmitBtn,labelFrame,lb1,footwearInfo1,quitBtn,root,Canvas1,status
    
    fid = footwearInfo1.get()

    extractFid = "select bid from "+issueTable
    try:
        cur.execute(extractFid)
        con.commit()
        for i in cur:
            allFid.append(i[0])
        
        if fid in allFid:
            checkAvail = "select f_status from "+footwearTable+" where fid = '"+fid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Footwear ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Footwear IDs")
    
    
    issueSql = "delete from items_issued where fid = '"+fid+"'"
  
    print(fid in allFid)
    print(status)
    updateStatus = "update "+footwearTable+" set f_status = 'avail' where fid = '"+fid+"'"
    try:
        if fid in allFid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Footwear Returned Successfully")
        else:
            allFid.clear()
            messagebox.showinfo('Message',"Please check the footwear ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    allFid.clear()
    root.destroy()
    
def returnFootwear(): 
    
    global footwearInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Costume Rentals")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Footwear", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Footwear ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    footwearInfo1 = Entry(labelFrame)
    footwearInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnF)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()