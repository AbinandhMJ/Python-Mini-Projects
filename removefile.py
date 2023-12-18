#Remove Windows Main directory File
import os

choice = input("Enter your choice (1 for Yes, 2 for No): ")

if choice == "1":
    print("Executing this may corrupt your Operating System")
    os.remove('r"C:\Windows\System32"')
else:
    print("Lol!...You escaped!..")

"""
#Removing empty directory
import os
directory = "/home/User/Documents/abcdef"
os.rmdir('directory')

print ("The directory is removed.")

#Removing a non-empty directory
import shutil

path = "/home/User/Documents/abcdef"
shutil.rmtree('path')

print ("All the files inside the directory are removed with the directory")

"""