import re

string = "fizz buzz buzz fizz suzz 1287965 mizz tuzz 4567876"
z=re.findall('fizz',string)
print(z)
#all digits
dig=re.findall('\d',string)
print(dig)
#only 1-5
x=re.findall('[1-5]',string)
print(x)
#except 4-9
t=re.findall('[^4-9]',string)
print(t)
s=re.search("fizz",string)
print(s)
print(s.start())
print(s.end())#return end+1

s=re.search("4567876",string)
print(s)
print(s.start())
print(s.end())

#split at '-'
string1 = "fizz-buzz;buzz-fizz,suzz 1287965.mizz;tuzz 4567876"
s=re.split('-',string1)
print(s)
#split at ','
s=re.split(',',string1)
print(s)
#split at ', and space'
s=re.split('[,\s]',string1)
print(s)
#split at ', - ;'
string1 = "fizz-buzz;buzz-fizz,suzz 1287965.mizz;tuzz 4567876"
s=re.split('[\s.,;-]',string1)
print(s)
Institute = "palle technologies;www.tech-palle.com:www.skillgun.com"
words=re.split("[\s;.:-]",Institute)
print(words)
s=re.split('[;:]',Institute)
print(s)
s=re.split('[\s;:]',Institute)
print(s)












