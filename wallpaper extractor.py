# -*- coding: utf-8 -*-
"""
Wallpaper extractor program

used to find widnows spotlight pictures and turn into png's to browse through
"""
import os
import shutil as sht
import random as rnd

##############################################################

main_dir = "C:\\Users\\Sohraab\\Desktop\\assets_bkp\\"  # future wallpaper directory

src = 'C:\\Users\\Sohraab\\Desktop\\Assets'         # where spotlight pics stored
dst = main_dir

sht.copytree(src, dst)

###############################################################

folder = main_dir   
files = [f for f in os.listdir(folder)]     #list of files copied
a = len(files)      #number of files in list of files
names_int = [rnd.randrange(1, 99999, 1) for _ in range(a)]      #assign random integer to each file
names_str = list(map(str, names_int))       #convert each integer to string for future renaming

names_list = []     #empty list also used for future renaming

for name in names_str:
    a=os.path.join("C:\\Users\\Sohraab\\Desktop\\assets_bkp\\" + name + "." + "png")
    names_list.append(a)        #new file names made, including abs path of renamed files

###############################################################

for (file, name) in zip(files, names_list):
    os.rename(os.path.join(main_dir, file), os.path.join(main_dir, name))       #files renamed and thus converted to pictures

###############################################################
