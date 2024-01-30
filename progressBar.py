# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 11:27:31 2024

@author: jemcm
"""
import time


print("Hello", end="\r") #you need to end every line with \r
time.sleep(1)
print("\rWhats Up?\r") #and begin the new replacement line with \r 
time.sleep(.5)
print("\rLoading...")

for i in range(11):
    arrow = i * "█"
    space = (10-i) * " "
    percent = i * 10
    print(f"\r|{arrow}{space}| {percent}%", end="\r") # use 'f' to allow for formatting, and {} to input variables 
    time.sleep(.5)
print("\nDone!")