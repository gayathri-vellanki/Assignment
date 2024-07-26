n=int(input("Enter number of Elements to list: "))
l=[]
for i in range(n):
    ele=input()
    l.append(ele)
k=set(l)
maxi=[]
for i in k:
    s=l.count(i)
    maxi.append(s)
print(maxi)
high=max(maxi)
print(maxi.count(high))
