import sqlite3
import os
import time


if os.path.exists("data.db"):
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
else:
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute(" CREATE TABLE accounts(uname text, pwd text) ")


accOrLog = input("1. Login\n2. Signup\n3. Exit\n\n--> ")

if accOrLog == "2":
    uname = input("Enter Username : ")
    upass = input("Password : ")
    upass2 = input("Conform Password : ")

    if upass == upass2:
        cur.execute(f" INSERT INTO accounts VALUES(?,?) ", [uname, upass])
        print("Account Successfully Created")
        conn.commit()
        time.sleep(2)
        os.system("cls")
    else:
        print("Error")

elif accOrLog == "1":
    uname = input("Enter Username : ")
    pwd = input("Enter Password : ")

    cur.execute(" SELECT * FROM accounts WHERE uname=? AND pwd=?", [uname, pwd])

    if cur.fetchone()==None:
        print("Wrong Details")
    else:
        print("Welcome")

elif accOrLog=="3":
    exit()
else:
    print("Please Select Right Option...")

