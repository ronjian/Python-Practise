# python mutable, inmutable
print("init a, b as same int number, c point to a")
a = 123
b = 123
c = a
print("a @{}, b@{} c@{}".format(id(a), id(b), id(c)))
print("change a")
a = 456
print("a @{}, b@{} c@{}".format(id(a), id(b), id(c)))
print("==========================================")
print("init a, b as list with same value, c point to a")
a = [1,2,3]
b = [1,2,3]
c = a
print("a @{}, b@{} c@{}".format(id(a), id(b), id(c)))
print("append value in a")
a.append(4)
print("a @{}, b@{} c@{}".format(id(a), id(b), id(c)))
print("==========================================")
print("init a, b as tuple with same value, c point to a")
a = (1, 2)
b = (1, 2)
c = a
print("a @{}, b@{} c@{}".format(id(a), id(b), id(c)))
print("add value in a")
a += (3,)
print("a @{}, b@{} c@{}".format(id(a), id(b), id(c)))

"""
init a, b as same int number, c point to a
a @4496983872, b@4496983872 c@4496983872
change a
a @4498300656, b@4496983872 c@4496983872
==========================================
init a, b as list with same value, c point to a
a @4505441416, b@4505441992 c@4505441416
append value in a
a @4505441416, b@4505441992 c@4505441416
==========================================
init a, b as tuple with same value, c point to a
a @4505443144, b@4505443208 c@4505443144
add value in a
a @4505386224, b@4505443208 c@4505443144
"""