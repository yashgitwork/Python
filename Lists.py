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
