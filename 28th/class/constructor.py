class Dog:
  species="Canis familiaris"

  def __init__ (self,name,age,color):
    self.name=name
    self.age=age
    self.color=color
  def desc(self):
    return f"{self.name} is {self.species} {self.age} years old"
  def speak(self,sound):
    return f"{self.name} says {sound}"
  def walk(self,style):
    return f"{self.name} walks in {style}"

my_dog =Dog("Buddy",3,"red")
print(my_dog.color)
print(my_dog.desc())
print(my_dog.speak("Woof Woof"))
print(my_dog("random"))