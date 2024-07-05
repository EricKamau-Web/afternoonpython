#  inbuilt functions/standard library function
number = max(56,78,100) #determines the largest value
print(number)

y = min(67,23,3,90)
print("the minimum value is" , y)

#User-defined functions
def name():
    print("Eric")

name() # calling a function

def student() :
    firstname = "Eric"
    course = "MIT"
    age = 27
    print(firstname,course,age)

student()

#parameters and arguments

def add(num1,num2) :
    print(num1 + num2)

add(10,56)
add(34,65)
add(89,56)

def employee(fullname,age,salary,position,maritalstatus) :
    print(fullname,age,salary,position,maritalstatus)

employee("Mary MUthoni",56,60000,"receptionist","single")
employee("Eric Kamau",27,100000,"CEO","single")
employee("Brian kimani",35,60000,"Treasurer","single")
employee("Eshter njoki",47,40000,"secretary","married")
employee("Nancy  Njeri",56,900000,"Manager","married")

def product(x,y) :
    print(x * y)
product(12,36)
product(144,306)
product(1252,3026)
product(1289,3687)
