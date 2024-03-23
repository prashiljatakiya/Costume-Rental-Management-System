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
issueTable = "items_issued" 
footwearTable = "footwear" #Book Table


def deleteFootwear():
    
    fid = footwearInfo1.get()
    
    deleteSql = "delete from "+footwearTable+" where fid = '"+fid+"'"
    deleteIssue = "delete from "+issueTable+" where bid = '"+fid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success',"Footwear Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check footwear ID")
    

    print(fid)

    footwearInfo1.delete(0, END)
    root.destroy()
    
def deleteF(): 
    
    global footwearInfo1, footwearInfo2,footwearInfo3,footwearInfo4,Canvas1,con,cur,footwearTable,root
    
    root = Tk()
    root.title("Costume Rentals")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Footwear", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Footwear ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    footwearInfo1 = Entry(labelFrame)
    footwearInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteFootwear)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()