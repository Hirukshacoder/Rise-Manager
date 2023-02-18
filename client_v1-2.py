


from tkinter import *
from tkinter import messagebox
import sqlite3 
import os
import customtkinter 
import hashlib 

from PIL import Image 

class app:
        def new_password():
            global new_passwords
            customtkinter.set_appearance_mode("System")
            customtkinter.set_default_color_theme("blue")

            new = customtkinter.CTk()
            new.title("New Password")
            new.geometry("327x527")
            new.resizable(False, False)
            label = customtkinter.CTkLabel(new, text="New Password", font=("Rubik", 26, "bold"))
            label.place(x=50, y=50)

            new_passwords = customtkinter.CTkEntry(new, width=250, border_width=0, font=("Regular", 10))

            def enter(e):
                new_passwords.delete(-1, "end")


            def leave(e):
                new_password0 = new_passwords.get()
                if new_password0 == "":
                    new_passwords.insert(-1, "New Password")

            new_passwords.insert(-1, "New Password")
            new_passwords.bind("<FocusIn>", enter)
            new_passwords.bind("<FocusOut>", leave)
            new_passwords.place(x=30, y=150)

            def save():
                connection = sqlite3.connect("list.db", timeout=10)
                cursor = connection.cursor()

                cursor.execute("""
                CREATE TABLE IF NOT EXISTS list (
                id INTEGER PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                new_password VARCHAR(255) NOT NULL
                )
                """)
                new_passwordx = new_passwords.get()
                cursor.execute("INSERT INTO list (username, new_password) VALUES (?,?)", (user, new_passwordx))
                print("Added to database successfully ]- updated")

                messagebox.showinfo("Success", "Saved password")

                print(user)
                print(new_passwordx)
                connection.commit()

            save_password = customtkinter.CTkButton(new, width=250, text="Save", border_width=0, command=save)
            save_password.place(x=30, y=210)

            new.mainloop()

        def view_password():
            connection = sqlite3.connect("list.db", timeout=10)
            cursor = connection.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS list (
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            new_password VARCHAR(255) NOT NULL
            )
            """)

            new = customtkinter.CTk()
            customtkinter.set_appearance_mode("System")
            customtkinter.set_default_color_theme("blue")
            new.title("View Password")
            new.geometry("327x527")
            label = customtkinter.CTkLabel(new, text="View Password", font=("Rubik", 26, "bold"))
            label.place(x=30, y=50)

            def View():
                    sql = '''SELECT new_password FROM list WHERE username=?'''
                    cursor.execute(sql, (user,))
                    result = cursor.fetchall()
                    print(result)
                    print(user)
                    print("")

                    label2 = customtkinter.CTkLabel(new, text=f"{result}", font=("Rubik", 15))
                    label2.place(x=30, y=280)

            view_password = customtkinter.CTkButton(new, width=250, text="View", border_width=0, command=View)
            view_password.place(x=30, y=210)
            new.mainloop()

        def delete_password():
            global delete_passwords
            new = Tk()
            new.title("Delete Password")
            new.configure(bg="#fff")
            new.geometry("327x527")
            label = customtkinter.CTkLabel(new, text="Delete Password", font=("Rubik", 24, "bold"))
            label.place(x=30, y=50)

            delete_passwords = customtkinter.CTkEntry(new, width=50, border_width=0, font=("Regular", 10))

            def enter(e):
                delete_passwords.delete(-1, "end")


            def leave(e):
                delete_password0 = delete_passwords.get()
                if delete_password0 == "":
                    delete_passwords.insert(-1, "Delete Password")

            delete_passwords.insert(-1, "Delete Password")
            delete_passwords.bind("<FocusIn>", enter)
            delete_passwords.bind("<FocusOut>", leave)
            delete_passwords.place(x=30, y=150)

            customtkinter.CTkFrame(new, width=250, height=2).place(x=30, y=165)


            def delete():
                connection = sqlite3.connect("list.db", timeout=10)
                cursor = connection.cursor()
                delete_passwordx = delete_passwords.get()
                sql = '''DELETE delete_passwordx FROM list WHERE new_password=?'''
                cursor.execute(sql, (new_passwords.get(),))

            delete_password = customtkinter.CTkButton(new, width=35, pady=7, text="Delete", border_width=0, command=delete)
            delete_password.place(x=30, y=210)
            new.mainloop()

        def app():
            new = customtkinter.CTkToplevel()
            customtkinter.set_appearance_mode("System")
            customtkinter.set_default_color_theme("blue")

            new.title("R-Manager")
            new.geometry("423x559")
            new.resizable(False, False)

            def change_appearance_mode_event(new_appearance_mode):
                customtkinter.set_appearance_mode(new_appearance_mode)

            appearance_mode_menu = customtkinter.CTkOptionMenu(new, values=["Light", "Dark", "System"], command=change_appearance_mode_event)
            appearance_mode_menu.grid(padx=95, pady=100, sticky="s")

            logo_image = customtkinter.CTkImage(Image.open("images/CustomTkinter_logo_single.png"), size=(30, 30))
            label = customtkinter.CTkLabel(new, text="  Dashboard", image=logo_image, compound="left", font=customtkinter.CTkFont(size=40, weight="bold"))
            label.place(x=90, y=5)

            new_password1 = customtkinter.CTkButton(new, width=50, text="New Password", border_width=0, command=app.new_password)
            new_password1.place(x=95, y=150)

            view_password1 = customtkinter.CTkButton(new, width=50, text="View Password", border_width=0, command=app.view_password)
            view_password1.place(x=95, y=200)

            new.mainloop()

        def client():
            def login():
                global user 
                done = False 
                connection = sqlite3.connect("database_mine.db", timeout=10)
                cursor = connection.cursor()

                user = username.get()
                print(user)

                pass_word = password.get()
                print(pass_word)

                if user == "":
                    messagebox.showerror("Error","Enter an username")
                        
                elif pass_word == "":
                    messagebox.showerror("Error","Enter a password")

                encode = pass_word.encode()
                hash_password = hashlib.sha256(encode).hexdigest()

                cursor.execute("SELECT * FROM database_mine WHERE username = ? AND password = ?", (user, hash_password))

                if cursor.fetchall():
                    print("Successfully logged in as", user)
                    win.quit()
                    app.app()

                else:
                    print("Incorrect username or password")
                    messagebox.showerror("Error", "Incorrect username or password")
                    
                    
            win = customtkinter.CTk()
            win.title("R-Manager Login")

            win.geometry("923x559")
            win.configure(bg="#fff")
            win.resizable(False,False)

            my_image = customtkinter.CTkImage(dark_image=Image.open("images/CustomTkinter_logo_single.png"), size=(350, 350))
            img = customtkinter.CTkLabel(win, image=my_image, text="")
            img.place(x=45, y=95)
            
            box = customtkinter.CTkFrame(win, width=350, height=350)
            box.place(x=480,y=70)
            

            title = customtkinter.CTkLabel(box,text="Login", font=("Regular",28,"bold"))
            title.place(x=115, y=5)

            def enter(e):
                username.delete(-1, "end")

            def leave(e):
                users = username.get()
                if users == "":
                    username.insert(-1, "Username")

            username = customtkinter.CTkEntry(box, width=300, border_width=0, font=("Regular",10))
            username.insert(-1, "Username")
            username.bind("<FocusIn>", enter)
            username.bind("<FocusOut>", leave)

            username.place(x=30, y=90)

            password = customtkinter.CTkEntry(box, width=300, border_width=0, font=("Regular",10))

            def enter(e):
                password.delete(-1, "end")

            def leave(e):
                passwords = password.get()
                if passwords == "":
                        passwords.insert(-1, "Passwords")


            password.insert(-1, "Password")
            password.bind("<FocusIn>", enter)
            password.bind("<FocusOut>", leave)
            password.place(x=30, y=150)

            login_button = customtkinter.CTkButton(box, width=300, text="Log In", border_width=0, command=login)
            login_button.place(x=30, y=205)


            win.mainloop()


app.client()