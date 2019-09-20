import random
x=random.choices(range(1,100),k=10)
print(x)

def large(a,b):
    if a<b: return b
    else: return a

def find(x):
    if len(x)==1: return x[0]
    else:
        b=len(x)//2
        return large(find(x[0:b]),find(x[b:len(x)]))
print(find(x))