def fib():
    a, b = 0, 1
    while True:
        a, b = b, a+b
        yield a, b

g = fib()
for i in range(10):
    print(g.__next__())