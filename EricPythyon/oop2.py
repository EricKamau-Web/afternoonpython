class Animal:
    def __init__(self,type,hasscales,haswings,color):
        self.type = type
        self.hasscales = hasscales
        self.haswings = haswings
        self.color = color


    def movement(self):
        print(self.type, "is moving")



Animal1 = Animal("fish",True,False,"grey")
Animal2 = Animal("bird",True,True,"grey")
Animal1 = Animal("lion",False,False,"brown")