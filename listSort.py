#Ascending order
l=[3,5,2,7,1,0,2]
print("original list:",l)
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("Sorting in ascending order:",l)

#descending order
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print("Sorting in descending order:",l)
