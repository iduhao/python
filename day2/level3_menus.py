# Author:Alex Du

city = {
    '北京': {
        "海淀": {
            "中关村": ["Microsoft", "sina"],
            "上地": ["baidu", "lenovo"],
        },
        "朝阳": {
            "望京": ["SOHO", "绿地"],
            "国贸": ["CCTV", "国贸"],
            "朝阳门": ["Fesco", "外交部"],
        },
    },
    '山东': {
        "济南": {},
        "青岛": {},
    },
    '山西': {
        "太原": {},
        "吕梁": {},
    },
}

while True:
    for level1 in city:
        print(level1)
    choice1 = input("选择进入第二层>>:")
    if choice1 in city:
        while True:
            for level2 in city[choice1]:
                print("\t", level2)
            choice2 = input("选择进入第三层>>:")
            if choice2 in city[choice1]:
                while True:
                    for level3 in city[choice1][choice2]:
                        print("\t", level3)
                    choice3 = input("选择进入第四层>>:")
                    if choice3 in city[choice1][choice2]:
                        while True:
                            for level4 in city[choice1][choice2][choice3]:
                                print("\t", level4)
                            choice4 = input("最后一层，按q退出!!!")
                            if choice4 == "q":
                                exit()
                    if choice3 == "q":
                    exit()
            if choice2 == "q":
                    exit()
    elif choice1 == "q":
        exit()
    else:
        print("输入不正确")
