from tkinter import *
import tkinter as tk
from tkinter import ttk
import tool
import tkinter.messagebox
import re
root = Tk()
root.geometry('700x700')
root.title("Travel Registration form")
root.resizable(False, False)
label_0 = Label(root, text = "Travel Information", width = 20, font=("bold", 20))
label_0.place(x = 90,y = 53)
e1 = tk.StringVar()
e2 = tk.StringVar()
e3 = tk.StringVar()
e4 = tk.StringVar()
e5 = tk.StringVar()
e6 = tk.StringVar()
e7 = tk.StringVar()
e8 = tk.StringVar()
e7.set(False)
clicked = StringVar()

lis1 = []
lis2 = []
def dell():
    mail = input("Enter mail : ")
    with open("agentinfo.txt",'r')as file:
        lines = file.readlines()

    with open("agentinfo.txt",'w') as file:
        for line in lines:
        # find() returns -1 if no match is found
            if line.find(mail) != -1:
                print("Reservation deleted!")
            else:
                file.write(line)
                print("No match found...")
                
    

    
def cli():
    e11 = e1.get()
    e22 = e2.get()
    e33 = e3.get()
    e88 = clicked.get()
    e44 = e4.get()
    e55 = e5.get()
    e66 = e6.get()
    e77 = e7.get()
    lis1 = [e11,e22,e33,e88,e44,e55,e66,e77]
    lis2 = [e1,e2,e3,clicked,e4,e5,e6,e7]
    tool.validations(lis1, lis2)
    
#first name
label_1 = Label(root, text = "First Name*", width = 20, font=("bold", 15))
label_1.place(x = -40, y = 100)
entry_1 = Entry(root, textvariable = e1, width = "30", font=("default", 15))
entry_1.place(x = 180, y = 105)
#last name
label_2 = Label(root, text = "Last Name*", width = 20, font=("bold", 15))
label_2.place(x = -40, y = 150)
entry_2 = Entry(root,textvariable = e2, width = "30", font=("default", 15))
entry_2.place(x = 180, y = 155)

#email
label_3 = Label(root, text = "Email*", width = 20, font=("bold", 15))
label_3.place(x = -50, y = 205)
entry_3 = Entry(root, textvariable = e3,width = "30", font=("default", 15))
entry_3.place(x = 180, y = 205)
#tour pkg
label_4 = Label(root, text = "Tour Package*", width = 20, font=("bold", 15))
label_4.place(x = -40, y = 255)
options = {"Goa", "Mahabaleshwar","Kashmir","Delhi","Karnataka","Kerla","Tamil Nadu"}
clicked.set("Mahabaleshwar")
drop = OptionMenu(root,clicked,*options)
drop.pack()
drop.place(x = 180, y = 255)

#no. of persons
label_5 = Label(root, text = "No. of Persons*", width = 20, font=("bold", 15))
label_5.place(x = -30, y = 305)
entry_4 = Entry(root, textvariable = e4,width = "30", font=("default", 15))
entry_4.place(x = 180, y = 305)

#contact
label_6 = Label(root, text = "Contact*", width = 20, font=("bold", 15))
label_6.place(x = -50, y = 355)
entry_5 = Entry(root, textvariable = e5,width = "30", font=("default", 15))
entry_5.place(x = 180, y = 360)


#discount coupon
label_7 = Label(root, text = "Discount Coupon", width = 20, font=("bold", 15))
label_7.place(x = -30, y = 405)
label_8 = Label(root, text = "(if any)", width = 20, font=("default", 10))
label_8.place(x = -20, y = 430)
entry_5 = Entry(root, textvariable = e6,width = "30", font=("default", 15))
entry_5.place(x = 180, y = 405)

#Terms and condition
label_9 = Label(root, text = "Terms and condition*", width = 20, font=("bold", 15))
label_9.place(x = -10, y = 455)
r1 = Radiobutton(root, text = "I agree", font=("bold",15),padx = 5,  value = 1, variable = e7).place(x = 100, y = 490)
r2 = Radiobutton(root, text = "I Disagree", font=("bold",15), padx = 20, value = 2,variable = e7).place(x = 250, y = 490)
#make reservation
Button(root,text = "Make Reservation",command = cli, width = 20,font=("bold", 15)).place(x = 100, y = 550)
e7.set(1)

#delete reservation
Button(root,text = "Delete Reservation",command = dell, width = 40,font=("bold", 15)).place(x = 100, y = 600)

#View all

def showw():
    lii = []
    li = ['First name','Last name', 'Email', 'Tour_Package','Peraons','Contact','coupon']
    lii.append(li)
    li = []
    file = open("agentinfo.txt","r")
    for line in file:
        for word in line.split("$"):
           li.append(word)
        lii.append(li)
        li = []
    root1 = Tk()
    root1.geometry('1200x500')
    root1.title("Reservation Information")
    root1.resizable(False, False)
    for i in range(len(lii)):
        for j in range(7):
            e = Entry(root1,width = 20,font = ("bold", 10))
            e.grid(row = i, column = j)
            e.insert(0,lii[i][j])   
    root1.lift()
    root1.attributes("-topmost", True)
    #root1.bind("<FocusIn>",handle_focus)
    hwnd = root1.winfo_id()
    root1.mainloop()
    file.close()
    
Button(root,text = "View All",command = showw, width = 20,font=("bold", 15)).place(x = 350, y = 550)
root.mainloop()
