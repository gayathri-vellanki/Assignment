x = [10,11,-12,14,15,16,17,18,19,20,21]
#Even number list
even=list(filter(lambda i:i%2==0 and i>0,x))
print("Even in list :",even)
#odd numbers list
odd=list(filter(lambda i:i%2!=0 and i>0,x))
print("Odd in list :",odd)
#positive numbers in list
positive=list(filter(lambda i:i>0,x))
print("positive numbers in list:",positive)
#negative numbers in list
negative=list(filter(lambda i:i<0,x))
print("Negative numbers in list:",negative)
#3 multiple positive numbers
num=list(filter(lambda i:i>0 and i%3==0,x))
print("3 multiple positive numbers:",num)

#3 and 5 multiple positive numbers
num=list(filter(lambda i:i>0 and i%3==0 and i%5==0,x))
print("3 and 5 multiple positive numbers:",num)

#numbers between 10 and 15 (exclusive)
num=list(filter(lambda i:i>10 and i<15,x))
print("numbers between 10 and 15:",num)
# even index numbers
even_index_numbers=list(map(lambda i:x[i],range(0,len(x),2)))
print("Even index numbers:",even_index_numbers)
# odd index numbers
odd_index_numbers=list(map(lambda i:x[i],range(1,len(x),2)))
print("Odd index numbers:",odd_index_numbers)
#even index even numbers
e_i_e_n=list(filter(lambda i:i%2==0 and i>0,map(lambda i:x[i],range(0,len(x),2))))
print("Even index even numbers",e_i_e_n)
#even index odd numbers
e_i_o_n=list(filter(lambda i:i%2!=0,map(lambda i:x[i],range(0,len(x),2))))
print("Even index odd nubers:",e_i_o_n)
#odd index odd numbers
o_i_o_n=list(filter(lambda i:i%2 !=0 ,map(lambda i:x[i],range(1,len(x),2))))
print("Odd index odd numbers:",o_i_o_n)
#odd index even numbers
o_i_e_n=list(filter(lambda i:i%2==0 ,map(lambda i:x[i],range(1,len(x),2))))
print("Odd index odd numbers:",o_i_e_n)
# Reverse order
reverse=list(map(lambda i:x[i],range(len(x)-1,-1,-1)))
print("List in reverse order:",reverse)
#Alternate elements
alt=list(map(lambda i:x[i],range(0,len(x),2)))
print("Alternate Elements:",alt)
#printing elements as tuple 
asTup=tuple(map(lambda i:x[i],range(0,len(x))))
print("Printing as tuple:",asTup)
#printing First half
firstHalf=list(map(lambda i:x[i],range(0,len(x)//2)))
print("First Half of list:",firstHalf)
#printing second half
secondHalf=list(map(lambda i:x[i],range(len(x)//2,len(x))))
print("Second Half of list:",secondHalf)
#alternate elements reverse
altreverse=list(map(lambda i:x[i],range(len(x)-1,-1,-2)))
print("ALternate Elements in reverse:",altreverse)
#printing last 3 elements
#printing First half
last3=list(map(lambda i:x[i],range(len(x)-3,len(x))))
print("last 3 elements of list:",last3)

y = [10,11,12,14,15,16,17,18,19,20]
#replace even number as "palle"
replace=list(map(lambda i:"palle" if i%2 == 0 else i,y))
print("Replacing with 'palle' in even numbers:",replace)
#replace odd number as "palle"
replace=list(map(lambda i:"palle" if i%2 != 0 else i,y))
print("Replacing with 'palle' in odd numbers:",replace)
#replacing even index as "palle"
replace=list(map(lambda i:"palle" if i%2 == 0 else y[i],range(0,len(y))))
print("Replacing even index as 'palle':",replace)
#replacing odd index as "palle"
replace=list(map(lambda i:"palle" if i%2 != 0 else y[i],range(0,len(y))))
print("Replacing odd index as 'palle':",replace)
# Using map and lambda to replace even-indexed even numbers with "python"
replace = list(map(lambda i: "python" if (i % 2 == 0 and y[i] % 2 == 0 and y[i] > 0) else y[i], range(len(y))))
print("Replace Even index even number with 'python':",replace)
# Using map and lambda to replace even-indexed odd numbers with "python"
replace = list(map(lambda i: "python" if (i % 2 == 0 and y[i] % 2 != 0 and y[i] > 0) else y[i], range(len(y))))
print("Replace Even index odd number with 'python':",replace)
# Using map and lambda to replace odd-indexed odd numbers with "python"
replace = list(map(lambda i: "python" if (i % 2 != 0 and y[i] % 2 != 0 and y[i] > 0) else y[i], range(len(y))))
print("Replace ODD index even number with 'python':",replace)
# Using map and lambda to replace odd-indexed odd numbers with "python"
replace = list(map(lambda i: "python" if (i % 2 != 0 and y[i] % 2 == 0 and y[i] > 0) else y[i], range(len(y))))
print("Replace ODD index even number with 'python':",replace)























# Sample list of numbers
numbers = [10, 15, 22, 35, 40, 50, 60, 70, 80, 90]
# Filtering even indexed even numbers using lambda
even_index_even_numbers = list(filter(lambda x: x[1] % 2 == 0, [(i, numbers[i]) for i in range(len(numbers)) if i % 2 == 0]))
# Extracting just the numbers from the filtered result
result = [x[1] for x in even_index_even_numbers]
print(result)
