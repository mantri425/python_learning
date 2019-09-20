###########using int to str logic(which is slow) ###############

# import time
# start_time=time.time()
# n=int(input())
# num=[]
# for i in range(0,n):
#     num.append(int(input()))
#
# for i in num:
#     while True:
#         i += 1
#         if str(i)==str(i)[::-1]:
#             print(i)
#             break
# print(time.time()-start_time)

#################using math but TLE on SPOJ
from SPOJ_problems.std_input import std_in
import time
start_time=time.time()

def palindrome(x):
    sum=0
    while x>0:
        sum=(sum*10)+x%10
        x=x//10
    return sum

def next_palindrome(i):
    while True:
        i += 1
        if i==palindrome(i):
            return i

for i in std_in():
    print(next_palindrome(i))
print(time.time()-start_time)
