from functools import reduce

def map_func(x):
    return x * x 

def reduce_func(x, y):
    return x + y 

l = [1,2,3,4]
m = map(map_func, l)
print(list(m))
f = filter(lambda x: x > 2, l)
print(list(f))
print(reduce(reduce_func, l))
