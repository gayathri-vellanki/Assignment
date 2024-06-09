#read 3 numbers and find arithmetic operations
A=int(input("Enter num1:"))
B=int(input("Enter num2:"))
C=int(input("Enter num3:"))
print("Addition:",(A + B) + C)
print("subtraction:",(A - B) - C)
print("Multiplication:",(A * B) * C)

#Read principle,time and rate from user and find Simple interest
p= float(input("Enter Principle:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate:"))
SI=(p * t * r)/100
print("Simple Interest:",SI)

#Read radius and find area of the circle
r=float(input("Enter Radius:"))
pi=3.14
area= pi * r * r
print("Area of the circle:",area)

#read and print name of a person
name=input("Enter Name:")
print("Name of the person:",name)