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
