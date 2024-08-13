f1=open('file handling\word.txt','r')
count=0
lcount=0
for i in f1.read():
    count=count+1
print(count)
f1.close()