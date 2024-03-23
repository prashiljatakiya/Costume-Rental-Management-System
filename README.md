# Costume-Rental-Management-System
Costume-Rental-management-System is a simple database management project aimed at helping costume rental shops to keep track of their costumes, footwear, jewellery, and props. The owners can easily manage their items by this system which is made using python, tkinter and mysql database which is easy to understand and use as well.  



>Dependencies:

- tkinter
- pillow
- pymysql
- MySQL should be instaled

Code to download dependencies:
```
pip install tk
pip install pillow
pip install pymysql
```

>❗ IMPORTANT STEP ❗

- Make sure you have installed MySQL for your OS, if not follow this video : ```https://www.youtube.com/watch?v=N3B3OonC2AU&t=343s ``` *Not sponcered*
- Follow the above video carefully and we recommend to use the password as ```root``` (here in this case I have added my own password i.e."Prashil@09")
- After you have successfully installed and tested now you will need to run a few commands before running the ```main.py`
- Open ``` MySQL 8.0(or any version) Command Line Client``` using windows key and searching it if you use windows
- Enter the password in this case we use ```Prashil@09```
- We add our data based which we will call `db` code for it : ```create database db;```
- Run the below command mentioned to make the necessary tables:
- ```create table costumes(cid varchar(20) primary key, c_price int, c_category varchar(20), c_status varchar(30));```
- ```create table props(pid varchar(20) primary key, p_price int, p_category varchar(20), p_status varchar(30));```
- ```create table footwear(fid varchar(20) primary key, f_price int, f_category varchar(20), f_status varchar(30));```
- ```create table jewellery(jid varchar(20) primary key, j_price int, j_category varchar(20), j_status varchar(30));```
  
>Usecase / run:

```  
if you want to run the code you will need to run : main.py
```

- If you have followed all the steps correctly as soon as you run ```main.py``` the UI will popup.

- for any queries reach out to me on the below mentioned social media accounts:
- Instagram: _prashil_1712__(Prashil Jatakiya)
- Linkedin: Prashil Jatakiya
