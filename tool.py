#tool to validate entered data
import travelreservationform
from tkinter import *
import tkinter as tk
import tkinter.messagebox
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def validations(lis1,lis2):
    a = 1
    b = 0
    if lis1[0].isalpha():#checking name
        a = 1
    else:
        tkinter.messagebox.showwarning("Invalid name","Enter valid Data")
        lis2[0].set("")
        b = 2
    if lis1[1].isalpha(): #checking surname
       a = 1
    else:
        tkinter.messagebox.showwarning("Invalid surname","Enter valid Data")
        lis2[1].set("")
        b = 2
    if (re.fullmatch(regex,lis1[2])):#checking mail is valid or not
        a = 1
    else:
        tkinter.messagebox.showwarning("Invalid Email","Enter valid Data")
        lis2[2].set("")
        b = 2
    if lis1[4].isdigit():#checking for person number
        a = 1
    else:
        tkinter.messagebox.showwarning("Invalid Count","Enter valid Data")
        lis2[4].set("")
        b = 2
    if (len(lis1[5]) == 10 and lis1[5].isdigit()):#checking contact is valid or not
        op = re.findall(r"^[789]\d{9}$",lis1[5])
        if(len(op) == 1):
            a = 1
        else:
            tkinter.messagebox.showwarning("Invalid Contact","Enter valid Data")
            lis2[5].set("")
            b = 2
    else:
        tkinter.messagebox.showwarning("Invalid Contact","Enter valid Data")
        lis2[5].set("")
        b = 2
    if(a == 1 and b == 0):
        #file operations
        file = open("agentinfo.txt", "a")
        file.write(lis1[0]+'$')
        file.write(lis1[1]+'$')
        file.write(lis1[2]+'$')
        file.write(lis1[3]+"$")
        file.write(lis1[4]+'$')
        file.write(lis1[5]+'$')
        file.write(lis1[6]+"$")
        file.write(lis1[7]+"\n")
        print("Data stored successfully...")
        lis2[0].set("")
        lis2[1].set("")
        lis2[2].set("")
        lis2[3].set("Mahabaleshwar")
        lis2[4].set("")
        lis2[5].set("")
        lis2[6].set("")
        lis2[7].set(False)
        file.close()
