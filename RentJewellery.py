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
jewelleryTable = "jewellery"
    
#List To store all Book IDs
allJid = [] 

def jewelleryissue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    jid = inf1.get()
    issueto = inf2.get()
    contact=inf3.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractJid = "select jid from "+jewelleryTable
    try:
        cur.execute(extractJid)
        con.commit()
        for i in cur:
            allJid.append(i[0])
        
        if jid in allJid:
            checkAvail = "select j_status from "+jewelleryTable+" where jid = '"+jid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Jewellery ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Jewellery IDs")
    
    issueSql = "insert into items_issued (jid, issuedto, contact_number) values (%s, %s, %s)"
    values = (jid, issueto, contact)
    show = "select * from "+issueTable
    
    updateStatus = "update "+jewelleryTable+" set j_status = 'issued' where jid = '"+jid+"'"
    try:
        if jid in allJid and status == True:
            cur.execute(issueSql,values)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Jewellery Rented Successfully")
            root.destroy()
        else:
            allJid.clear()
            messagebox.showinfo('Message',"Jewellery Already Rented")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(jid)
    print(issueto)
    print(contact)
    
    allJid.clear()
    
def rentJewellery(): 
    
    global issueBtn,labelFrame,lb1,lb2,lb3,inf3,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Costume Rentals")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Rent Jewellery", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Jewellery ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    lb3 = Label(labelFrame,text="Phone Number : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.5)
        
    inf3 = Entry(labelFrame)
    inf3.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Issue Button
    issueBtn = Button(root,text="Rent",bg='#d1ccc0', fg='black',command=jewelleryissue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()