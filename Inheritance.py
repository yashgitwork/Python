#Inheritance: Child class inherits attributes from Parent class.

class Dog(object):

 def __init__(self,name):
  self.name=name
  
 def sit(self):
  print (self.name + " Sitdown.")
  


class Search_Dog(Dog):
  def __init__(self,name):
    super().__init__(name)
    
  def search(self):
   print(self.name + " is searching")
   
my_dog=Search_Dog("Kalu")
print(my_dog.name + " is a search Dog.")
 
my_dog.sit()
my_dog.search()
