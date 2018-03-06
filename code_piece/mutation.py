# python mutable, inmutable
print("init a, b as same int number")
a = 123
b = 123
print("a @{}, b@{}".format(id(a), id(b)))
print("changing a")
a = 456
print("a @{}, b@{}".format(id(a), id(b)))
print("init a, b as same list value")
a = [1,2,3]
b = [1,2,3]
print("a @{}, b@{}".format(id(a), id(b)))
print("append value in a")
a.append(4)
print("a @{}, b@{}".format(id(a), id(b)))
print("init a, b as same tuple")
a = (1, 2)
b = (1, 2)
print("a @{}, b@{}".format(id(a), id(b)))
print("add value in a")
a += (3,)
print("a @{}, b@{}".format(id(a), id(b)))