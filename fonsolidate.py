#!/usr/bin/python3
#RSMCANADA  -  IGNATIUS MICHAEL
#SIMPLE CONSOLIDATION SCRIPT

file1 = input("The name of file 1: ")
file2 = input("The name of file 2: ")

f1 = open(file1, 'r')
value1 = f1.read().splitlines()
f1.close()

f2 = open(file2, 'r')
value2 = f2.read().splitlines()
f2.close()

newvalue = []

#CHECK IF THERE ARE DUPES
for i in value1:
    for j in value2:
        if i == j:
            newvalue.append(i)

#CHECK IF VALUE IS UNIQUE
for i in value2:
    if i not in value1:
        newvalue.append(i)
f = open("newfile.txt", 'w')
for item in newvalue:
    f.writelines(item+'\n')
f.close

print(newvalue)

