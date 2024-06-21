n=int(input("Enter Number :"))
x=0
y=1
l=[]
sum=0
while n!=0:
    print(x,end=" ")
    sum=sum+x
    l=l+[x]
    x,y=y,x+y
    n=n-1
print("\nFibonacci in list:",l)
print("Sum of fibonacci series:",sum)
print("Fibonacci series below 100:")
x=0
y=1
while x<100:
    print(x,end=" ")
    x,y=y,x+y
print("All even Fibonacci numbers below 500:")
x=0
y=1
while x<500:
    if x%2 == 0:
        print(x,end=" ")
    x,y=y,x+y
print("\nSum of all odd fibonacci numbers below 200:")
x=0
y=1
osum=0
while x<100:
    if x%2 != 0:
        osum=osum+x
    x,y=y,x+y
print(osum)




