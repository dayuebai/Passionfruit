#!/usr/local/bin/python3

import random

candidates = ["Alice","Bob","Charlie"]

def lstToStr(lst):
    str = ""
    for s in lst:
        str += s + ","
    return str[:-1]

f = open("win-data-full", "w")
for i in range(800001):
    random.shuffle(candidates)
    f.write(lstToStr(candidates)+"\n")

f.close()