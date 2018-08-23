# !/usr/bin/env python
# -*- coding: UTF-8 -*-

# 定义函数cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanker.\n")
# 每调用一次函数，就输出函数cheese_and_crackers的全部内容

print("We can just give the function numbers directly:")
# 调用函数，并传入实参20， 30
cheese_and_crackers(20, 30)


print("OR, we can ue variables from out script:")
# 同上一次调用，实参形式改变
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# 调用函数，实参用数学运算来代替
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# 调用函数，实参为全局变量 + 数学运算
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("这是用input()来完成的：")
'''
cheese = int(input("请输入cheese的数量>"))
cracker = int(input("请输入cracker的数量>"))
print("这是每一个变量加上1000后的结果：")
cheese_and_crackers(cheese + 1000, cracker + 1000)
'''
cheese = input("请输入cracker的数量>")
cracker = input("请输入cheese的数量>")
print("这应该是一个错误的演示，同样每个变量加上1000：")
cheese_and_crackers(cheese + 1000, cracker + 1000)
