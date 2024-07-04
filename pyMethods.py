l=[]
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.append(7)
l.append(8)
l.append(9)
l.append(10)
print(l)
ind=int(input("Enter position to insert:"))
ele=int(input("Enter element to insert:"))
l.insert(ind,ele)
print(l)
elem=int(input("Enter element to delete from list:"))
if elem in l:
    l.remove(elem)
else:
    print("Element is not present")
print(l)
pos=int(input("enter position to delete element:"))
if pos<len(l):
    l.pop(pos)
else:
    print("index out of range")
print(l)
element=int(input("enter element:"))
if element in l:
    print(l.index(element))
else:
    print("-1")