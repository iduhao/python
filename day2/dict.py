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
# info.pop("student003")  删除指定key的值
print(info)
#  ================字典嵌套=======================================
nba_start = {
    "gsw": {
        "PG": ["Stephen Curry"],
        "SG": ["Klay Thompson"],
        "SF": ["Kevin Durant"],
        "PF": ["Draymond Green"],
        "C": ["DeMarcus Cousins"]
    },
    "hou": {
        "PG": ["James Harden"],
        "SG": ["Chris Paul"],
        "SF": ["Trevor Ariza"],
        "PF": ["Clint Capela"],
        "C": ["Qi Zhou"]
    },
    "cavs": {
        "PG": ["J.R.Smith"],
        "SG": ["Kyle Korver"],
        "SF": ["LeBron James"],
        "PF": ["Kevin Love"],
        "C": ["Tristan Thompson"]
    },

}
print(nba_start)
nba_start["cavs"]["PF"][0] = "Jeff Green"  # 修改嵌套字典中的键值
print(nba_start)
print(nba_start.values())  # 直接打印字典中的value
print(nba_start.keys())  # 打印字典中的key
nba_start.setdefault("lal", {"PG": ["ball"]},)  # 在字典中取该值，如果有直接输出，如果没有赋新值
nba_start.setdefault("cavs", {"PG": ["ball"]},)  # 如果有就直接输出该值
print(nba_start)
# ===========================================================================================
# update 方法，将两个字典合并，如果有交叉的直接更新替换，如果没有，直接附在后面
# item 方法，把字典转成列表
#  dict.fromkeys()初始化一个字典
