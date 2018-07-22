# Author:Alex Du

# budget = int(input("Please input your budget:"))

product_list= [
    ('Iphone X', '8588'),
    ('MacbookPro', '14588'),
    ('Imac', '14788'),
    ('AppleWatch', '2588')
]
budget = input("Please input your budget:(press 'q' to exit)")
shopping_list = []   # 定义一个空的列表存放用户选择的商品

if budget.isdigit():  # 判断如果是数字，则将其转成int类型
    budget = int(budget)
    while True:
        for index, item in enumerate(product_list):  # enumerate输出列表中各个项目的下标索引和项目本身的值
            print(index, item)
        # 定义用户选择的变量
        choose = input("Please input product code>>>(press 'q' to exit)")
        if choose.isdigit():  # 判断输入是否是合法的数字代码，如果是转换成int类型，如果不是输入错误
            choose = int(choose)
            if 0 <= choose < len(product_list):
            #  if choose < len(product_list) and choose >= 0: 操作可以简化成上面的，同样的效果
                # print(len(product_list))

                choose_item = product_list[choose]
                product_item = int(choose_item[1])
                if product_item <= budget:  # 买的起
                    shopping_list.append(choose_item)
                    budget -= product_item
                    print(shopping_list)
                    print("Added %s into your shopping car, your current balance is \033[31;1m%s\033[0m" %(product_item, budget))
                else:
                    print("\033[41;1m Your balance is %s\033[0m" %(budget))
            else:
                print("product code [%s] is not exist!!!" %(choose))
        elif choose == 'q':
            print("-------shopping-list-------")
            for p in shopping_list:
                print(p)
            print("------Your current balance is\033[31;1m%s\033[0m----------" %(budget))
            exit()
        else:
            print("Warning!!!Invalid input")
elif budget =="q":
    exit()
else:
    print("Warning!!!Invalid input")


