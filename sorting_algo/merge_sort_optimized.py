import random
x=random.choices(range(1,10000),k=1000)
print(x)

def sortandmerge(a,b):
    c=[]
    while len(a)>=1 and len(b)>=1:
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])
    return c+a+b

def divide_sort(x):
    if len(x) ==1: return x
    else:
        b=len(x)//2
        return sortandmerge(divide_sort(x[0:b]),divide_sort(x[b:len(x)]))

# print(divide_sort(x))