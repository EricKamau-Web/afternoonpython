# a class is a blueprint of an object
# object is an instance of a class

class  person:
    #This are the properties/attribue/variable/characteristic
    name = "Eric"
    age = 25
    gender = "male"


    #Behavior/methods/function
    def walk(self):
        print("person is walking")


person1 = person()
print(person1.gender)
print(person1.name)

person1.walk()