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
while i<len(l):
    if l[i]%2==0 and l[i]>0:
        print(l[i])
    i=i+2