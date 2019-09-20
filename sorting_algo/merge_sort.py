import random
x=random.choices(range(1,100),k=11)
print (x)

def sortandmerge(a,b):
    c=[]
    while len(a)>=1 and len(b)>=1:
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])
    # print (c+a+b, "merge")
    return c+a+b
# sortandmerge([1],[0,2])

def splitarray(A):
    count=int(len(A)/2)
    LeftArray = []
    RightArray = []
    for i in range(0, count):
        LeftArray.insert(i, A[i])
    for j in range(0, len(A) - count):
        RightArray.insert(j, A[count + j])
    # print(LeftArray,"***",RightArray)
    if len(LeftArray)>1:
        LeftArray = splitarray(LeftArray)
    if len(RightArray)>1:
        RightArray=splitarray(RightArray)
    return sortandmerge(LeftArray,RightArray)


print(splitarray(x))