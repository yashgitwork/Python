Squares=[ (i**2) for i in range(1,11)]

countries=['India',"Pakistan","Israel",'USA',6]
first_two=countries[:2]
all_except_last=countries[:-1]

copy_list=countries[:]


Players=['messi','ronaldo','neymar','sunil']

U_Players=[name.upper() for name in Players]


for name in U_Players:
 print(name)
