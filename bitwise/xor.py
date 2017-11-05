import random

i=0
loop = 10000000
while i<loop:
    x = random.randint(1,loop)
    assert x^x == 0
    assert x^0 == x
    assert x^x^x^x^x == x^x^x == x
    assert x^10000001^x == 10000001
    i+=1
    if i % loop/10 == 0:
        print("done")

# x^x = 0
# x^0 = x
# x^x^x^x^x = x^x^x = x
# x^1000001^x == 1000001




