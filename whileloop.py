x=[10,11,14,16,12,13,15,17,18,19,20]
print(x)
i=0
sum1=0
sum2=0
while i<len(x):
    sum1=sum1+x[i]
    i=i+1
print("sum of all elements:",sum1)
i=0
while i<len(x):
    sum2=sum2+x[i]
    i=i+2
print("Sum of alternate elements:",sum2)
i=0
sum3=0
while i<len(x):
    if i%2 != 0:
        sum3=sum3+x[i]
    i=i+1
print("Sum of odd index position elements:",sum3)

l=[10,11,14,-16,-12,-13,15,17,18,-19,20]
j=0
print("positive numbers are:")
psum=0
while j<len(l):
    if l[j]>0:
        print(l[j],end=" ")
        psum=psum+l[j]
    j=j+1
print("\n")
print("Sum of positive numbers:",psum)
print("Negative numbers in reverse order:")
nsum=0
j=len(l)-1
while j>=0:
    if l[j]<0:
        print(l[j],end=" ")
        nsum=nsum+l[j]
    j=j-1
print("\n")
print("sum of negative numbers:",nsum)    

##biggest element in list
l=[1,21,43,45,3,0]
max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print("Maximmun Element:",max)
print("Minimum Element:",min)

##searching Element in list
l=[1,2,3,4,5,6]
elem=3
pos=-1
for i in range(len(l)):
    if l[i]==elem:
        pos=i
        break
if pos==-1:
        print("Element not found")
else:
    print("Element found at position :",pos)
        