def upper_case(fun):
    def inner(x,y):
        new=[]
        s=fun(x, y)
        l=list(s)
        for i in l:
            ele=i.upper()
            new.append(ele)
        return " ".join(new)
    return inner
@upper_case
def str_fun(x,y):
    return x,y
a=str_fun("hello good morning","palle")
print(a)


def word_split(fun):
    def inner(x):
        s=fun(x)
        return s.split(" ")
    return inner
@word_split
def str_fun(x):
    return x
a=str_fun("HELLO GOOD MORNING PALLE")
print(a)