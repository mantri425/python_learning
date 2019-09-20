import random
x=random.choices(range(1,100),k=15)
print (x)
# x=[4, 81, 82, 79, 22, 97, 94, 32, 26, 61, 84]
count=0
while count < len(x)-1:
    count=0
    for i in range(1,len(x)):
        if x[i-1] > x[i]:
            c=x[i-1]
            x[i-1]=x[i]
            x[i]=c
            # print(x,"after each iteration")
        else:
            count=count+1
    # print (x,"final after one complete iteration")
    # print (count)
print (x)



