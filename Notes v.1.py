from tkinter import*
import os


def register():
    global screen1

    screen1 = Toplevel(root)
    screen1.title("Register")
    screen1.geometry("300x250")
  
    global username
    global password
    global username_entry
    global password_entry
    
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text= "Username *").pack()
    username_entry= Entry(screen1, textvariable= username)
    username_entry.pack()
    Label(screen1, text= "Password *").pack()
    password_entry = Entry(screen1, textvariable= password, show= "*")
    password_entry.pack()
    Label(screen1, text= "").pack()
    button_register= Button(screen1, text= ("Register"), padx= 10, pady = 1, command= register_user).pack()
   
    screen1.mainloop()

def register_user():

    global label_reg
    db = open("user_info.txt", "a")

    username_info= username.get()
    password_info= password.get()

    db = open("user_info.txt", "r")
    if username_info in db.readline():
       return Label(register, text= "Username alreasy exist").pack()
    
    if len(password_info) < 8:
        return Label(register, text= "Password should be 8 Characters")


    db = open("user_info.txt", "a")
    data = f"{username_info} {password_info} ,\n"
    db.write(data)
    db.close()
    
    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1, text= "Registration successfully", fg= "green", font= ("calabri" , 11)).pack()

def delete2():
    screen3.destroy()

def saved():
    screen5 = Toplevel(root)
    screen5.title("Saved")
    screen5.geometry("100x100")
    Label(screen5, text= "Saved").pack()

def save():
    filename = raw_filename.get()
    notes = raw_notes.get()
    
    data = open(filename , "w")
    data.write(notes)
    data.close()
    saved()

def create_notes():
    global screen4
    global raw_filename
    global raw_notes
    raw_filename = StringVar()
    raw_notes = StringVar()

    screen4 = Toplevel(root)
    screen4.title("info")
    screen4.geometry("300x250")
    Label(screen4, text= "Please name the file below:").pack()
    Label(screen4, text="").pack()
    Entry(screen4, textvariable = raw_filename).pack()
    Label(screen4, text="").pack()
    Label(screen4, text= "please enter the Notes bellow:").pack()
    Label(screen4, text="").pack()
    Entry(screen4, textvariable= raw_notes).pack()
    Label(screen4, text="").pack()    
    Button(screen4, text= "Save", padx= 20, pady= 5, command= save).pack()

def view_notes1():
    filename1 = raw_filename1.get()
    data = open(filename1 , "r")
    data1 = data.read()
    screen6 = Toplevel(root)
    screen6.title("Notes")
    screen6.geometry("400x400")
    Label(screen6, text = data1).pack()
    data.close()

def view_notes():
    #print("Coming soon....")
    screen5 = Toplevel(root)
    screen5.title("info")
    screen5.geometry("250x250")
    all_files = os.listdir()
    Label(screen5, text = "Please use one of the files").pack()
    Label(screen5, text="").pack()
    Label(screen5, text = all_files).pack()
    global raw_filename1
    raw_filename1 = StringVar()
    Entry(screen5, textvariable= raw_filename1).pack()
    Button(screen5, text= "View Note", command= view_notes1).pack()

def delete_note1():
    filename2 = raw_filename2.get()
    os.remove(filename2)
    screen7 = Toplevel(root)
    screen7.title("Notes")
    screen7.geometry("400x400")
    Label(screen7, text = "Note Deleted successfully").pack()

def delete_notes():
   # print("Coming soon....")
    screen8 = Toplevel(root)
    screen8.title("info")
    screen8.geometry("250x250")
    all_files = os.listdir()
    Label(screen8, text = "Please use one of the files").pack()
    Label(screen8, text="").pack()
    Label(screen8, text = all_files).pack()
    global raw_filename2
    raw_filename2 = StringVar()
    Entry(screen8, textvariable= raw_filename2).pack()
    Button(screen8, text= "Delete", command= delete_note1).pack()

def session():
    screen4 = Toplevel(root)
    screen4.title("dashboard")
    screen4.geometry("400x400")
    Label(screen4, text= "Welcome to Dashboard", font= ("Times new romen", 16)).pack()
    Label(screen4, text="").pack()
    Button(screen4, text= "Create Note", padx = 20, pady= 5, command= create_notes).pack()
    Label(screen4, text="").pack()
    Button(screen4, text= "view Note", padx = 20, pady= 5, command= view_notes).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Delete", padx = 20, pady= 5, command= delete_notes).pack()

def login_success():
    session()

def user_not():
    global screen3
    screen3 = Toplevel(root)
    screen3.title("Password not recoganised")
    screen3.geometry("150x100")
    Label(screen3, text="User not found", fg="red").pack()
    Label(screen3, text="").pack()
    Button(screen3, text="OK",padx=10, pady=5, command= delete2).pack()


def login_verify():
    username_entry = username_entry1.get()
    password_entry = password_entry1.get()
    db = open("user_info.txt", "r")
    for line in db.readlines():
        line = line.split(",")
        line = line[0].split(" ")
        username1 = line[0]
        password1 = line[1]
        if username1 == username_entry:
            if password1 == password_entry:
                login_success()
    return user_not()

def login():
    #Label(root, text= ("Coming soon")).pack()
    global screen2
    screen2= Toplevel(root)
    screen2.title ("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "please enter details below to login").pack()
    Label(screen2, text = "").pack()

    global username_entry1
    global password_entry1

    password_entry1 = StringVar()

    Label(screen2, text = "Username").pack()
    username_entry1 = Entry(screen2)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password").pack()
    password_entry1 = Entry(screen2, show= "*")
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button (screen2, text= "Login" , padx=20, pady=10,command= login_verify).pack()
 
def main_screen():
    global root
    root = Tk()
    root.title("Notes V1.0")
    root.geometry("300x250")

    button_login= Button(root, text=("Login"), width=("30"), height = ("2"), command= login)
    button_Regester= Button(root, text=("Register"), width=("30"), height = ("2"), command= register)

    Label(text= ("Notes"), bg= ("grey") , fg= ("black") , width = ("300"), height = ("2"), font = ("calabri", 13)).pack()
    Label(text = "").pack()
    button_login.pack()
    Label(text = "").pack()
    button_Regester.pack()
    Label(text = "").pack()
    button_Exit = Button(root, text=("Exit"), padx= 20 , pady= 10,borderwidth=5 , command=root.quit)
    button_Exit.pack()

    root.mainloop()
main_screen()