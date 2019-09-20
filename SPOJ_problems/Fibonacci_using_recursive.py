#simple recursion but not efficient, exponential sequence
def fib(n):
    if n <=2: return 1
    else:
        f=fib(n-2)+fib(n-1)
        return f

print(fib(10))



# #using recursion and memorization implementation makes the algo efficient as follows, linear sequence
# import itertools
# counter=itertools.count()
# final={}
# def fib(n):
#     print("calling n this many times",next(counter))
#     if n in final: return final[n]
#     if n <=2: return 1
#     else:
#         f=fib(n-2)+fib(n-1)
#         final[n]=f
#         print(final)
#         return f
#
# print(fib(100))
# print(final)
#
# #using same memorization concept without recursion as follows, same efficency as above solution
# final={}
# def fib(n):
#     for k in range(1,n+1):
#         if k<=2:
#             final[k]=1
#         else:
#             f=final[k-2]+final[k-1]
#             final[k]=f
#     return final[n]
# print(fib(10))