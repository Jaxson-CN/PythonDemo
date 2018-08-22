# !/usr/bin/env python
# -*- coding: UTF-8 -*-

types_of_people = 10 # 定义10类人
x = f"There are {types_of_people} types of people." #　把10类人放入x中

binary = "binary" # binary
do_not = "don't" # don't
y = f"Those who know {binary} and those who {do_not}." # 把binary和don't放入y中

print(x) # 输出x
print(y) # 输出y

print(f"I said: {x}") # 把x放入另一字符串中
print(f"I also said: '{y}'") # 把y放入另一字符串中

hilarious = True # hilarious = False # hilarious(可笑的)是False
joke_evaluation = "Isn't that joke so fanny?! {}" # 字符串joke_evaluation

print(joke_evaluation.format(hilarious)) # 输出joke_evaluation，正则表达式？

w = "This is the left side of..." # 字符串w
e = "a string with a right side." # 字符串e

print(w + e) # 输入w + e 