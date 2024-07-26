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

####
# n=5
# list=[1,2,1,2,3]
# here, 1 appears 2times and 2 appears 2 times, and 3 1 time .hence count is[2,2,1]
#here the maximum is 2 which appears 2 times .Hence output is 2.

