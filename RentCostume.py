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
costumeTable = "costumes"
    
#List To store all Book IDs
allCid = [] 


# def validate_contact_numbers(number_to_validate):
#     validation_results = {}

#     def validate_contact_number(contact_number):
#         nonlocal validation_results
#         with con.cursor() as cursor:
#             cursor.execute("CALL ValidateContactNumber(%s, @result)", (contact_number,))
#             cursor.execute("SELECT @result AS 'Validation Result'")
#             result = cursor.fetchone()
#             return result['Validation Result']

#     for number in number_to_validate:
#         validation_results[number] = validate_contact_number(number)

#     return validation_results

# # Example usage:
# # Replace '9876543210', '1234567890', etc., with the numbers you want to validate
# numbers_to_check = ['9876543210', '1234567890', '8765432109']
# results = validate_contact_numbers(numbers_to_check)

# for number, result in results.items():
#     print(f"Validation for {number}: {result}")



def costumerent():
    
#     global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
#     cid = inf1.get()
#     issueto = inf2.get()
#     contact=inf3.get()

#     issueBtn.destroy()
#     labelFrame.destroy()
#     lb1.destroy()
#     inf1.destroy()
#     inf2.destroy()
    
    
#     extractCid = "select cid from "+costumeTable
#     try:
#         cur.execute(extractCid)
#         con.commit()
#         for i in cur:
#             allCid.append(i[0])
        
#         if cid in allCid:
#             checkAvail = "select c_status from "+costumeTable+" where cid = '"+cid+"'"
#             cur.execute(checkAvail)
#             con.commit()
#             for i in cur:
#                 check = i[0]
                
#             if check == 'avail':
#                 status = True
#             else:
#                 status = False

#         else:
#             messagebox.showinfo("Error","Costume ID not present")
#     except:
#         messagebox.showinfo("Error","Can't fetch Costume IDs")
    
    

#     issueSql = "insert into items_issued (cid, issuedto, contact_number) values (%s, %s, %s)"
#     values = (cid, issueto, contact)

# # Execute the query with user inputs as parameters


#     # issueSql = "insert into "+issueTable+" values ('"+pid+"','"+issueto+"')"
#     show = "select * from "+issueTable
    
#     show = "select * from "+issueTable
    
#     updateStatus = "update "+costumeTable+" set c_status = 'issued' where cid = '"+cid+"'"
#     try:
#         if cid in allCid and status == True:
#             cur.execute(issueSql, values)
#             con.commit()
#             cur.execute(updateStatus)
#             con.commit()
#             messagebox.showinfo('Success',"Costume Issued Successfully")
#             root.destroy()
#         else:
#             allCid.clear()
#             messagebox.showinfo('Message',"Costume Already Issued")
#             root.destroy()
#             return
#     except:
#         messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
#     print(cid)
#     print(issueto)
#     print(contact)
    
#     allCid.clear()

    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1

    cid = inf1.get()
    issueto = inf2.get()
    contact = inf3.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    try:
        with con.cursor() as cur:
            # Nested queries to check availability and insert data
            cur.execute("SELECT c_status FROM {} WHERE cid = %s".format(costumeTable), (cid,))
            check = cur.fetchone()

            if check:
                if check[0] == 'avail':
                    cur.execute(
                        "INSERT INTO {} (cid, issuedto, contact_number) VALUES (%s, %s, %s)".format(issueTable),
                        (cid, issueto, contact)
                    )
                    con.commit()

                    cur.execute(
                        "UPDATE {} SET c_status = 'issued' WHERE cid = %s".format(costumeTable), (cid,)
                    )
                    con.commit()

                    messagebox.showinfo('Success', "Costume Issued Successfully")
                    root.destroy()
                else:
                    messagebox.showinfo('Message', "Costume Already Issued")
                    root.destroy()
            else:
                messagebox.showinfo("Error", "Costume ID not present")
    except pymysql.Error as e:
        messagebox.showinfo("Error", f"Error: {str(e)}")
        con.rollback()

    allCid.clear()

    
def rentCostume(): 
    
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
        
    headingLabel = Label(headingFrame1, text="Rent Costume", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Costume ID : ", bg='black', fg='white')
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
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=costumerent)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()