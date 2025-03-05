#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    listed_name = s.split(" ")
    new_list = []
    for i in listed_name:
        if i and i[0].isalpha():
            new_list.append(i.capitalize())
        else:
            new_list.append(i)
    x = " ".join(new_list)
    print (listed_name)
    return x
    
    

if __name__ == '__main__':
    

    s = input()

    result = solve(s)

    
    