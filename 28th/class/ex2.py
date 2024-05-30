class car:
 

  def __init__ (self,name,model,type):
    self.name=name
    self.model=model
    self.type=type
     
  def drive(self):
    return f"{self.name} is my car name and {self.model} is its model its type is {self.type}"
my_car=car("Honda","s007","SUV")
print(my_car.name)
print(my_car.model)

print(my_car.drive())