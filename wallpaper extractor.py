# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import shutil as sht
import random as rnd

#os.makedirs('C:\\Users\\Sohraab\\Desktop\\spotlight pics')

src = 'C:\\Users\\Sohraab\\Desktop\\Assets'
dst = 'C:\\Users\\Sohraab\\Desktop\\assets_bkp'

sht.copytree(src, dst)


folder = 'C:\\Users\\Sohraab\\Desktop\\assets_bkp'   # wallpaper directory
files = [f for f in os.listdir(folder)]
a = len(files)
names = [rnd.randrange(1, 99999, 1) for _ in range(a)]
suffix = ".png"

for name in names:
    os.path.join(C:\\Users\\Sohraab\\Desktop\\, name + "." + filename_suffix)'



for (file,name) in zip(files,names):
    os.rename(file, names + ".png"))



#os.rename('C:\\Users\\Sohraab\\Desktop\\test.txt', 'C:\\Users\\Sohraab\\Desktop\\hahaha.png')
    
