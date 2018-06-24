# Author:Alex Du



#budget = int(input("Please input your budget:"))

budget = input("Please input your budget:")
product_list= [
    ['Iphone X', '8588'],
    ['MacbookPro', '14588'],
    ['Imac', '14788'],
    ['AppleWatch', '2588']
]
shopping_list=[]   # 定义一个空的列表存放用户选择的商品

if budget.isdigit():
    budget = int(budget)
    while True:
        for index, item in enumerate (product_list):
            print(index, item)

        choose = input("Please input product code>>>")
        if choose.isdigit():
            choose = int(choose)
            if choose < len(product_list) and choose >= 0:
                # print(len(product_list))
                choose_item = product_list[choose]
                if choose_item[1] <= budget:  # 买得起
                    shopping_list.append(choose_item)
                    budget -= choose_item[1]
                    print(shopping_list)
                    print("Added %s into your shopping car, your current balance is \033[31;1m%s\033[0m" %(choose_item, budget))
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
else:
    print("Warning!!!Invalid input")


