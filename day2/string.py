# Author:Alex Du
# 字符串方法的使用
name = "our country caption is {city}"
print(name.capitalize())  # 首字母大写
print(name.count("i"))  # 统计字符串中该元素出现的次数
print(name.center(50, "-"))  # 将字符串居中显示
print(name.endswith("ng"))  # 判断字符串是否以某一元素结尾
print(name.expandtabs(tabsize=50))  # 将一个tab键转成多少空格
print(name.find("c"))  # 找到字符串中某一元素的第一次出现的位置
print(name[name.find("c"):])  # 进行切片
print(name.format(city='beijing'))  # 格式化输出
print(name.isalnum())  # 判断是不是包含阿拉伯数字和字母，不包括特殊符号
print("dad".isalpha())  # 是不是包含大小写字母
print("abc".isidentifier())  # 是不是合法的标识符（比如变量名）
print(name.join("==="))  # 将字符串以定义的符号拼接起来
print(name.ljust(50, '='))  # 保证字符串有指定长度，如果不够用指定字符填充在右边
print(name.rjust(50, '='))  # 保证字符串有指定长度，如果不够用指定字符填充在左边
print("NaMe".lower())  # 将大写转成小写
print("NaMe".upper())  # 将小写转成大写
print("  \nalex\n".lstrip())  # 去掉边的空格和回车
print("  \nalex\n".rstrip())  # 去掉右边的空格和回车
print("beijing".replace('b', 'B'))  # 将新的字符替换旧的字符
# split将字符串按指定方式生产列表
print(name.split())
print("1+2+3+4+5".split('+'))
print("NaMe Is beijing".swapcase())  # 将大写转成小写，小写转成大写

# --------------同样也支持中文-------------------------------------------
country = "我们的祖国是中国"
print(country)
print(country.count("国"))
print(country[country.find("祖"):])
print(country.find("中"))

