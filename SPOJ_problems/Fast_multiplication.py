n = int(input())
l = [input() for i in range(0, n)]
[print(int(i.split()[0])*int(i.split()[1])) for i in l]