
#################################################################################################################################################################################
from tkinter import *

from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddCostume import *
from DeleteCostume import *
from ViewCostumes import *
from RentCostume import *
from ReturnCostume import *
from AddProps import *
from DeleteProps import *
from ViewProps import *
from RentProps import *
from ReturnProps import *
from AddFootwear import *
from DeleteFootwear import *
from ViewFootwear import *
from RentFootwear import *
from ReturnFootwear import *
from AddJewellery import *
from DeleteJewellery import *
from ViewJewellery import *
from RentJewellery import *
from ReturnJewellery import *
from showcustomers import *

# Add your own database name and password here to reflect in the code

# to run it on MYSQL server on CMD code: mysql -u root -p
# 
# create table books(cid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
# create table books_issued(cid varchar(20) primary key, issuedto varchar(30));
mypass = "Prashil@09"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Costume Rentals")
root.attributes('-fullscreen', True)
# root.minsize(width=600,height=500)
root.geometry("1600x500")
# root.resizable(False, False)


# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image

# background_image =Image.open('lib.jpg') 
# [imageSizeWidth, imageSizeHeight] = background_image.size

# newImageSizeWidth = int(imageSizeWidth*n)
# if same:
#     newImageSizeHeight = int(imageSizeHeight*n) 
# else:
#     newImageSizeHeight = int(imageSizeHeight/n) 
    
# background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
# img = ImageTk.PhotoImage(background_image)

# Canvas1 = Canvas(root)

# Canvas1.create_image(300,340,image = img)      
# Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
# Canvas1.pack(expand=True,fill=BOTH)



screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window dimensions
window_width = screen_width
window_height = screen_height

# Set the window geometry
root.geometry(f"{window_width}x{window_height}")

# Set window minimum size
root.minsize(width=600, height=window_height)

# Create a canvas to fill the window
canvas = Canvas(root, width=window_width, height=window_height)
canvas.pack(fill="both", expand=True)

color_start = "#9370DB"  # Medium Purple
color_end = "#FFD700"    # Gold


# Create a gradient effect using rectangles with slightly different colors
for i in range(window_width):
    # Calculate the color between start and end colors
    color = '#%02x%02x%02x' % (
        int(255 - (255 - int(color_end[1:3], 16)) * (i / window_width)),
        int(255 - (255 - int(color_end[3:5], 16)) * (i / window_width)),
        int(255 - (255 - int(color_end[5:], 16)) * (i / window_width))
    )
    canvas.create_rectangle(i, 0, i + 1, window_height, fill=color, outline="")





headingFrame1 = Frame(root,bg="#800080",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Ready-to-Wear Costume Rentals \n by Prashil Jatakiya & Kruthik K ", bg='black', fg='white', font=('Garamond',20))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text=" 👗 Add Costumes",bg='dark slate grey', fg='white',font=('Helvetica',16), command=addCostume)
btn1.place(relx=0.05,rely=0.4, relwidth=0.20,relheight=0.1)
    
btn2 = Button(root,text="👗 Delete Costume",bg='black', fg='white',font=('Helvetica',16), command=deleteC)
btn2.place(relx=0.05,rely=0.5, relwidth=0.20,relheight=0.1)
    
btn3 = Button(root,text="👗 View Costumes",bg='dark slate grey', fg='white',font=('Helvetica',16), command=ViewC)
btn3.place(relx=0.05,rely=0.6, relwidth=0.20,relheight=0.1)
    
btn4 = Button(root,text="👗 Rent Costumes",bg='black', fg='white',font=('Helvetica',16), command = rentCostume)
btn4.place(relx=0.05,rely=0.7, relwidth=0.20,relheight=0.1)

btn5 = Button(root,text="👗 Return Costume",bg='dark slate grey', fg='white',font=('Helvetica',16), command = returnCostume)
btn5.place(relx=0.05,rely=0.8, relwidth=0.20,relheight=0.1)

btn6 = Button(root,text="🎭 Add Props",bg='dark slate grey', fg='white',font=('Helvetica',16), command=addProps)
btn6.place(relx=0.27,rely=0.4, relwidth=0.20,relheight=0.1)
    
btn7 = Button(root,text="🎭 Delete Props",bg='black', fg='white',font=('Helvetica',16), command=deleteP)
btn7.place(relx=0.27,rely=0.5, relwidth=0.20,relheight=0.1)
    
btn8 = Button(root,text="🎭 View Props",bg='dark slate grey', fg='white',font=('Helvetica',16), command=ViewP)
btn8.place(relx=0.27,rely=0.6, relwidth=0.20,relheight=0.1)
    
btn9 = Button(root,text="🎭 Rent Props",bg='black', fg='white',font=('Helvetica',16), command = rentProps)
btn9.place(relx=0.27,rely=0.7, relwidth=0.20,relheight=0.1)
    
btn10 = Button(root,text="🎭 Return Props",bg='dark slate grey', fg='white',font=('Helvetica',16), command = returnProps)
btn10.place(relx=0.27,rely=0.8, relwidth=0.20,relheight=0.1)


btn11 = Button(root,text="👞👠 Add Footwear",bg='dark slate grey', fg='white',font=('Helvetica',16), command=addFootwear)
btn11.place(relx=0.49,rely=0.4, relwidth=0.20,relheight=0.1)
    
btn12 = Button(root,text="👞👠 Delete Footwear",bg='black', fg='white',font=('Helvetica',16), command=deleteF)
btn12.place(relx=0.49,rely=0.5, relwidth=0.20,relheight=0.1)
    
btn13 = Button(root,text="👞👠 View Footwear",bg='dark slate grey', fg='white',font=('Helvetica',16), command=ViewF)
btn13.place(relx=0.49,rely=0.6, relwidth=0.20,relheight=0.1)
    
btn14 = Button(root,text="👞👠 Rent Footwear",bg='black', fg='white',font=('Helvetica',16), command = rentFootwear)
btn14.place(relx=0.49,rely=0.7, relwidth=0.20,relheight=0.1)
    
btn15 = Button(root,text="👞👠 Return Footwear",bg='dark slate grey', fg='white',font=('Helvetica',16), command = returnFootwear)
btn15.place(relx=0.49,rely=0.8, relwidth=0.20,relheight=0.1)

btn16 = Button(root,text="💍📿 Add Jewellery",bg='dark slate grey', fg='white',font=('Helvetica',16), command=addJewellery)
btn16.place(relx=0.71,rely=0.4, relwidth=0.20,relheight=0.1)
    
btn17 = Button(root,text="💍📿 Delete Jewellery",bg='black', fg='white',font=('Helvetica',16), command=deleteJ)
btn17.place(relx=0.71,rely=0.5, relwidth=0.20,relheight=0.1)
    
btn18 = Button(root,text="💍📿 View Jewellery",bg='dark slate grey', fg='white',font=('Helvetica',16), command=ViewJ)
btn18.place(relx=0.71,rely=0.6, relwidth=0.20,relheight=0.1)
    
btn19 = Button(root,text="💍📿 Rent Jewellery",bg='black', fg='white',font=('Helvetica',16), command = rentJewellery)
btn19.place(relx=0.71,rely=0.7, relwidth=0.20,relheight=0.1)
    
btn20 = Button(root,text="💍📿 Return Jewellery",bg='dark slate grey', fg='white',font=('Helvetica',16), command = returnJewellery)
btn20.place(relx=0.71,rely=0.8, relwidth=0.20,relheight=0.1)

btn21=Button(root,text="👩‍💼👨‍💼 Show Customer List",bg='black', fg='white',font=('Helvetica',16), command = showcustomers)
btn21.place(relx=0.05,rely=0.91, relwidth=0.86,relheight=0.05)

root.mainloop()



##In MY SQL for seeing DMs code : show databases;
## for selecting DB code : use db;
## for seeing the tables: show tables;
## for creatig view code : create view a as select * from [table name: ]
## for selecting / viewing code : select * from a; or [select * from books]
## for deleting element code: drop view a;

