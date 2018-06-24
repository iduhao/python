# Author:Alex Du
# tuple （元组的使用方法）
# 元组一旦创建，内容不可改变，所以又叫只读列表,只有count和index两个属性

tuple = ("alex", "19", "19", "25")
print(tuple.count("19"))  # 查找某一个选项在列表中出现的次数
print(tuple.index("25"))  # 查找某一个选项的索引值
print(tuple)
