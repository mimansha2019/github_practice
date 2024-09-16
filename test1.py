class Animal:
  def __init__(self):
    self.breed = input("Which breed is the Dog : ")
    self.name = input("What is the name of the dog : ")

  def display(self):
    print(f"Name : {self.name}")
    print(f"Breed : {self.breed}")
