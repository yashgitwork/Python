#Dictionaries store data in the form of key:value pair.
#Dctionaries store connection between pieces of information.

body={'hands':'2','face':'1','eyes':'2'}
print ("I have " + body['hands'] + "hands")

body['stomach']='1'

print (body['stomach'])


#Looping through both KEY and VALUE
for key,value in body.items():
 print(key +" : "+ value  )

#Looping through only key
for key in body.keys():
 print(key  )


#Looping through only value
for key in body.values():
 print(key  )
