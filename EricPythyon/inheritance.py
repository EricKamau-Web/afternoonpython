#parent class and child class

class Animal:
    def speak(self):
        print("Animal is speaking")

    def movement(self):
        print("Animal is moving")

class Duck(Animal):
    def Quack(self):
        print("Duck is quacking")

class Bee:
    def Buzz(self):
        print("Bee is buzzing")

a = Animal()
a.movement()



d = Duck()
d.Quack()



b = Bee()
b.Buzz()