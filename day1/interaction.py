# Author:Alex Du
Name = input("Name:")
Age = input("Age:")
Job = input("Job:")
Salary = input("Salary:")
# 使用+来进行字符串拼接格式化输出，不推荐
"""info = '''
-------------- info of '''+ Name +''' --------------------
Name:'''+ Name + '''
Age: '''+ Age + '''
Job:''' + Job + '''
Salary:''' + Salary"""

# 使用%s来进行格式化输出

"""info = '''
# s代表的是字符串，如果是d，则代表整数，
-------------- info of %s---------------------------
Name:%s
Age:%s
Job:%s
Salary:%s
'''% (Name,Name,Age,Job,Salary)"""

# 使用参数传递进行格式化输出 推荐使用此方法
info = '''
------------ info of {_Name}---------------------
Name:{_Name}
Age:{_Age}
Job:{_Job}
Salary:{_Salary}
'''.format(_Name=Name,_Age=Age,_Job=Job,_Salary=Salary)

# 使用数字编号进行格式化输出
"""info = '''
-------------info of {0}-------------------------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
''' .format(Name,Age,Job,Salary)"""
print (info)


