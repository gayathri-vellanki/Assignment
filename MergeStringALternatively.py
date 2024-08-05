a="ab"
b="pqrs"
st=""
if len(a)>len(b):
    n=len(b)
elif len(a)<len(b):
    n=len(a)
else:
    n=len(a)   #min(len(a),len(b))
for i in range(n):
    st=st+a[i]
    st=st+b[i]
if len(a)>len(b):
    for i in range(n,len(a)):
        st=st+a[i]
else:
    for i in range(n,len(b)):
        st=st+b[i]
print(st)