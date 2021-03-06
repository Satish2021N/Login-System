from tkinter import*
from PIL import Image,ImageTk

root = Tk()
root.title("Registration Form")
root.geometry("1366x768")
root.config(bg="white")
root.iconbitmap('favicon.ico')

def get_data():
    first_name = firstname.get()
    last_name = lastname.get()
    email_address = eaddress.get()
    contact_address = contact.get()
    print(first_name)
    print(last_name)
    print(email_address)
    print(contact_address)

    file = open("user.txt","w")
    file.write(first_name)
    file.write(last_name)
    file.write(email_address)
    file.write(contact_address)
    file.close()
    print("User info has been registered successfully")


'''Background Image'''
background= ImageTk.PhotoImage(file="Background.jpg")
label=Label(root, image=background).place(relwidth=1, relheight=1)

'''Title'''
title =Label(root, text="REGISTER HERE", font=("Comic Sans MS", 20, "bold"), bg="white", fg="Black").place(x=180, y=90)

'''Widgets'''

firstname = StringVar()
f_name = Label(root,text="First Name", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 160)
txt_fname =Entry(root, font=("Comic Sans MS", 11),bg="#FBFCFC",textvariable=firstname).place(x=220,y=165, width=250)

lastname=StringVar()
l_name = Label(root, text="Last Name", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 220)
txt_lname =Entry(root, font=("Comic Sans MS", 11), bg="#FBFCFC", textvariable=lastname) .place(x=220,y=225, width=250)

eaddress=StringVar()
e_address = Label(root, text="Email Address", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 280)
txt_email =Entry(root, font=("Comic Sans MS", 11), bg="#FBFCFC", textvariable=eaddress) .place(x=220,y=285, width=250)

contact=StringVar()
c_contact = Label(root, text="Contact No.", font=("Comic Sans MS", 13,"bold"), bg="white", fg="Black").place(x=80, y = 340)
txt_contact =Entry(root, font=("Comic Sans MS", 11),  bg="#FBFCFC", textvariable=contact) .place(x=220,y=345, width=250)

chk = Checkbutton(root, text="I agree to the terms and conditions", font=("Comic Sans MS",11), bg="white") .place(x=150,y=400)
btn_register = Button(root, text="REGISTER", font=("Comic Sans MS",13),bd=0,cursor="hand2", command=get_data,bg="#0b9663", fg="white") .place(x=240, y=450, width=150)


root.mainloop()