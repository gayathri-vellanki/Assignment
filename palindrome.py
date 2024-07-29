num=int(input("Enter Number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if temp==rev:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

##Armstrong number
num1=int(input("Enter Number:"))
temp=num1
sum=0
while(num1>0):
    dig=num1%10
    sum=sum+dig**3   #sum=sum+(dig*dig*dig)
    num1=num1//10
if sum==temp:
    print("Number is Armstrong")
else:
    print("Not Armstrong")

##string Palindrome
s=input("Enter String:")
rev=""
re=""
for i in range(len(s)-1,-1,-1):
    rev=rev+s[i]
for i in range(len(s)):
    re=s[i]+re
if s==rev:
    print("String is palindrome")
else:
    print("Not a palindrome")

    