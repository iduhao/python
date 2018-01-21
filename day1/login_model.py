# Author:Alex Du
#!/usr/bin/env python
#import  getpass
user = input("Please set your username:")
# pwd = getpass.getpass("Please set your password:") pycharm不能使用getpass模块
pwd = input("Please set your password:")
print("Your username is:", user + ",Your password is:", pwd)
for i in range(3):
    in_name = input("Please input your username:")
    # in_pwd = getpass.getpass("Please input your password:") 如果其他环境可以使用getpass隐藏秘密输入
    in_pwd = input("Please input your password:")
    if in_name == user and in_pwd == pwd:
        print("Welcome"+in_name+"login!!!")
        break
    elif in_name != user:
        print("username error")
    elif in_pwd != pwd:
        print("password error")
print("user is locked!!!")

