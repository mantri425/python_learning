
import random
# with duplicates
A=random.choices(range(1,100),k=10)
# without duplicates
# A=random.sample(range(10),10)
print(A)
for i in range(1,len(A)):
        while i>0 and A[i-1] > A[i]:
            c=A[i]
            A[i]=A[i-1]
            A[i-1]=c
            i-=1

print(A)

