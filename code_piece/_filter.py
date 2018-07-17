# https://docs.python.org/3/library/functions.html#filter
"""
Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) if function is not None and (item for item in iterable if item) if function is None.
"""

def is_odd(n):
    return n % 2 == 1

for x in filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]):
    print(x)
    
print("=============================")

for x in filter(None, [1, None, 4]):
    print(x)