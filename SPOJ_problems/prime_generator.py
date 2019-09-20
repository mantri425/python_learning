# My solution which shows TLE on spoj
import time
start_time=time.time()
primes=[2]

def check_prime(x):
    if x>=2 and x%2!=0:
        for i in range(3,int(x**0.5)+1,2):
                # print(i,int(x**0.5)+1,x)
                if x%i==0:
                    return False
        return True
    else: return False

def ran(x,y):
    prime_nos=[]
    for i in range(x,y+1):
            if i in primes:
                prime_nos.append(i)
            else:
                if check_prime(i):
                    primes.append(i)
                    prime_nos.append(i)

    return prime_nos

#
# print(ran(1,123))
# print(primes)

num=int(input())
result=[]
for i in range(num):
    k=str(input())
    if int(k.split()[0])<int(k.split()[1]):
        result.append(ran(int(k.split()[0]),int(k.split()[1])))
    else:
        print("{} is greater than {}".format(k.split()[0],k.split()[1]))
        break

for i in result:
    print("\n")
    for j in i:
        print(j)
print("--- %s seconds ---" % (time.time() - start_time))

# Sieve segmented solution
