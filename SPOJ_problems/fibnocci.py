def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        b = a + b
        a = b - a



value = input("Enter the value:")
print(type(value))
fib(int(value))
