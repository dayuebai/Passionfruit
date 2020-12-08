#!/usr/local/bin/python3

# This script counts the number of 1's in the file, and output the <key,count> pair
# argv[1] a key i.e. a word
# argv[2] a file containing a list of 1's
#
# Author: Yitan Ze, Dayue Bai
# Date: 11/23/2020

import sys

key = sys.argv[1]
filename = sys.argv[2]
count = 0

with open(filename, "r") as file:
    for line in file:
        if len(line.strip()) > 0:
            count += 1

print(key + "," + str(count))
