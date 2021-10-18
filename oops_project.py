from tkinter import *
import random
root =  Tk()

root.geometry("1000x1000")
root.title("Restaurant Management System")
frame1= Frame(root,borderwidth=8,padx=10,pady=20, relief=SUNKEN, bg="violet")
frame1.grid(row=0,column=5)
label=Label(frame1, text="Welcome to Hotel Taj",font="Algerian 30", fg="red")
label.pack(side=TOP)

photo = PhotoImage(file="taj2.png")
vedang_label = Label(image=photo)
vedang_label.grid(row=0,column=7)

user = Label(root, text="Name",font="Algerian 16",anchor=W)
people = Label(root, text="No. of people",font="Algerian 16",anchor=W)

user.grid(row=1,padx=12,pady=20)
people.grid(row=2,padx=12,pady=16)

uservalue = StringVar()
peoplevalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
peopleentry = Entry(root, textvariable = peoplevalue)

userentry.grid(row=1,column=1)
peopleentry.grid(row=2,column=1)

def welcome():
    a=random.randrange(1,6)
    #print("Please proceed to table no.",a,"\n","We hope you have a nice experience!!!!")
    l1=Label(text="Please proceed to table no."+str(a)+"\n"+"\n"+"Click on proceed button below to view menu card"+"\n"+"\n"+"We hope you have a great experience!!!!",font="20")
    l1.grid(padx=20,pady=12,row=4,column=1)
    Button(text="Proceed",padx=20,pady=10,font="20",bg="grey",fg="white").grid(row=5,column=1)

Button(text="Submit", command=welcome,padx=20,pady=10,font="20",bg="grey",fg="white").grid(row=4,column=1)




root.mainloop()