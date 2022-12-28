import socket
import sqlite3
import threading
import hashlib

host = str("<add your ip>")

port = int(9999)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

def control_con(cli):
    cli.send("Enter your username: ".encode())
    username = cli.recv(1024).decode()


    cli.send("Enter your password: ".encode())
    password = cli.recv(1024)

    password = hashlib.sha256(password).hexdigest()
    con_db = sqlite3.connect("database_mine.db")
    cursor = con_db.cursor()

    cursor.execute("SELECT * FROM database_mine WHERE username = ? AND password = ?", (username, password))

    if cursor.fetchall():
        cli.send(f"Logged in as {username}".encode())
        cli.send("You are secured!".encode())
    else:
        cli.send(f"{username} or {password} was incorrect".encode())

while True:
    client, addr = server.accept()
    threading.Thread(target=control_con, args=(client,)).start()
