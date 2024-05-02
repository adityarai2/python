num1 = int(input("enter the marks of physics:"))
num2 = int(input("enter the marks of chemistry:"))
num3 = int(input("enter the marks of maths:"))
per = ((num1+num2+num3)/300)*100
print("your percentage =",per)
if (per>=90):
    print("excellent")
elif (per>=70):
    print("good")
elif(per>=50):
    print("average")
else:
    print("fail")


