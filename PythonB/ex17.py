# !/usr/bin/env python 
# -*- coding: UTF-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
'''
in_file = open(from_file)
indata = in_file.read()
'''
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
'''对应上文多行注释
in_file.close() # 上文中没有定义in_file，所以这句没有必要
'''

