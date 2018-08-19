# Author:Alex Du
# 列表操作
provinces = [
    "北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江", "上海", "江苏", "浙江",
    "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "广西", "海南", "重庆", "四川",
    "贵州", "云南", "西藏", "陕西", "甘肃", "青海", "宁夏", "新疆", "香港",
]

# 列表的切片操作
print(provinces)  # 输出全部列表内容
print(provinces[0])  # 输出第一项内容
print(provinces[0], provinces[1], provinces[2])  # 输出前3项内容
print(provinces[0:3])  # 输出前3项内容
print(provinces[-1])  # 输出倒数第一项内容
print(provinces[-3:-1])  # 输出倒数第二，三项内容
print(provinces[-3:])  # 输出最后三项内容
print(provinces[:3])  # 输出前3项内容
print(provinces[0:-1:2])  # 间隔一个输出一项
print(provinces[::2])  # 省略开头和结尾 简写
print(provinces[::])
print(provinces[:])  # 省略后相当于直接输出，无意义
# 列表项的增删查操作
# provinces.append("香港", "澳门", "台湾")  追加项报错，只能一个一个加,默认追加到最后
provinces.append("香港")
provinces.append("澳门")
provinces.append("台湾")
print(provinces)

provinces.insert(2, "纽约")  # 指定位置追加列表项
print(provinces)
provinces.insert(3, "伦敦")
print(provinces)
provinces[3] = "德国"  # 直接通过索引值修改
print(provinces)

# 删除列表项
provinces.remove("德国")  # remove 方法只能写名称，不能用索引
# provinces.remove[3]
print(provinces)
del provinces[2]  # del 方法删除使用索引值，不能用名称
# del provinces("江苏")
print(provinces)
provinces.pop()  # pop方法默认删除最后一项，通过下标索引指定位置删除
print(provinces)
provinces.pop(4)  # del provinces[2] = provinces.pop[2]
print(provinces)
# 查找列表项
print(provinces.index("广东"))  # 查找某一项的索引值，区分大小写
print(provinces[provinces.index("广东")])  # 通过查找到某一项的索引值，然后再通过索引值输出该项名称
print(provinces.count("香港"))  # 查找某一项的个数
# 其他命令
# provinces.clear()  # 清除列表项
# print(provinces)
provinces.reverse()  # 反转列表顺序
print(provinces)
provinces.sort()  # 对列表进行排序
print(provinces)

nba = [
   "GSW", "OKC", "UTAH", "HOU"
]
provinces.extend(nba)  # 扩展操作，即将另一个列表的项附加到该列表,扩展后原列表仍然存在
print(provinces)
nba.sort()
print(nba)

# copy 将原来列表复制到新列表，只复制列表项，子列表不会复制，修改列表项不会影响复制的 如需完全复制，使用copy模块的deepcopy命令
cba = nba.copy()
print(cba)

# 列表循环
for i in provinces:
    print(i)
# 操作完成删除列表
# del nba
# print(nba)  # 报错，提示列表未定义
