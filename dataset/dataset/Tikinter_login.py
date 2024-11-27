from tkinter import *
from functools import partial
from Tikinter_home import launchapp

##def validateLoginfunc(username, password):
##    print(username)
##    if (username == "admin" and password == "admin"):
##        partial(launchapp)
##
##
### Window
##tkWindow = Tk()  
##tkWindow.geometry('500x350')  
##tkWindow.title('Home Security system')
##
### Username label and text entry box
##usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
##username = StringVar()
##usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  
##
### Password label and password entry box
##passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
##password = StringVar()
##passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  
##
##validateLogin = partial(validateLoginfunc, username, password)
##
##
### Login button
##loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  
##
##tkWindow.mainloop()

import tkinter as tk
from tkinter import messagebox

# Function to validate the login
def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    # You can add your own validation logic here
    if userid == "admin" and password == "password":
        launchapp()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
parent = tk.Tk()
parent.title("Login Form")
parent.geometry('500x350')  
parent.title('Home Security system')

# Create and place the username label and entry
username_label = tk.Label(parent, text="Userid:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()

# Create and place the password label and entry
password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
parent.mainloop()
