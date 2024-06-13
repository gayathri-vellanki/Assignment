#------string-------

#question 1
Institute="PALLE TECHNOLOGIES"
#printing 'T' using positive and negative indexing
print(Institute[6])
print(Institute[-12])
#printing 'G' 
print(Institute[14])
print(Institute[-4])
#printing 'H'
print(Institute[9])
print(Institute[-9])
#printing 'S'
print(Institute[17])
print(Institute[-1])

#question 2
stmt="I AM LEARNING PYTHON AT PALLE TECHNOLOGIES"
print("LENGTH OG STRING:",len(stmt))
print("printing using forward slicing")
print(stmt[0])
print(stmt[2:4])
print(stmt[5:13])
print(stmt[14:20])
print(stmt[21:23])
print(stmt[24:29])
print(stmt[30:])
print("printing using backward slicing")
print(stmt[-42])
print(stmt[-40:-38])
print(stmt[-37:-29])
print(stmt[-28:-22])
print(stmt[-21:-19])
print(stmt[-18:-13])
print(stmt[-12:])

#question 3
quote="PRACTICE MAKES MAN PREFECT"
print(quote[0:8])
print(quote[9:14])
print(quote[15:18])
print(quote[19:])
print(quote[-1:-8:-1])
print(quote[-13:-18:-1])
print(quote[0::2])
print(quote[-1::-2])
print(quote[-2::-2])

#question 4
#str1=input("str1=")
#str2=input("str2=")
str1="PALLE"
str2="TECHNOLOGIES"
print("output=",str1+str2)
print("Output=",str1[::-1]+str2[::-1])

#-----LIST----
numbers=[10,20,30,40]
numbers[0:5]=["ten","twenty","thirty","fourty"]
print(numbers)

#q-2
details=[1,"name","place","course"]
print(details[0:2])
print(details[-2:])

#q-3
subjects=["english","mathematics","science","computers","hindi"]
print(subjects[0:3])
print(subjects[1:4])
print(subjects[-1:-4:-1])

#------tuple--------
numbers=(10,20,30,40,50,60,70,80,90)
print(numbers[0::2])
print(numbers[1::2])
print(numbers[-1::-2])
print(numbers[-2::-2])
print(numbers[1:5])
numbers=list(numbers)
numbers[1]="twenty"
print(tuple(numbers))

#--list--
details=[['ramesh','suresh'],
         ['banglore','hyderabad','delhi'],
         [10,20,30,['ten',"twenty","thirty"]]]
print(details[0][1])
print(details[1][1])
print(details[2][2])
print(details[2][3][2])
print(details[1][2])
print(details[0][0])
print(details[2][3][1])
details[0][1]="vignesh"
details[1][2]="varanasi"
print(details)

#---set----
set1={"rajesh","suresh","vignesh","manish"}
print(set1)
for i in set1:
    print(i)
#print(set1[1]) --error---

numbers={10,20,20,40,59,40,67,89,67}
print(len(numbers))
print(numbers)
#str to set
institute="palle technologies"
print(set(institute))
#list to set
My_students=["amitab","ms dhoni","abdul kalam","narendra modi","ms dhoni"]
print(set(My_students))

#----range-----
num5=range(5,101,5)#5 multiples
print(list(num5))
print(list(range(40,3,-4)))#4 multiples
print(list(range(99,10,-2)))#odd in list
print(tuple(range(50,1,-2)))#even in tuple



