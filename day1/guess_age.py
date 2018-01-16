# Author:Alex Du
My_age = 25
count = 1
while count < 3 :
    Guess_age = int(input("Please guess my age:"))
    if Guess_age == My_age:
        print("Yes,You got it !!!")
        break
    elif Guess_age < My_age:
        print("Yahoo....You can guess a bigger...")
    else:
        print("Em.....You should  think a smaller...")
        count = count + 1
else:
    print("you have tried too many times..stop it")