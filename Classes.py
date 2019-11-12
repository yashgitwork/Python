#A class defines the behaviour of the object and the kind of information an object can store.
#The information is stored in the form of attributes and functions that belong to a  class are called methods.
#A child class inherits the attributes from its parent class.


class Dog(object):

 def __init__(self,name):
  self.name=name
  
 def sit(self):
  print (self.name + " Sitdown.")
  
  
my_dog=Dog("Jhonny")
 
print (my_dog.name)
my_dog.sit()
