s="hello world"
st=""
for i in range(len(s)):
    if i==0:
        st=st+s[i].upper()
    elif s[i-1]==" ":
        st=st+s[i].upper()    
    else:
        st=st+s[i]
print(st)

