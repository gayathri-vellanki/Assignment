with open('file handling\word.txt','r+') as f1:
    f1.write('\n')
    f1.write(" My name is gayathri")
    count=0
    wordcount=0
    for line in f1.readlines():
        count=count+1
        lines=line.split(' ')
        for i in lines:
            wordcount=wordcount+1
        print(lines)
    print(count)
    print(wordcount)