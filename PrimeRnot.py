n=int(input("Enter Number:"))
##using while
result=False
if n==1 or n==0:
    print("Number is not prime")
else:
    i=2
    while(i<n):
        if n%i == 0:
            result=True
            break
        i=i+1
    if result:
        print("Number is not prime")
    else:
        print("Number is prime")
##method-2
c=0
for i in range(1,n+1):
    if n%i == 0:
        c=c+1
if c==2:
    print("number is prime number")
else:
    print("number is not prime")
    
#All prime numbers below 100
c=0
sum=0
for i in range(2,101):
    result=False
    j=2
    while(j<i):
        if i%j == 0:
            result=True
            break
        j=j+1
    if result:
        pass
    else:
        print(i,end=" ")
        sum=sum+i
        c=c+1
print()
print("Sum of prime numbers below 100:",sum)
print("Number of prime numbers below 100:",c)

##first 10 prime numbers
print("First 10 prime numbers:")
c=0
for i in range(2,100):
    refe=False
    j=2
    while(j<i):
        if i%j==0:
            refe=True
            break
        j=j+1
    if refe:
        pass
    else:
        print(i,end=" ")
        c=c+1
        if c==10:
            break
