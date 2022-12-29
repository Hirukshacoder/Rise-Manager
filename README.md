
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



### ~ signup.py ~

* A signup system that adds your username and the hashed password to 'database_mine.db'.

* R-Manager has a secured signup system.

* Your passwords are hashed and then add to the database.


## Ngrok - configuration

* Ngrok is a bit buggy on `client_v1-0.py`

* It works only on `client_v1-1.py`

### Config ngrok

* Install [ngrok](https://ngrok.com/)

* Go to the extracted ngrok directory and save your auth token

* Run `./ngrok tcp 9999`

* Type `localhost` to the `host` variable in `server.py`

* Get the `ip` and `port` from the ngrok connection in terminal

* Paste the `ip` and `port` to the `client_v1-1.py` as shown below

```python
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("0.tcp.in.ngrok.io", 11441))
```

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

- [@Treveen](https://github.com/Hirukshacoder)

<a href="https://www.buymeacoffee.com/thborg"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=thborg&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>

# Thank you!
