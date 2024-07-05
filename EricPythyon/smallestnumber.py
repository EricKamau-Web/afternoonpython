

first = int(input("enter firstnumber:"))
second= int(input("enter secondnumber:"))
third= int(input("enter thirdnumber:"))
forth = int(input("enter forthnumber:"))

if first<second and first<third and first<forth:
    print(first,"is the smallest")
elif second<first and second<third and second<forth:
    print(second,"is the smallest ")
elif third<first and third <second and third<forth:
     print(third,"is the smallest")
else:
     print(forth,"is the smallest number")