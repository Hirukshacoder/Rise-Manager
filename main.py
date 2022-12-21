import hashlib 
import sqlite3

connection = sqlite3.connect("database_mine.db", timeout=10)
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS database_mine (
id INTEGER PRIMARY KEY,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL
)
""")


username = input("Enter a username: ")
password = input("Enter a password: ")
username1, password1 = "Treveen", hashlib.sha256("123".encode()).hexdigest()
username2, password2 = "John", hashlib.sha256("lovehacking".encode()).hexdigest()
username3, password3 = "Harold", hashlib.sha256("ipython".encode()).hexdigest()
username4, password4 = username, hashlib.sha256(password.encode()).hexdigest()
cursor.execute("INSERT INTO database_mine (username, password) VALUES (?, ?)", (username1, password1))
cursor.execute("INSERT INTO database_mine (username, password) VALUES (?, ?)", (username2, password2))
cursor.execute("INSERT INTO database_mine (username, password) VALUES (?, ?)", (username3, password3))
cursor.execute("INSERT INTO database_mine (username, password) VALUES (?, ?)", (username4, password4))

connection.commit()