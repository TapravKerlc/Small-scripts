# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:24:20 2021

@author: lukako
"""
import os

os.chdir(r'c:\\Testno')
if __name__ == '__main__':  # To ensure correct behavior on Windows and macOS
    vsota = 0
    fajl = open('Velikosti.txt', 'r') #to je naš začasni txt file, kamor shrani tekst
    lajne = fajl.readlines()
    for x in range(len(lajne)):
        y = lajne[x].find("size")+5
        u = 0
        for i in range(len(lajne[x])):
            i=i+y
            if lajne[x][i] == ';':
                vsota = vsota + int(lajne[x][y:u+y])
                print(lajne[x][y:u+y])
                break
            else:
                u = u+1

print(vsota)