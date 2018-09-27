# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana",
 "Girl", "Boy"]

# 试着用for循环写一遍
i = len(stuff)

for i in range(i, 10): # (i, 10)include i, exclude 10
    # print(i) # 检测i的值
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There are %d items now."%(i+1))
    # print(f"There are {i + 1} items now.")
    # {i + 1} : position and order(position + 1)
    i += 1
    # print(i) # Debug i

'''
while len(stuff) != 10: # while loop
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
'''

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
