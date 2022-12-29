import socket
from sys import exit
import subprocess
import sqlite3 
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("0.tcp.in.ngrok.io", 11441))

def new_password(username, new_password):
    connection = sqlite3.connect("list.db", timeout=10)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS list (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    new_password VARCHAR(255) NOT NULL
    )
    """)

    cursor.execute("INSERT INTO list (username, new_password) VALUES (?,?)", (username, new_password))
    print("Added to database successfully ]- updated")
    connection.commit()


def view_password(username):
        connection = sqlite3.connect("list.db", timeout=10)
        cursor = connection.cursor()
        subprocess.run("cls", shell=True)
        print(" ~ View passwords ~")
        print("")
        sql = '''SELECT new_password FROM list WHERE username=?'''
        cursor.execute(sql, (username,))
        result = cursor.fetchall()
        print(result)
        print("")

def delete_password(username, password):
    connection = sqlite3.connect("list.db", timeout=10)
    cursor = connection.cursor()
    print("~ Delete passwords ~")
    print("")
    sql = '''SELECT new_password FROM list WHERE username=?'''
    cursor.execute(sql, (username,))
    result = cursor.fetchall()
    print(result)

    option = input("Enter password you want to delete: ")
    cursor.execute('''DELETE FROM list option''')

        



message1 = client.recv(1024).decode()
message3 = input(message1)
client.send(str(message3).encode())
message2 = client.recv(1024).decode()
message4 = client.send(input(message2).encode())
client.send(str(message4).encode())
login = (client.recv(1024).decode())

print(login)

if login == f"Logged in as {message3}":
            print("Success")
            def manager():
                    exit = False 
                    while not exit:
                        print("""
                        [ * - * - * - * - * - * - * - *  ]
                        [                                ]
                        [    ~ Manager Dashboard ~       ]
                        [                                ]
                        [    > [1] - New password        ]
                        [    > [2] - View passwords      ] 
                        [                                ]
                        [ * - * - * - * - * - * - * - *  ]
                        """)
                        username = input("Enter your username to verify: ")
                        option = input("Option: ")

                        if option == "1":
                            print("~ New password ~")
                            print("")
                            saves = int(input("How many passwords do you want to save: "))
                            for x in range(saves):
                                new_passwords = str(input("Enter a new password: "))
                                new_password(username=username, new_password=new_passwords)
                            subprocess.run('cls', shell=True)

                        elif option == "2":
                            view_password(username=username)
                            option = input("[1]- Go back: ")
                            if option == "1":
                                manager()
                            else:
                                exit = True 
                                subprocess.run('cls', shell=True)
                                print("Exitted program")

                        else:
                            exit = True 
                            subprocess.run('cls', shell=True)

                
            manager()
else:
    print("Login bad gateway")
