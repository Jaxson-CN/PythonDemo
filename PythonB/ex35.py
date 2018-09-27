# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 

from sys import exit # 导入exit包

# 定义gold_room函数
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    # if分支语句，判断输入是否为数字（此处需要改进）
    if "0" in choice or "1" in choice:
        how_much = int(choice) # 将输入结果转换为int类型
    else:
        dead("Man, learn to type a number.") # 调用dead函数

    # 判断输入金额是否大于50
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


# 定义bear_room函数
def bear_room():
    print("There is a bear here,")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False # 为下面的while循环创造循环条件

    while True: # while循环
        choice = input("> ")

        if choice == "take honey": # 判断字符串是否相同
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True # 改变判断条件
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start() # 开始运行的地方，调用start()函数，整个代码块与游戏内容基本上为倒着进行的
