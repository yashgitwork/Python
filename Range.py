#range() function starts at 0 by default, and stops one number below the number passed to it.
#You can use the list() function to efficiently generate a large list of numbers.

for no in range(1001):
 print (no)
 
#print number from 1-1000
for no in range(1,1001): 
 print (no)
 
# create a list of numbers from 1 to a million.
numbers=list (range(1,100001))

numbers= [i for i in range(1,11) ]
print (numbers)
