def fibonacci(N=10):
    a = 1
    b = 2
    while a < N:
        yield a
        a, b = b, a + b
print( sum(i for i in fibonacci(10000000) if i % 2 == 0 ))
