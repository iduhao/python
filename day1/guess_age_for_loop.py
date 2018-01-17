# Author:Alex Du
My_age = 25

for i in range(10):
    Guess_age = int(input("Please guess my age:"))
    if Guess_age == My_age:
        print("Yes,You got it !!!")
        break
    elif Guess_age < My_age:
        print("Yahoo....You can guess a bigger...")
    else:
        print("Em.....You should  think a smaller...")
else:
    print("you have tried too many times..stop it")