# !/usr/bin/env python
# -*- coding: UTF-8 -*-

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

my_height = 2.54 * height # 1英寸 = 2.54厘米
my_weight = 0.4536 * weight # 1磅 = 0.4536千克 

print(f"Let's talk about {name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + my_height + my_weight
print(f"If I add {age}, {my_height}, and {my_weight} I get {total}.")
