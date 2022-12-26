
![R - (1)](https://user-images.githubusercontent.com/97717488/209555229-be15123d-abc7-42df-aaa6-9f7ea087cb15.png)

# R - Manager 

* A tool to manage all of your paswords in one program / database.

![](https://img.shields.io/badge/TryHackMe-THB-212C42?style=for_the_badge&logo=thb)
![](https://img.shields.io/pypi/l/hashlib?color=yellow&logo=python)
![python](https://img.shields.io/badge/Python-v3.10-3776AB?style=for_the_badge&logo=Python)
![sqlite](https://img.shields.io/badge/Sqlite-v3-003B57?style=for_the_badge&logo=Sqlite)

## Top features

* Two databases for login and managing passwords.
* Online server (can use the manager anywhere)
* Well programmed client
* Retrive passwords easily
* Add passwords easily
## Installation

Install R-Manager with git

```bash
  $ git clone https://github.com/Hirukshacoder/Rise-Manager.git
  $ cd Rise-Manager
  $ python3 server.py 
  $ python3 main.py (signup only)
  $ python3 client.py (login and dashboard)
```
    
## Database Structure 

#### Login and signup database (database_mine.db)


| id        | username | password                |
| :-------- | :------- | :-----------------------|
| 1         | John     | hashed password sha256  |
| 2         | Beckham  | hashed password sha256  |
| 3         | Ann      | hashed password sha256  |

#### Manager database structure (list.db)


| id        | username | password                |
| :-------- | :------- | :-----------------------|
| 1         | John     | password                |
| 2         | Beckham  | password                |
| 3         | Ann      | password                |

## R - Manager Vol-1.0 Documentation

* Made by THB 
* Your free to fork this project.
* server.py - the main server that hosts the application.
* signup.py - create an account.
* client.py - login and dashboard.
* Application can be promoted.

### ~ server.py ~

* The main server that hosts the application in your ip.

* Makesure, to add your ip to server.py and feel free to change the port.

* Does half of the login function: checks if your username and password in database and sends it to client.


### ~ client.py ~

* Receives login details and perform the functions accordignly.

* contains the dashboard.

* saves passwords.

* make passwords viewable.



### ~ main.py ~

* A signup system that adds your username and the hashed password to 'database_mine.db'.

* R-Manager has a secured signup system.

* Your passwords are hashed and then add to the database.




## Examples

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.8.160", 9999)) 
```

```python
import sqlite3 

connect = sqlite3.connect("database.db")
cursor = sqlite3.cursor()

```
```python
def world():
  print("Hello world")
def bye():
  print("bye")
dashboard = """
    [1] - Greet
    [2] - Exit
"""
print(dashboard)
response = input("> ")

if response == "1":
  world()

elif response == "2":
  bye()

else:
  print("Operation undefined")
```
## Contact us

- [📱Telegram](https://t.me/+wrtEUZA9_j8yMjM9)

- [💽 Discord](https://discord.gg/H6P5VEn2)

## Top users

This project is used by the following companies:

- [NMSec](https://t.me/NetflixMoviesus)
- [Elite Predator](https://t.me/+OoLv5gh6DoAwNjUx)
- [Irupcnet](https://t.me/irupc_net)


## Authors

- [@Treveen](https://www.github.com/Hirukshacorder)

# Thank you!
