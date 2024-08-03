fact=1
num=int(input("Enter number to find factorial:"))
for i in range(1,num+1):
    fact=fact*i
print("facatorial of number:",fact)

num=int(input("enter number to find range of factorials:"))
for i in range(1,num+1):
    fact=1
    if i==0 or i==1:
        print("1",end=" ")
    else:
        for j in range(2,i+1):
            fact=fact*j
        print(fact,end=" ")
            
    