#Lists stores a series of items in a particular order.
#You access items using an index, or within a loop.


countries = ['India', 'USA', 'Nepal', 'Israel', 'Norway' ,'Sweden', 'Finland']
first_bike = countries[0]
last_bike = countries[-1]


print(first_bike)
print(countries[1])
print(last_bike)

#Looping through a list

for country in countries:
    print (country)
    
#Adding Items to a list

companies=[]

companies.append("Intel")
companies.append("Google")

#storing square of no's
squares = []

for x in range(1,10):
 squares.append(x**2)

for x in range(1,9): 
 print(squares[x])


#Slicing a List: A portion of a list is called slice.To slice a list start with the index of first item you want, put a colon and the index
#                of the last item you want.Leave off the first index to start at the beginning of the list, and leave off the last index to
#                slice throught the end of the list.





companies=['Intel', 'Mellanox', 'Google', 'Marvell', 'Qlogic', 'Cavium', 'Xoriant']

#getting the first three elements.
first_three=companies[:3]
print (first_three)

#Getting the first to 
first_to_third=companies[1:4]
print(first_to_third)

#Getting the last three elements.

last_three=companies[-3:]
print(last_three)

#Copying a list

copy_of_companies=companies[:]
print (copy_of_companies)
