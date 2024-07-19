s="abcdefghijklmn"
n=4
count=0
st=""
lt=[]
for i in s:
    st=st+i
    count += 1
    if count==n:
        print(st)
        lt=lt+[st]
        st=""
        count=0
print(st)
lt=lt+[st]
print(lt)
#using funtion
import textwrap
def wrap(string, max_width):
    count=0
    l=[]
    st=""
    for i in string:
        st=st+i
        count += 1
        if count==max_width:
            l=l+[st]
            st=""
            count=0
    l=l+[st]
    return "\n".join(l)
        
if __name__ == '__main__':
    string= input()
    max_width=int(input())
    result = wrap(string, max_width)
    print(result)