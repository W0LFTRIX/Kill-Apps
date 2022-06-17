#!/usr/bin/env python3

import os

new_name = input("Enter the new name for this script : ")

file = []

for x in os.listdir() :
	if x == "rename.py" or x == "README.md" or x == "LICENSE" :
		continue

	else : 
		file.append(x)




script = file[len(file) - 1]

line_number = 0

with open(script, "r") as file :
	contenu = file.readlines()

contenu[3] = f'name="{new_name}"\n'

with open(script, "w") as file : 
	for x in contenu :
		file.write(x)

os.rename(script, new_name)

print("Ok, you can reinstall it by going to : https://github.com/Wolftrix2514/Kill-Apps")





