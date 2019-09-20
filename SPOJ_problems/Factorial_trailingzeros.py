# Find trailing zeros of a factorial
def num_of_zeros(x):
    result,i = 0,5
    while i < x:
        result = result + (x // i)
        i *= 5
    return result

n = int(input())
if n<=100000:
    l=[int(input()) for i in range(0, n)]
    [print(num_of_zeros(i)) for i in l if i>=1 and i<=1000000000]