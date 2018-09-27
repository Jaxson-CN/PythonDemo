# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 

"""
i = 0
numbers = [] # 定义空列表numbers

# while循环，循环条件是i < 6
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i) # 把当前的i的值添加到numbers列表中

    i += 1 # i值递加
    print("Numbers now: ", numbers) # 输出当前列表的全部元素
    print(f"At the bottom i is {i}") # 输出当前i的取值


print("The numbers: ") # 当i的取值等于6时，跳出while循环，开始执行此行命令

# for循环，遍历列表中全部的元素
for num in numbers:
    print(num)
"""
def list(a, b):
    i = 0
    numbers = []

    while i < a:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += b
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

print("这是一个用函数写的while循环测试：")
a = int(input("请输入列表最大值> "))
b = int(input("请输入列表中相邻两个数的值> "))

list(a, b)