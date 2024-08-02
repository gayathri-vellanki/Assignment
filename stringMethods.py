str="krIshna is everything"
print(str.upper())
print(str.lower())
print(str.title())#title case
print(str.capitalize())# convert first character to uppercase
print(str.swapcase())#swap the case
print(str.count('i'))#character count
print(str.count('e'))
print(str.count('is'))
print(str.endswith('thing'))
print(str.endswith('everything'))
print(str.endswith('is'))
print(str.endswith('g',10,22))
print(str.find('is'))#return first occurence of value,otherwise -1(same as index())
print(str.find('god'))# -1
str="Python is easy programming language"
s=""
l=[]
for i in str:
    if i==" ":
        print(s)
        l=l+[s]
        s=""
    else:
        s=s+i
l=l+[s]
print(s)
print(l)
print(l[::-1])
revs=""
revW=""
for i in l[::-1]:
    revs=revs+i+" "
    revW=revW+i[::-1]+" "
    print(i)
print(revs)
print(revW)
SW=""
Rl=[]
for i in revW:
    if i==" ":
        Rl=Rl+[SW]
        SW=""
    else:
        SW=SW+i
print(Rl)
word="python"
ws=''
WordList=[]
for i in range(len(word)):
    for j in range(0,i+1):
        ws=ws+word[j]
    WordList=WordList+[ws]
    ws=''
print(WordList)
RevWord=word[::-1]
ws=''
WordList=[]
for i in range(len(RevWord)):
    for j in range(0,i+1):
        ws=ws+RevWord[j]
    WordList=WordList+[ws]
    ws=''
print(WordList)

#Count of vowels
s="gayathrii"
vowels="aeiou"
vcount=0
for i in s:
    if i in vowels:
        vcount=vcount+1
print("count of vowels in string:",vcount)

#Replace vowels with "z" in string
st=""
for i in s:
    if i in vowels:
        st=st+'z'
    else:
        st=st+i
print("string after replacing with 'z' in vowels:",st)

#counting words in string
s="python is good programming language"
count=0
for i in s:
    if i == " ":
        count=count+1
count=count+1
print("Number of words in string:",count)
revst=""
for i in s:
    revst=i+revst
print("Reverse of string:",revst)

str="Python is easy programming language"
nl=[]
rs=""
count=0
lt=list(str.split(" "))
for i in range(len(lt)):
    if i%2 != 0:
        for j in l[i]:
            rs=j+rs
        nl=nl+[rs]
    else:
        nl=nl+[l[i]]
print(nl)
print(" ".join(nl))