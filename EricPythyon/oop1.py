class student:
    def __init__(self,firstname,age,course,gender):
        self.firstname =firstname
        self.age = age
        self.course = course
        self.gender = gender

    def study(self):
        print(self.firstname,"is studying")

student1 = student("Job",21,"MIT","Male")
student1.study()
print(student1.gender)
student2 = student("Ann",19,"datascience","female")
student3 = student("Eric",27,"cybersecurity","male")
student4 = student("Kelvin",18,"software engineering", "male")