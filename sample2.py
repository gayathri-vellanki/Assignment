import random
n=int(input("Enter number:"))
l=[]
for i in range(n):
    ele=random.randint(1,1000)
    l.append(ele)
print(l)
s=sorted(l)   
print(s)