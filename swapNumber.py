x=20
y=30
x,y=y,x
print("After Swaping: x=",x,"y=",y)
#using temp variable
temp=x
x=y
y=temp
print("After Swaping: x=",x,"y=",y)
#without temp
x=x+y
y=x-y
x=x-y
print("After Swaping: x=",x,"y=",y)
x=x^y
y=x^y
x=x^y
print("After Swaping: x=",x,"y=",y)


