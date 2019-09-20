t=int(input())
result=[]
if t<=10000:
    while t!=0:
        i=input()
        if(int(i.split()[0]) * int(i.split()[1]) >=  int(i.split()[2]) * int(i.split()[3])):
            result.append("Escape is possible.")
        else:
            result.append("Box cannot be dropped.")
        t-=1

for j in result:
    print(j)