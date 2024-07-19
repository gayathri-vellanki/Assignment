#odd
l=[10,11,14,-16,-12,-13,15,17,18,-19,20]
i=0
evensum,oddsum=0,0
print("odd Numbers:")
while i<len(l):
    if l[i]%2 != 0 and l[i]>0:
        print(l[i])
        oddsum=oddsum+l[i]
    elif l[i]%2 == 0 and l[i]>0:
        evensum=evensum+l[i]
    i=i+1
print("OddNumbers sum:",oddsum)
print("Even Numbers sum:",evensum)
print("Alternate index even numbers")
i=0
evenAltSum=0
while i<len(l):
    if l[i]%2==0 and l[i]>0:
        print(l[i])
        evenAltSum=evenAltSum+l[i]
    i=i+2
print("Even numbers alternative index sum:",evenAltSum)
print("Alternate index odd numbers")
i=0
oddAltSum=0
while i<len(l):
    if l[i]%2!=0 and l[i]>0:
        print(l[i])
        oddAltSum=oddAltSum+l[i]
    i=i+2
print("Odd numbers alternative index sum:",oddAltSum)
#multiply value with index position
x=[10,11,14,-16,-12,-13,15,17,18,-19,20]
y=[]
i=0
z=0
while i<len(x):
    z=x[i]*i
    y=y+[z]
    i=i+1
print(y)
print("Sum of odd index even numbers:")
l=[10,11,14,-16,-12,-13,15,17,18,-19,20]
i=0
oddindexEvensum=0
oddindexOddsum=0
while i<len(l):
    if i%2 != 0:
        if l[i]%2 == 0 and l[i]>0:
            oddindexEvensum=oddindexEvensum+l[i]
        elif l[i]%2 != 0 and l[i]>0:
            oddindexOddsum=oddindexOddsum+l[i]
    i=i+1
print(oddindexEvensum)
print("Sum of odd index odd numbers:",oddindexOddsum)


##find biggest even number present in a list
lt=[20,24,34,12,31,98]
nl=[]
for i in range(len(lt)):
    if lt[i]%2==0:
        nl=nl+[lt[i]]
maxi=nl[0]
for i in nl:
    if i>maxi:
        maxi=i
print("Biggest Even Number in list:",maxi)