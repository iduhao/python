# Author:Alex Du

# dictionary（字典）是一种key-value的数据类型.无序，没有下标.通过key进行查找

info = {
    'student001': "zhang san",
    'student002': "li si",
    'student003': "wang mazi",
}

print(info)
print(info["student002"])  # 直接查找，如果不存在可能导致错误，最好使用get
print(info.get("student003"))  # 不能保证key存在，即使用该方法，如果不存在返回none而不是报错
print('student002' in info)  # 判断某一个key在不在字典中，返回true或者false
info["student003"] = "王麻子"  # 直接修改即可，如果不存在，即添加
info["student004"] = "赵老爷"
# del info  # 删除字典
# 删除key
# del info["student004"]
# info.pop("student003")
print(info)
#  ================字典嵌套=======================================

