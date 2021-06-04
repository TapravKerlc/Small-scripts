# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:29:57 2021

@author: lukako
"""
import os
import shutil

def my_func(file_name, n):
    try:
           shutil.copytree('c:\Testno', 'c:\Testno\+str(n))')
    except FileExistsError as f_err:
        my_func(file_name, n+1)

os.chdir(r'c:\\Testno') #set to server location
print(os.getcwd())
os.listdir() #prebere lokacijo z datotekami
try:
    shutil.copytree('c:\Testno', 'c:\Testno\Backup')
except FileExistsError:
    os.makedirs(os.path.join(os.getcwd(), "backup"))
    
