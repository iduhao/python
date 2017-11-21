#!/bin/python
import getpass
Name = "alex"
Password ="123.com"
In_name = input("Username:")
In_password = getpass.getpass("Password:")
if In_name == Name and In_password == Password:
    print("Welcome user {User_name} login ...".format(User_name=In_name))
else:
    print("Invalid Username or Password")
