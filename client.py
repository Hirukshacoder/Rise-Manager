import socket
from sys import exit
import subprocess

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("<add your ip>", "<add your port>"))



def manager():
    subprocess.run("cls", shell=True)
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
        subprocess.run('cls', shell=True)
        print("~ New password ~")
        print("")
        saves = int(input("How many passwords do you want to save: "))
        for x in range(saves):
            new_password = input("New password: ")
            passwords = open(f"passwords/{username}_passwords.txt", "a")
            passwords.write(new_password + "\n")
            passwords.close()
        manager()



    if option == "2":
        subprocess.run("cls", shell=True)
        print(" ~ View passwords ~")
        print("")
        passwords = open(f"passwords/{username}_passwords.txt", "r")
        read = passwords.readlines()
        print(read)
        print("")
        print("These are your passwords")
        option = input("option ( [1] - go back ): ")
        if option == "1":
            manager()
        else:
            return "Operation undefined!"



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
    manager()


else:
    print("Login corrupted!")
