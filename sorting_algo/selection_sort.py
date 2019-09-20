# selection sort: finding the smallest value of A and replace it with A[i]

A=[67,45,13,16,13,16,78]

for i in range(0,len(A)-1):
    c=A[i]
    for j in range(i+1,len(A)):
        if c > A[j]:
            c=A[j]
            k=j
    A.pop(k)
    A.insert(i,c)
    print(A)
print (A)