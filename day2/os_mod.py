# Author:Alex Du

import os

sys_res = os.system("dir")          #直接就执行命令了，赋值变量并没有保存效果
print('-----', sys_res)             #输出命令的状态码
popen_res = os.popen("dir").read()  #可以通过read读取到popen命令执行的结果赋值给变量输出
print('----->', popen_res)
os.mkdir("../day3")                    #当前路径下创建一个新目录
