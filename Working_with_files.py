#!/bin/python

file='p.txt'
#READ
with open(file,'w') as fo:
 fo.write("1. This is file created using python language +\n")
 fo.write("2. This is file created using python language +\n")

#WRITE
with open(file) as fo:
 lines=fo.readlines()


for line in lines:
 print(line)


#APPEND
with open(file,a) as fo:
 fo.write("3. This is file created using python language\n")
