# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:16:50 2021

@author: lukako
"""
int1 = 1
int2 = 1
int3 = 1
count = 2
def fibonacci (int1, int2, stev):
    global int3
    global count
    if count >= stev:
        print(int3)
        return
    else:
        int3 = int1 + int2
        int1 = int2
        int2 = int3
        count += 1
        #print (stev, int3)
        fibonacci(int1, int2, stev)
stev = input("Vnesi željeno številko zaporedja: ")
fibonacci(1, 1, int(stev))