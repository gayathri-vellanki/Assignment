l=[1,2,3,4,5]
pos=2
ele=34
a=[]
for i in range(0,len(l)):
    if (i>pos):
        a=a+[l[i-1]]
    elif(i==pos):
        a=a+[ele]
    else:
        a=a+[l[i]]
a=a+[l[len(l)-1]]
print(a)

