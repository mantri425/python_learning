from sorting.merge_sort_optimized import divide_sort
t=int(input())
data=[]
if t<=5:
    # data=[[input() for j in range(int(input()))] for i in range(t)]
    for i in range(t):
        k=int(input())
        if k<=100000:
            data1={}
            for j in range(k):
                l=input().strip()
                if l in data1:
                    data1[l]+=1
                else:
                    data1[l]=1
        data.append(data1)
        input()

for i in data:
    for j in divide_sort(list(i.keys())):
        print("{} {}".format(j,i[j]))
