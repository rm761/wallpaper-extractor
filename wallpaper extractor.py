# -*- coding: utf-8 -*-
"""
Wallpaper extractor program - extracts windows spotlight images stored on your account

Set main_dir as destination for where you want wallpapers to be extracted to
Keep src as it is but change user to your own username
In both of the above, set "User" to whatever your own user account is called
"""
import os
import shutil as sht
import random as rnd
import PIL as pil

##############################################################

main_dir = "C:\\Users\\User\\Desktop\\Windows Spotlight Pictures\\"  # future wallpaper directory

src = (r'C:\Users\User\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets')         # where spotlight pics stored
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
    a=os.path.join(main_dir + name + "." + "png")
    names_list.append(a)        #new file names made, including abs path of renamed files

###############################################################

for (file, name) in zip(files, names_list):
    os.rename(os.path.join(main_dir, file), os.path.join(main_dir, name))       #files renamed and thus converted to pictures

###############################################################

files2 = [f for f in os.listdir(folder)]        #list of files with edited names

os.chdir(main_dir)     #change directory as loop below doesn't work otherwise

for file in files2:
    im = pil.Image.open(file)       #using PIL and image to obtain image properties
    if im.size != (1920, 1080):
        im.close()                  #if dont close object/file then cant delete as being used by program
        path = os.path.join(main_dir, file)
        os.remove(path)
    elif im.size == (1920, 1080):
        im.close()
        
os.chdir(r"C:\\Users\\User\\Desktop\\wallpaper extractor")
